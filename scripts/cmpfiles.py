#!/usr/bin/env python
""" A diff like utility that can ignore small numerical differences.

usage: cmpfiles.py [-h] [-t TOLERANCE] [-i IGNORE] [-b BEGIN] [-e END]
                  filename filename

positional arguments:
 filename              name of the input files

optional arguments:
 -h, --help            show this help message and exit
 -t TOLERANCE, --tolerance TOLERANCE
                       numerical differences below this threshold will be
                       ignored (default: 1e-13)
 -i IGNORE, --ignore IGNORE
                       regex pattern to ignore lines (default None)
 -b BEGIN, --begin BEGIN
                       regex pattern to define start of block (default:
                       beginning of the file)
 -e END, --end END     regex pattern to define end of block (default: end of
                       file)

The files are compared line by line and differing lines are compared word by
word. If the differing words store numerical values, then the relative
numerical difference is calculated. Relative differences that are smaller
than the tolerance are ignored.

It is possible to select only certain regions from the files for comparison:
using the -b and -e flags we can specify a block of lines that will be
compared, everything outside the blocks will be ignored. The input files can
store several blocks, we iterate through the block one by one and compare them
individually. See the examples for details.

Examples:
 - Compare the whole files using default settings:
  ./cmpfiles.py file1 file2

- Compare two files ignoring lines that contains 'junk':
  ./cmpfiles.py -i 'junk' file1 file2

- Using multiple ignore patterns (the second one ignores empty lines):
  ./cmpfiles.py -i 'junk' -i '^\s*$' file1 file2

Block Examples:
  Let us assume that file1 and file2 contains text like:
    ...
    intermediate results
    ...
    Final results
    Value1 1.234
    Value2 5.678

  Using blocks we can focus the comparison to the final results:
  ./cmpfiles.py --begin 'Final results' file1 file2

  Note that we did not give the --end flag, so the comparison runs till the
  end of the file. The pattern provided for --begin and --end must match the
  line from the first character. So the above example will not work if file1 has
  ' Final results' (but you could use '\s*Final results').

Blocks are useful in the following example. Assume the files have the following
format:
   Iteration 1
   intermediate results
   ...
   summary of iteration 1
   values to compare
   ...
   Iteration 2
   intermediate results
   ...
   summary of iteration 2
   values to compare
   ...

Then we can skip the intermediate results if we specify the blocks like:
./cmpfiles.py --begin 'summary of iteration' --end 'Iteration \d' file1 file2

"""


import sys
import os
import re
import difflib
import argparse

try:
    from itertools import zip_longest
except ImportError:
    from itertools import zip_longest as zip_longest

__author__ = 'Tamas Feher'
__email__ = 'tamas.bela.feher@ipp.mpg.de'

tolerance = 1e-13 # Default tolerance

num_err = 0    # numerical errors
other_err = 0  # insert, delete, or conversion errors
max_err = 0    # the largest relative error from the numerical errors

# pstart is inclusive (i.e. the matching line will be added to the block)
# pstop is exclusive (the matching line will not be added to the block)
# So the block will be created like [pstart, pstop)
pstart = None
pstop = None
pignore = None


class Block:
    """ Iterator to read blocks of lines from file.

    This class iterates through the blocks of the file. A block is a list of
    lines that are read from the input file. A block is defined by the regex
    patterns pstart and pstop. The returned block contains lines
    [pstart, pstop) and possibly omits lines that match pignore.

    The default empty patterns lead to a single block with the whole file.
    """

    _file = None
    def __init__(self, file):
        """ Initialize with a file handle """
        self._file = file

    def __iter__(self):
        return self

    def __next__(self):
        """ Reads the next block from file.

        Lines before pstart are ignored.
        Reading is suspended after pstop is reached.
        Lines that match pignore are skipped.
        """
        global pstart
        global pstop
        global pignore
        block = list()
        if pstart:
            # patterns exist to define input blocks
            # we do not store until we encounter the start pattern
            store = False
        else:
            # no blocks are defined, we store everything
            store = True
        line = self._file.readline()
        if line=="":
            raise StopIteration
        while line:
            if pstart and pstart.match(line):
                store = True
            if store and pstop and pstop.match(line):
                break
            if store and ( (not pignore) or (not pignore.search(line))):
                block.append(line)

            line = self._file.readline()
        if not store:
            # We did not find any block, we should be at the end of the file
            raise StopIteration
        return block

    next = __next__


class PrintLine:
    """ Prints error information
    """
    _text = None # text being with lines
    _wordlist = None # list of words of text with start and stop indices
    _printed = None # set of line indices that are printed already

    def __init__(self, text):
        """ initialize with the text from which we will print """
        self._text = text
        # We need to know the indices for every word, so that we can print the
        # differing lines
        self._wordlist = [(m.group(0), m.start(), m.end())
                           for m in re.finditer(r'\S+', text)]
        self._printed = set()

    def printline(self, idx, prefix):
        """ Prints the whole line that contains the word specified by its idx
        Arguments:
        idx - index of the word in wordlist
        prefix - prefix for printing the line
        """
        if idx >= len(self._wordlist):
            return
        start_idx = self._wordlist[idx][1]
        while start_idx > 0 and self._text[start_idx-1] != "\n":
            start_idx -= 1
        if not start_idx in self._printed:
            stop_idx = self._wordlist[idx][2]
            while stop_idx < len(self._text) and self._text[stop_idx] != "\n":
                stop_idx += 1
            print(prefix + self._text[start_idx:stop_idx])
            self._printed.add(start_idx)




def comparelines(text1, text2):
    """ Compares text1 and text2 word by word ignoring small numerical diffs

    Arguments
      text1 -- string (possibly multiline string)
      text2 -- string

    On exit the global variables num_err and other_err will be increased by the
    number of differences found, and max_err will store the maximum relative
    differences.

    """
    global num_err
    global max_err
    global other_err

    # Object for printing the differences on screen
    p1 = PrintLine(text1)
    p2 = PrintLine(text2)

    # Instead of character by character comparison, we compare word by word
    words1 = text1.split()
    words2 = text2.split()
    s = difflib.SequenceMatcher(None, words1, words2)

    for tag, i1, i2, j1, j2 in s.get_opcodes():
        if tag=='equal':
            continue
        elif tag=='insert':
            print('Error', tag, " ".join(words2[j1:j2]))
            other_err += 1
            continue
        elif tag=='delete':
            print('Error', tag, " ".join(words1[i1:i2]))
            other_err += 1
            continue
        for idx, (word1, word2) in enumerate(zip_longest(words1[i1:i2],
                                                         words2[j1:j2])):
            if word1!=word2:
                try:
                    f1 = float(word1)
                    f2 = float(word2)
                    if f2==0:
                        err = abs(f1-f2)
                    else:
                        err = abs((f1-f2)/f2)
                    if err > tolerance:
                        num_err += 1
                        print("Relative error {0: 4.2g} between {1} and {2}"
                              .format(err, word1, word2))
                        p1.printline(idx, '< ')
                        p2.printline(idx, '> ')
                    #else:
                        #print("error within tolerance", err, "values", f1, f2)
                    if err > max_err:
                        max_err = err
                except (ValueError, TypeError) as err:
                    print(err)
                    print("words:\n", word1, word2)
                    p1.printline(idx, '< ')
                    p2.printline(idx, '> ')
                    other_err += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "A diff like utility that "
               "can ignore small numerical differences.", epilog=__doc__[824:],
               formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("filename", type=str, nargs=2,
                help="name of the input files")
    parser.add_argument("-t", "--tolerance", type=float, default=tolerance,
                help="numerical differences below this threshold will be "
                      "ignored (default: " + str(tolerance) + ")")
    parser.add_argument("-i", "--ignore", type=str, action='append',
                help="regex pattern to ignore lines (default None)")
    parser.add_argument("-b", "--begin", type=str, action='append',
                help="regex pattern to define start of block "
                     "(default: beginning of the file)")
    parser.add_argument("-e", "--end", type=str, action='append',
                help="regex pattern to define end of block "
                     "(default: end of file)")
    args = parser.parse_args()

    if args.ignore:
        pignore = re.compile("(" + ( ")|(".join(args.ignore) ) + ")")
    if args.begin:
        pstart = re.compile("(" + ( ")|(".join(args.begin) ) + ")")
    if args.end:
        pstop = re.compile("(" + ( ")|(".join(args.end) ) + ")")

    tolerance = args.tolerance

    with open(args.filename[0],'rt') as file1, open(args.filename[1],'rt') as file2:
        d = difflib.Differ()
        for block1, block2 in zip_longest(Block(file1), Block(file2)):
            lines = list()
            # one could use SequenceMatcher instead of Differ()
            # Compare the blocks:
            for line in d.compare(block1, block2):
                if line[0:2] == "  ":
                    if len(lines)>0:
                        lines1 = "".join(difflib.restore(lines,1))
                        lines2 = "".join(difflib.restore(lines,2))
                        comparelines(lines1, lines2)
                        lines = list()
                else:
                    lines.append(line)
            if len(lines)>0:
                lines1 = "".join(difflib.restore(lines,1))
                lines2 = "".join(difflib.restore(lines,2))
                comparelines(lines1, lines2)

        if num_err > 0:
            print("There were", num_err, "numerical errors, max relative error is", max_err)
        if other_err > 0:
            print("There were", other_err, "other errors (insert/delete or conversion).")

    if num_err + other_err > 0:
        sys.exit(1)
