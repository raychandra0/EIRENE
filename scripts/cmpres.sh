#!/bin/bash
# Compare results of Eirene
# usage ./cmpres.sh dir1 dir2 [stdout_file]
#
# It compares the standard output of Eirene and the fort.44 files
#
# The first and second arguments are the directory names where the results are
# stored.
#
# The third optional argument is the name of the file that contains the 
# standard output (default is stdout). For example if you call Eirene like:
# eirobjx > eirene.log
# then use eirene.log as third argument.

STDOUT_FILE="stdout"

MYPATH=`dirname "$0"` # path to this script, used when we call cmpfiles.py

if [ ! -d "$1" ] || [ ! -d "$2" ]; then
  echo usage: ./cmpres.sh dir1 dir2
  exit 2
fi

if [ ! -z "$3" ]; then
  STDOUT_FILE="$3"
fi

get_stdout_file() {
  # returns the name of the logfile
  if [ -e "$1/output.0000" ]; then
    echo $1/output.0000
  elif [ -e $1/$STDOUT_FILE ]; then
    echo $1/$STDOUT_FILE
  else
    echo "Error, no stdout found, try to specify file name with the 3rd argument"
    exit 2
  fi
}

logfile1=$(get_stdout_file $1)
logfile2=$(get_stdout_file $2)

sort_rnd_stream() {
  # sort the random numbers according to the particle idx
  if [ -e "$1/output.0000" ]; then
    # random streams are also in these files
    grep -h RANF ${1}/output.* | grep -v ' -137 ' | sort -n -k 2 --stable > $1/random.log
  elif [ -e $1/$STDOUT_FILE ]; then
    grep -h RANF $1/$STDOUT_FILE | grep -v ' -137 ' | sort -n -k 2 --stable > $1/random.log
  else
    echo "Error, neither $STDOUT_FILE, nor output.0000 found in $1"
    exit 2
  fi
}

# First check if the random streams agree
sort_rnd_stream $1
sort_rnd_stream $2
cmp $1/random.log  $2/random.log

if [ "$?" == "0" ]; then
  echo random streams agree.
else
  echo random streams differ 
  diff $1/random.log  $2/random.log
  echo output files not compared because random streams differ
  # no need to continue if the random streams differ
  # the output will be different in that case
  exit 1
fi

# Check the output of Eirene
# Comparison starts after the "THIS IS THE SUM OVER THE STRATA" line.
# We compare until we reach the end of the file, where "TOTAL CPU_TIME..." 
# is written, or until the start of the next iteration which (marked by
# "GRNXTB CALLED FROM EIRENE.F"). 
# Some lines are ignored using the -i flag.
$MYPATH/cmpfiles.py --begin '\*  THIS IS THE SUM OVER THE STRATA' \
--end '^ TOTAL CPU_TIME OF THIS RUN' --end 'GRNXTB CALLED FROM EIRENE\.F' --end 'TIME CYCLE COMPLETED' \
-i 'tamas' -i 'RANF' -i '^\s*area     power' -i '^non-def-surf' -i '^ ncutl,ncutb' \
-i 'ndx,ndy,natm,ndxa,ndya,nfla,n1st' -i '^ nred' -i '^\[0\] MPI' \
$logfile1 $logfile2

# to ignore differences from modbgk, one could add
# -i '(^ RATM)|(^ RATE)|(^ RESE)' 

OK1="$?"
if [ "$OK1" == "0" ]; then
  echo Log files agree.
else
  sed '/RANF/d;/TOTAL CPU_TIME/d' $logfile1 > $1/eirene_preprocessed.log
  sed '/RANF/d;/TOTAL CPU_TIME/d' $logfile2 > $2/eirene_preprocessed.log
  #diff $1/eirene_preprocessed.log $2/eirene_preprocessed.log
fi

if ! cmp $1/fort.44 $2/fort.44; then
  $MYPATH/cmpfiles.py $1/fort.44 $2/fort.44
  OK2="$?"
  exit
else
  echo fort.44 files agree.
  OK2=0
fi

echo ""

exit $(( OK1 + OK2 ))
