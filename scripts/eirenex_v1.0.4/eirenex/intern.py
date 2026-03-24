#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:15:08 2020

@author: nathanbartlett
"""



    
    
    
    



def upload_files(FILE_in,FILE_out,PLS_TEMP_DATA_FILE,PLS_DENS_DATA_FILE,ATM_DENS_DATA_FILE,MOL_DENS_DATA_FILE,ION_DENS_DATA_FILE):
    '''
    upload and read lines on input and output file
    '''
    #
    #
    #
    # Process input file
    FILE_IN_OPEN = open(FILE_in)
    FILE_IN_OPEN.seek(0)
    FILE_IN_LINES = FILE_IN_OPEN.readlines()
    FILE_IN_OPEN.close()
    #---------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------------
    # Process output file
    FILE_OUT_OPEN = open(FILE_out)
    FILE_OUT_OPEN.seek(0)
    FILE_OUT_LINES = FILE_OUT_OPEN.readlines()
    FILE_OUT_OPEN.close()
    #---------------------------------------------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------------------------------------------
    
    
    PLS_TEMP_FT_DATA_LINES = 'NONE'
    if PLS_TEMP_DATA_FILE != 'NONE':
        PLS_TEMP_OPEN = open(PLS_TEMP_DATA_FILE) 
        PLS_TEMP_OPEN.seek(0)
        PLS_TEMP_FT_DATA_LINES = PLS_TEMP_OPEN.readlines()
        PLS_TEMP_OPEN.close()
        
    PLS_DENS_FT_DATA_LINES = 'NONE'
    if PLS_DENS_DATA_FILE != 'NONE':
        PLS_DENS_OPEN = open(PLS_DENS_DATA_FILE) 
        PLS_DENS_OPEN.seek(0)
        PLS_DENS_FT_DATA_LINES = PLS_DENS_OPEN.readlines()
        PLS_DENS_OPEN.close()
    
    ATM_DENS_FT_DATA_LINES = 'NONE'
    if ATM_DENS_DATA_FILE != 'NONE':
        ATM_DENS_OPEN = open(ATM_DENS_DATA_FILE) 
        ATM_DENS_OPEN.seek(0)
        ATM_DENS_FT_DATA_LINES = ATM_DENS_OPEN.readlines()
        ATM_DENS_OPEN.close()
        
    MOL_DENS_FT_DATA_LINES = 'NONE'
    if MOL_DENS_DATA_FILE != 'NONE':
        MOL_DENS_OPEN = open(MOL_DENS_DATA_FILE) 
        MOL_DENS_OPEN.seek(0)
        MOL_DENS_FT_DATA_LINES = MOL_DENS_OPEN.readlines()
        MOL_DENS_OPEN.close()
        
    ION_DENS_FT_DATA_LINES = 'NONE'
    if ION_DENS_DATA_FILE != 'NONE':
        ION_DENS_OPEN = open(ION_DENS_DATA_FILE) 
        ION_DENS_OPEN.seek(0)
        ION_DENS_FT_DATA_LINES = ION_DENS_OPEN.readlines()
        ION_DENS_OPEN.close()
        
    # Get the file name up unto the '.in'
    FILE_NAME = FILE_in.split('/')[-1].split('.')[0]
    
    
    return FILE_IN_LINES, FILE_OUT_LINES, FILE_NAME,PLS_TEMP_FT_DATA_LINES, PLS_DENS_FT_DATA_LINES,ATM_DENS_FT_DATA_LINES,MOL_DENS_FT_DATA_LINES,ION_DENS_FT_DATA_LINES






def block_11_data(FILE_IN_LINES,i, VOL_AVG_DATA_TYPES, SUR_AVG_DATA_TYPES):
    '''
    Get block 11 data
    '''
    

    
    NUM_PRINTOUT_CONDITIONAL_LIST = (FILE_IN_LINES[i+1] + FILE_IN_LINES[i+2]).replace(' ','').replace('\n','')
    VOL_AVG_NUM = int(FILE_IN_LINES[i + 3][0:8])
    SUR_AVG_NUM = int(FILE_IN_LINES[i + 3 + VOL_AVG_NUM + 1])
    #---------------------------------------------------------------------------------------------------------------------------------------------
    for j in range(VOL_AVG_NUM):
        VOL_AVG_DATA_TYPES.append(FILE_IN_LINES[i + 3 +j + 1])
    VOL_AVG_DICT = {}
    for j in VOL_AVG_DATA_TYPES:
        VOL_AVG_DICT.update({int(j[0:7]):int(j[6:12])})
    #---------------------------------------------------------------------------------------------------------------------------------------------
    for j in range(SUR_AVG_NUM):  
        SUR_AVG_DATA_TYPES.append(FILE_IN_LINES[i + 3 + VOL_AVG_NUM+ j + 2])
    SUR_AVG_DICT = {}
    for j in SUR_AVG_DATA_TYPES:
        SUR_AVG_DICT.update({int(j[0:7]):int(j[6:12])})
    
    
    
    
    return NUM_PRINTOUT_CONDITIONAL_LIST, VOL_AVG_NUM, SUR_AVG_NUM,VOL_AVG_DICT,SUR_AVG_DICT



def get_MDL(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the description of the file
    '''

    META_DESCRIPTION_LINE = FILE_OUT_LINES[FWD_MAIN_IND+2]
    
    return META_DESCRIPTION_LINE

def get_XR_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of x/radial geometric points
    '''

    XR_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25]) - 1
    
    return XR_NUM
    
    
def get_YP_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of y/poloidal geometric points
    '''
    
    YP_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25]) - 1
    
    return YP_NUM

def get_ZT_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of z/toroidal geometric points
    '''
    
    ZT_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25]) - 1
    
    return ZT_NUM

def get_ATM_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of atom species
    '''
    
    ATM_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25])
    
    return ATM_NUM

def get_MOL_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of molecule species
    '''
    
    MOL_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25])
    
    return MOL_NUM

def get_ION_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of test ion species
    '''
    
    ION_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25])
    
    return ION_NUM

def get_PLS_NUM(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of plasma species
    '''
    
    PLS_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][15:25])
    
    return PLS_NUM

def get_DATE(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the date the EIRENE run was executed
    '''
    
    DATE = FILE_OUT_LINES[FWD_MAIN_IND][8:20]
    
    return DATE

def get_TIME(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the time the EIRENE run was executed
    '''
    
    TIME = FILE_OUT_LINES[FWD_MAIN_IND][8:20]
    
    return TIME

def get_IN(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of iterations in the run
    '''
    
    ITERATION_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][40:50])
    
    return ITERATION_NUM

def get_TSN(FILE_OUT_LINES,FWD_MAIN_IND):
    '''
    get the number of time steps
    '''
    
    TIME_STP_NUM = int(FILE_OUT_LINES[FWD_MAIN_IND][40:50])
    
    return TIME_STP_NUM

def get_XR_GEODATA(FILE_OUT_LINES,FWD_MAIN_IND,i,XR_NUM):
    '''
    get the x/radial geometry defined in the run
    '''
    
    #----------------------------------
    import numpy as  np 
    
    XR_GEODATA = []
    XR_LEN = 0.0
    
    for i in range(XR_NUM+1):
                
        XR_GEODATA.append(float(FILE_OUT_LINES[FWD_MAIN_IND+1+i][5:20]))
                
    XR_GEODATA = np.array(XR_GEODATA) 
    XR_LEN = XR_GEODATA[XR_NUM] - XR_GEODATA[0]
    
    return XR_GEODATA, XR_LEN

def get_YP_GEODATA(FILE_OUT_LINES,FWD_MAIN_IND,YP_NUM):
    '''
    get the y/poloiadal geometry defined in the run
    '''
    
    #----------------------------------
    import numpy as  np 
    #----------------------------------
    
    YP_LEN = 0
    YP_GEODATA = np.zeros((YP_NUM+1))
    FWD_COND_1 = 0
    FWD_IND = 0
    
    while (FWD_COND_1 == 0):
                
        if (('   N, PSURF' in FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND]) and (FWD_COND_1 == 0)):
            
            while (len(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND]) > 5):
                
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][1:5])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][5:20])
                    YP_GEODATA[a-1] = b
                     
                except:
                    
                    pass
                         
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][20:25])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][25:38])
                    YP_GEODATA[a-1] = b
   
                except:
                    
                    pass
                    
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][38:43])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][44:55])
                    YP_GEODATA[a-1] = b
                    
                except:
                    
                    pass
                    
                FWD_IND += 1
                
            FWD_COND_1 = 1
                
        FWD_IND += 1
        
    YP_LEN = YP_GEODATA[YP_NUM] - YP_GEODATA[0] 
    
    
    
    
    return YP_LEN, YP_GEODATA

def get_ZT_GEODATA(FILE_OUT_LINES,FWD_MAIN_IND,ZT_NUM):
    '''
    get the Z/toroidal geometry defined in the run
    '''
    #----------------------------------
    import numpy as  np 
    #----------------------------------
    
    ZT_LEN = 0
    ZT_GEODATA = np.zeros((ZT_NUM+1))
    FWD_COND_1 = 0
    FWD_IND = 0
    
    while (FWD_COND_1 == 0):
                
        if (('  N,  ZSURF' in FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND]) and (FWD_COND_1 == 0)):
            
            while (len(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND]) > 5):
                
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][1:5])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][5:20])
                    ZT_GEODATA[a-1] = b
                     
                except:
                    
                    pass
                         
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][20:25])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][25:38])
                    ZT_GEODATA[a-1] = b
   
                except:
                    
                    pass
                    
                try:
                    
                    a = int(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][38:43])
                    b = float(FILE_OUT_LINES[FWD_MAIN_IND + FWD_IND+1][44:55])
                    ZT_GEODATA[a-1] = b
                    
                except:
                    
                    pass
                    
                FWD_IND += 1
                
            FWD_COND_1 = 1
            
        FWD_IND += 1
        
    ZT_LEN = ZT_GEODATA[ZT_NUM] - ZT_GEODATA[0] 
    
    return ZT_LEN, ZT_GEODATA


def BUILD_ARRAYS(TIME_STP_NUM,ITERATION_NUM,PLS_NUM,XR_NUM,YP_NUM,ZT_NUM):
    '''
    build the arrays to be filled when the output is read
    '''
    
    #----------------------------------
    import numpy as  np 
    #----------------------------------
    
    PSPC_INDX_DENS = 0 
    PLASMA_SPC_NAMES_DENS = []
    VPDA = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM])
            

    
    #Radial
    PDA1DXR_INDX_DENS = 0 
    PDA1DXR = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,XR_NUM])
    
    #Poloidal
    PDA1DYP_INDX_DENS = 0 
    PDA1DYP = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,YP_NUM])
    
    #Z-axis
    PDA1DZT_INDX_DENS = 0 
    PDA1DZT = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,ZT_NUM])
    
    #2D-YP-ZT
    D2YP_INDEX_TEMP = 0
    D2YP = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,YP_NUM,ZT_NUM])
    
    #2D-XR-YP
    PT2XR_YP_INDEX_TEMP = 0
    PT2XR_YP = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,XR_NUM,YP_NUM])
    
    #2D-XR-ZT
    PT2XR_ZT_INDEX_TEMP = 0
    PT2XR_ZT = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,XR_NUM,ZT_NUM])
    
    #3D-XR
    PT3DXR_INDEX1_TEMP = 0
    PT3DXR = np.zeros([TIME_STP_NUM,ITERATION_NUM,PLS_NUM,XR_NUM,YP_NUM,ZT_NUM])
    
    return PSPC_INDX_DENS,PLASMA_SPC_NAMES_DENS,VPDA,PDA1DXR_INDX_DENS,PDA1DXR,PDA1DYP_INDX_DENS,PDA1DYP,PDA1DZT_INDX_DENS,PDA1DZT,D2YP_INDEX_TEMP,D2YP,PT2XR_YP_INDEX_TEMP,PT2XR_YP,PT2XR_ZT_INDEX_TEMP,PT2XR_ZT,PT3DXR_INDEX1_TEMP,PT3DXR
    




def get_NAMES(PLASMA_SPC_NAMES_DENS,FILE_OUT_LINES,i,ITERATION,TIME_STP,VOL_AVG_DICT):
    '''
    get the names of the background and test particle species 
    '''
    

    
    if (VOL_AVG_DICT >= 0):  ########### ONLY AVG DATA
              
        #-----------------------------------------------------------
        if ((ITERATION == 0) and (TIME_STP == 0)):
        
            PLASMA_SPC_NAMES_DENS.append(FILE_OUT_LINES[i+1][8:].strip())
    
    return PLASMA_SPC_NAMES_DENS


def IZ(PDA1DXR,PDA1DYP,PDA1DZT,PDA1DXR_INDX_DENS,PDA1DYP_INDX_DENS,PDA1DZT_INDX_DENS,TIME_STP,ITERATION,i,FILE_OUT_LINES,PSPC_INDX_TEMP,PT2YP_ZT_INDEX_TEMP,PT2XR_YP_INDEX_TEMP,PT2XR_ZT_INDEX_TEMP,PT3DXR_INDEX1_TEMP):
    '''
    an initial check to see if the output data for a species is just identically zero
    '''
   

    
    FWD_COND_1 = 0
    FWD_IND = 0
        
    if ('IDENTICALLY ZERO' in FILE_OUT_LINES[i+6]):
        
        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,:] = 0.0
        PDA1DYP[TIME_STP,ITERATION,PDA1DYP_INDX_DENS,:] = 0.0
        PDA1DZT[TIME_STP,ITERATION,PDA1DZT_INDX_DENS,:] = 0.0
        FWD_COND_1 = 1
        PSPC_INDX_TEMP    += 1
        PDA1DXR_INDX_DENS += 1
        PDA1DYP_INDX_DENS += 1
        PDA1DZT_INDX_DENS += 1
        PT2YP_ZT_INDEX_TEMP += 1
        PT2XR_YP_INDEX_TEMP +=1
        PT2XR_ZT_INDEX_TEMP +=1
        PT3DXR_INDEX1_TEMP  +=1
    
    
    return PDA1DXR,PDA1DYP,PDA1DZT,FWD_COND_1,PDA1DXR_INDX_DENS,PDA1DYP_INDX_DENS,PDA1DZT_INDX_DENS,TIME_STP,ITERATION,FWD_IND,PSPC_INDX_TEMP,PT2YP_ZT_INDEX_TEMP,PT2XR_YP_INDEX_TEMP,PT2XR_ZT_INDEX_TEMP,PT3DXR_INDEX1_TEMP











def DENS_0D(PSPC_INDX_DENS,PLS_NUM,FILE_OUT_LINES,VPDA,i,TIME_STP,ITERATION,FWD_COND):
    '''
    get the block average data for species
    '''
    
    
    
    if FWD_COND == 0:
    
        FWD_IND = 1
        FWD_COND_0D = 0
        while ((FWD_COND_0D == 0) and (PSPC_INDX_DENS <= (PLS_NUM-1)) and ((i + FWD_IND) < len(FILE_OUT_LINES))) :
            if ('BLOCK AVERAGE' in FILE_OUT_LINES[i+FWD_IND]):
                
                VPDA[TIME_STP,ITERATION,PSPC_INDX_DENS] = float(FILE_OUT_LINES[i+FWD_IND][14:])
                FWD_COND_0D = 1
                PSPC_INDX_DENS +=1
                
            
            FWD_IND += 1
        
    return PSPC_INDX_DENS,VPDA
    

def get_1D(PDA1DXR_INDX_DENS,PLS_NUM,FILE_OUT_LINES,PDA1DXR,i,TIME_STP,ITERATION,FWD_COND,STR_A,STR_B):
    '''
    get the 1D data, average in other two dimensions
    '''

    
    if FWD_COND == 0:
        
        FWD_IND = 1
        FWD_COND_1D = 0
        while ((FWD_COND_1D == 0) and ((i + FWD_IND) < len(FILE_OUT_LINES))) :
            
            if (STR_A in FILE_OUT_LINES[i+FWD_IND]) and (STR_B in FILE_OUT_LINES[i+FWD_IND+1] ):
                
                
                
                while (len(FILE_OUT_LINES[i+2+FWD_IND]) > 1):
                    try:
                        a =  int(FILE_OUT_LINES[i+2+FWD_IND][0:5]) - 1
                        b = float(FILE_OUT_LINES[i+2+FWD_IND][9:20])
                        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a] = b
                    except:
                        #print('HERE 8')
                        pass
                    try:
                        a =  int(FILE_OUT_LINES[i+2+FWD_IND][20:25]) - 1 
                        b = float(FILE_OUT_LINES[i+2+FWD_IND][29:40])
                        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a] = b
                    except:
                        #print('HERE 9')
                        pass
                    try:
                        a =  int(FILE_OUT_LINES[i+2+FWD_IND][40:45]) - 1
                        b = float(FILE_OUT_LINES[i+2+FWD_IND][49:60])
                        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a] = b
                    except:
                        #print('HERE 10')
                        pass
                    try:
                        a =  int(FILE_OUT_LINES[i+2+FWD_IND][60:65]) - 1
                        b = float(FILE_OUT_LINES[i+2+FWD_IND][69:80])
                        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a] = b
                    except:
                        #print('HERE 11')
                        pass
                    try:
                        a =  int(FILE_OUT_LINES[i+2+FWD_IND][80:85]) - 1 
                        b = float(FILE_OUT_LINES[i+2+FWD_IND][89:100])
                        PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a] = b
                    except:
                        #print('HERE 12')
                        pass
                    
                    FWD_IND += 1
                    
                    
                FWD_COND_1D = 1    
                PDA1DXR_INDX_DENS +=1   
                            
            FWD_IND += 1
            
            
            
            
        
        
    
    
    
    
    return PDA1DXR,PDA1DXR_INDX_DENS




def get_2D(FWD_COND,STR_A,STR_B,STR_C,PDA1DXR,FILE_OUT_LINES,i,PDA1DXR_INDX_DENS,TIME_STP,ITERATION,ZT_NUM,PLS_NUM,VOL_AVG_DICT):
    '''
    get 2d data, average in the other dimension
    '''

    
    

    if (FWD_COND) == 0 and (VOL_AVG_DICT >= 2):
        FWD_IND = 1
        FWD_COND_2D = 0
        DUM_IND = 0

        while ((FWD_COND_2D == 0) and ((i + FWD_IND) < len(FILE_OUT_LINES))) :
            
            
            
            if (STR_A in FILE_OUT_LINES[i+FWD_IND]) and (STR_B in FILE_OUT_LINES[i+FWD_IND+1]):
                
                while FWD_COND_2D == 0:
                    
                    
                    
                    
                    
                    if STR_C in FILE_OUT_LINES[i+FWD_IND+3]:
                        
                        
                        #print(FILE_OUT_LINES[i+FWD_IND+3][30:40])
                        DUM_IND = int(FILE_OUT_LINES[i+FWD_IND+3][30:40])
                        
                        
                        while (len(FILE_OUT_LINES[i+4+FWD_IND]) > 1) and (FWD_COND_2D == 0):
                            
                            
                            
                            a =  int(FILE_OUT_LINES[i+4+FWD_IND][0:5]) - 1
                            
                            b = float(FILE_OUT_LINES[i+4+FWD_IND][9:20])
                            
                            PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a,DUM_IND-1] = b
                        
                            try:
                                a =  int(FILE_OUT_LINES[i+4+FWD_IND][20:25]) - 1 
                                b = float(FILE_OUT_LINES[i+4+FWD_IND][29:40])
                                PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a,DUM_IND-1] = b
                            except:
                                #print('HERE 9')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+4+FWD_IND][40:45]) - 1
                                b = float(FILE_OUT_LINES[i+4+FWD_IND][49:60])
                                PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a,DUM_IND-1] = b
                            except:
                                #print('HERE 10')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+4+FWD_IND][60:65]) - 1
                                b = float(FILE_OUT_LINES[i+4+FWD_IND][69:80])
                                PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a,DUM_IND-1] = b
                            except:
                                #print('HERE 11')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+4+FWD_IND][80:85]) - 1 
                                b = float(FILE_OUT_LINES[i+4+FWD_IND][89:100])
                                PDA1DXR[TIME_STP,ITERATION,PDA1DXR_INDX_DENS,a,DUM_IND-1] = b
                            except:
                                #print('HERE 12')
                                pass
                            
                            FWD_IND += 1
                        
                        
                        #print(DUM_IND)
                        if DUM_IND >= ZT_NUM:
                            DUM_IND = 0
                            PDA1DXR_INDX_DENS +=1
                            FWD_COND_2D = 1
                            
                        
                            
                        
                        
                    else:
                        
                        FWD_IND += 1
            
            else:
                    
                FWD_IND +=1
                        
          
    
    return PDA1DXR_INDX_DENS, PDA1DXR



def get_3D(FWD_COND,STR_A,STR_B,STR_C,PT3DXR,FILE_OUT_LINES,PT3DXR_INDEX1_TEMP,TIME_STP,ITERATION,XR_NUM,YP_NUM,ZT_NUM,VOL_AVG_DICT,i):
    '''
    get 3d data, average in the other dimension
    '''
    
    
    if (FWD_COND) == 0 and (VOL_AVG_DICT >= 3):
        FWD_IND = 1
        FWD_COND_2D = 0
        DUM_IND_Z = 0
        DUM_IND_Y = 0

        while ((FWD_COND_2D == 0) and ((i + FWD_IND) < len(FILE_OUT_LINES))) :
            
            
            
            if (STR_A in FILE_OUT_LINES[i+FWD_IND]) and (STR_B in FILE_OUT_LINES[i+FWD_IND+3]):
                
                while FWD_COND_2D == 0:
                    
                    
                    
                    
                    if STR_C in FILE_OUT_LINES[i+FWD_IND+5]:
                        
                        #print(FILE_OUT_LINES[i+FWD_IND+3][30:40])
                        
                        
                        
                        while (len(FILE_OUT_LINES[i+6+FWD_IND]) > 1) and (FWD_COND_2D == 0):
                            
                            
                            
                            a =  int(FILE_OUT_LINES[i+6+FWD_IND][0:5]) - 1
                            b = float(FILE_OUT_LINES[i+6+FWD_IND][9:20])
                            
                            PT3DXR[TIME_STP,ITERATION,PT3DXR_INDEX1_TEMP,a,DUM_IND_Y,DUM_IND_Z] = b
                        
                            try:
                                a =  int(FILE_OUT_LINES[i+6+FWD_IND][20:25]) - 1 
                                b = float(FILE_OUT_LINES[i+6+FWD_IND][29:40])
                                PT3DXR[TIME_STP,ITERATION,PT3DXR_INDEX1_TEMP,a,DUM_IND_Y,DUM_IND_Z] = b
                            except:
                                #print('HERE 9')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+6+FWD_IND][40:45]) - 1
                                b = float(FILE_OUT_LINES[i+6+FWD_IND][49:60])
                                PT3DXR[TIME_STP,ITERATION,PT3DXR_INDEX1_TEMP,a,DUM_IND_Y,DUM_IND_Z] = b
                            except:
                                #print('HERE 10')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+6+FWD_IND][60:65]) - 1
                                b = float(FILE_OUT_LINES[i+6+FWD_IND][69:80])
                                PT3DXR[TIME_STP,ITERATION,PT3DXR_INDEX1_TEMP,a,DUM_IND_Y,DUM_IND_Z] = b
                            except:
                                #print('HERE 11')
                                pass
                            try:
                                a =  int(FILE_OUT_LINES[i+6+FWD_IND][80:85]) - 1 
                                b = float(FILE_OUT_LINES[i+6+FWD_IND][89:100])
                                PT3DXR[TIME_STP,ITERATION,PT3DXR_INDEX1_TEMP,a,DUM_IND_Y,DUM_IND_Z] = b
                            except:
                                #print('HERE 12')
                                pass
                            
                            FWD_IND += 1
                        
                        
                        DUM_IND_Y +=1
                        if DUM_IND_Y >= YP_NUM:
                            DUM_IND_Z += 1
                            DUM_IND_Y = 0
                            if DUM_IND_Z >= ZT_NUM-1:
    
                                PT3DXR_INDEX1_TEMP +=1
                                FWD_COND_2D = 1
                                DUM_IND_Z = 0
                            
                        
                            
                        
                        
                    else:
                        
                        FWD_IND += 1
            
            else:
                    
                FWD_IND +=1
    
    
    
    
    return PT3DXR_INDEX1_TEMP,PT3DXR
    
    

    
    


def build_DA_0D(VOL_AVG_DICT,NP_ARRAY,SPECIES,TIME_STP_NUM,ITERATION_NUM,PLASMA_SPC_NAMES_DENS,long_name_ans,units_ans,data_type,DATASET_DICT,DS_NAME,FILE_NAME):
    '''
    Build an xarray dataset with 3 dimensions for 0D data
    '''
    #----------------------------------
    import xarray as xr
    #----------------------------------
    
    
    #---------------------------------------------------------------------------     
    #construct xarray DataArray for the run for absolute density
    EIR_DA_PDEN = xr.DataArray(NP_ARRAY.copy(),
                               dims = ('TIME_STP','ITERATION',SPECIES),
                               coords = {'TIME_STP' : range(TIME_STP_NUM) ,'ITERATION' : range(ITERATION_NUM) , SPECIES : PLASMA_SPC_NAMES_DENS})     ########## DENSITY DataArray
    #-------------------s--------------------------------------------------------
    #---------------------------------------------------------------------------
    #set the data arrays metadata
    EIR_DA_PDEN.attrs['long_name'] = long_name_ans
    EIR_DA_PDEN.attrs['units']  = units_ans
    EIR_DA_PDEN.attrs['data_tag'] = data_type
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    DATASET_DICT.update({DS_NAME : EIR_DA_PDEN})
    #---------------------------------------------------------------------------
    
    
def build_DA_1D(VOL_AVG_DICT,NP_ARRAY,SPECIES,TIME_STP_NUM,ITERATION_NUM,PLASMA_SPC_NAMES_DENS,long_name_ans,units_ans,data_type,DATASET_DICT,DS_NAME,FILE_NAME,DIRECTION,XR_NUM):
    '''
    Build an xarray dataset with 4 dimensions for 1D data
    '''

    #----------------------------------
    import xarray as xr
    #----------------------------------
    
    
    #---------------------------------------------------------------------------     
    #construct xarray DataArray for the run for absolute density
    EIR_DA_PDEN = xr.DataArray(NP_ARRAY.copy(),
                               dims = ('TIME_STP','ITERATION',SPECIES,DIRECTION),
                               coords = {'TIME_STP' : range(TIME_STP_NUM) ,'ITERATION' : range(ITERATION_NUM) , SPECIES : PLASMA_SPC_NAMES_DENS, DIRECTION : range(XR_NUM)})     ########## DENSITY DataArray
    #-------------------s--------------------------------------------------------
    #---------------------------------------------------------------------------
    #set the data arrays metadata
    EIR_DA_PDEN.attrs['long_name'] = long_name_ans
    EIR_DA_PDEN.attrs['units']  = units_ans
    EIR_DA_PDEN.attrs['data_tag'] = data_type
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    DATASET_DICT.update({DS_NAME : EIR_DA_PDEN})
    #---------------------------------------------------------------------------
    
    
def build_DA_2D(VOL_AVG_DICT,NP_ARRAY,SPECIES,TIME_STP_NUM,ITERATION_NUM,PLASMA_SPC_NAMES_DENS,long_name_ans,units_ans,data_type,DATASET_DICT,DS_NAME,FILE_NAME,DIRECTION_P,DIRECTION_S,XR_NUM,YP_NUM):
    '''
    Build an xarray dataset with 5 dimensions for 2D data
    '''

    #----------------------------------
    import xarray as xr
    #----------------------------------
    
    
    #---------------------------------------------------------------------------     
    #construct xarray DataArray for the run for absolute density
    EIR_DA_PDEN = xr.DataArray(NP_ARRAY.copy(),
                               dims = ('TIME_STP','ITERATION',SPECIES,DIRECTION_P,DIRECTION_S),
                               coords = {'TIME_STP' : range(TIME_STP_NUM) ,'ITERATION' : range(ITERATION_NUM) , SPECIES : PLASMA_SPC_NAMES_DENS, DIRECTION_P : range(XR_NUM),DIRECTION_S : range(YP_NUM)})     ########## DENSITY DataArray
    #-------------------s--------------------------------------------------------
    #---------------------------------------------------------------------------
    #set the data arrays metadata
    EIR_DA_PDEN.attrs['long_name'] = long_name_ans
    EIR_DA_PDEN.attrs['units']  = units_ans
    EIR_DA_PDEN.attrs['data_tag'] = data_type
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    DATASET_DICT.update({DS_NAME : EIR_DA_PDEN})
    #---------------------------------------------------------------------------
    
    
def build_DA_3D(VOL_AVG_DICT,NP_ARRAY,SPECIES,TIME_STP_NUM,ITERATION_NUM,PLASMA_SPC_NAMES_DENS,long_name_ans,units_ans,data_type,DATASET_DICT,DS_NAME,FILE_NAME,DIRECTION_P,DIRECTION_S,DIRECTION_T,XR_NUM,YP_NUM,ZT_NUM):
    '''
    Build an xarray dataset with 6 dimensions for 3D data
    '''

    #----------------------------------
    import xarray as xr
    #----------------------------------
    
    
    #---------------------------------------------------------------------------     
    #construct xarray DataArray for the run for absolute density
    EIR_DA_PDEN = xr.DataArray(NP_ARRAY.copy(),
                               dims = ('TIME_STP','ITERATION',SPECIES,DIRECTION_P,DIRECTION_S,DIRECTION_T),
                               coords = {'TIME_STP' : range(TIME_STP_NUM) ,'ITERATION' : range(ITERATION_NUM) , SPECIES : PLASMA_SPC_NAMES_DENS, DIRECTION_P : range(XR_NUM),DIRECTION_S : range(YP_NUM),DIRECTION_T : range(ZT_NUM)})     ########## DENSITY DataArray
    #-------------------s--------------------------------------------------------
    #---------------------------------------------------------------------------
    #set the data arrays metadata
    EIR_DA_PDEN.attrs['long_name'] = long_name_ans
    EIR_DA_PDEN.attrs['units']  = units_ans
    EIR_DA_PDEN.attrs['data_tag'] = data_type
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    DATASET_DICT.update({DS_NAME : EIR_DA_PDEN})
    #---------------------------------------------------------------------------
    
    
def build_1D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE' ):
    '''
    build 2D plot for 1D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
        
        
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,PLS_SPECIES = list(DS.PLS_SPECIES.data).index(SPC)).data
    data_xr = data_xr * np.ones((len(th)-1,len(r)-1))
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,PLS_SPECIES = list(DS.PLS_SPECIES.data).index(SPC)).data
    data_zt = data_zt * np.ones((len(r)-1,len(z)-1))
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    rm,thm = np.meshgrid(r,th)
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('1D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)    
    ax1.plot(x0,y0,'k')

    ###############################
        
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('1D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_1D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'  ):
    '''
    build 2D plot for 1D atom data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ATM_SPECIES = list(DS.ATM_SPECIES.data).index(SPC)).data
    data_xr = data_xr * np.ones((len(th)-1,len(r)-1))
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ATM_SPECIES = list(DS.ATM_SPECIES.data).index(SPC)).data
    data_zt = data_zt * np.ones((len(r)-1,len(z)-1))
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    rm,thm = np.meshgrid(r,th)
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('1D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)    
    ax1.plot(x0,y0,'k')

    ###############################
        
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('1D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 

def build_1D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'  ):
    '''
    build 2D plot for 1D mol data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,MOL_SPECIES = list(DS.MOL_SPECIES.data).index(SPC)).data
    data_xr = data_xr * np.ones((len(th)-1,len(r)-1))
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,MOL_SPECIES = list(DS.MOL_SPECIES.data).index(SPC)).data
    data_zt = data_zt * np.ones((len(r)-1,len(z)-1))
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    rm,thm = np.meshgrid(r,th)
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('1D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)    
    ax1.plot(x0,y0,'k')

    ###############################
        
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('1D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_1D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'  ):
    '''
    build 2D plot for 1D ion data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ION_SPECIES = list(DS.ION_SPECIES.data).index(SPC)).data
    data_xr = data_xr * np.ones((len(th)-1,len(r)-1))
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ION_SPECIES = list(DS.ION_SPECIES.data).index(SPC)).data
    data_zt = data_zt * np.ones((len(r)-1,len(z)-1))
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    rm,thm = np.meshgrid(r,th)
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('1D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)    
    ax1.plot(x0,y0,'k')

    ###############################
        
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('1D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_2D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,PLS_SPECIES = list(DS.PLS_SPECIES.data).index(SPC)).data
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,PLS_SPECIES = list(DS.PLS_SPECIES.data).index(SPC)).data
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('2D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('2D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_2D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D atom data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ATM_SPECIES = list(DS.ATM_SPECIES.data).index(SPC)).data
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ATM_SPECIES = list(DS.ATM_SPECIES.data).index(SPC)).data
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('2D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('2D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_2D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D molecule data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,MOL_SPECIES = list(DS.MOL_SPECIES.data).index(SPC)).data
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,MOL_SPECIES = list(DS.MOL_SPECIES.data).index(SPC)).data
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('2D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('2D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 

    
    









def build_2D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D ion data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ION_SPECIES = list(DS.ION_SPECIES.data).index(SPC)).data
    
    data_zt = DS_TYPE_2.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ION_SPECIES = list(DS.ION_SPECIES.data).index(SPC)).data
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('2D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    ############################### 
    fig2,ax2 = plt.subplots()

    zm,rm = np.meshgrid(z,r)
    zmf,rmf = np.meshgrid(z,-r)
    ax2.pcolormesh(zmf,rmf,data_zt,cmap=cm.plasma)
    
    plot_2 = ax2.pcolormesh(zm,rm,data_zt,cmap=cm.plasma)
    ax2.set_xlim(0-(z.max()*.01),(z.max()*1.01))
    ax2.set_ylim(0-(r.max()*1.50),(r.max()*1.50))
    ax2.set_aspect(5)
    ax2.set_title('1D ' + DS_TYPE_2.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_2.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i' % ITERATIONIN)
    ax2.set_xlabel('cm')
    ax2.set_ylabel('cm')
    fig2.colorbar(plot_2)
    
    ax2.hlines(r.max(),z.min(),z.max())
    ax2.hlines(-r.max(),z.min(),z.max())
    ax2.vlines(z.min(),-r.max(),r.max())
    ax2.vlines(z.max(),-r.max(),r.max())
    ###############################
    
    return fig1,fig2 


def build_3D_PLS_PLOT(DS,DS_TYPE_1,SPC,Z_SEC = 20,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry

    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
   ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,PLS_SPECIES = list(DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = Z_SEC).data
    
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('3D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i ' % ITERATIONIN + 'Z: %i' % Z_SEC )
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    
    
    return fig1

def build_3D_ATM_PLOT(DS,DS_TYPE_1,SPC,Z_SEC = 20,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ATM_SPECIES = list(DS.ATM_SPECIES.data).index(SPC),ZT_POSITION = Z_SEC).data
    
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('3D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i ' % ITERATIONIN + 'Z: %i' % Z_SEC )
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    
    
    return fig1



def build_3D_MOL_PLOT(DS,DS_TYPE_1,SPC,Z_SEC = 20,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,MOL_SPECIES = list(DS.MOL_SPECIES.data).index(SPC),ZT_POSITION = Z_SEC).data
    
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('3D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i ' % ITERATIONIN + 'Z: %i' % Z_SEC )
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    
    
    return fig1



def build_3D_ION_PLOT(DS,DS_TYPE_1,SPC,Z_SEC = 20,ITERATIONIN = 'NONE',TIME_STPIN = 'NONE'):
    '''
    build 2D plot for 2D plasma data with cylindrical geometry
    '''
    #----------------------------------
    import numpy as  np 
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import eirenex.geometry
    #----------------------------------
    
    if ITERATIONIN == 'NONE':
        
        ITERATIONIN = DS.ITERATION.data.max()
        
    if TIME_STPIN == 'NONE':
        
        TIME_STPIN = DS.TIME_STP.data.max()
    
    
    plt.cla()
    plt.clf()
    
    ##############################
    r,th,z = eirenex.geometry.bessel_cyl()
    ##############################
    
    ##############################
    
    r0 = r.max()
    th0  = np.linspace(0,2*np.pi,100)
    x0 = r0*np.cos(th0)
    y0 = r0*np.sin(th0)
    ##############################
    
    ##############################
    data_xr = DS_TYPE_1.isel(TIME_STP = TIME_STPIN,ITERATION = ITERATIONIN,ION_SPECIES = list(DS.ION_SPECIES.data).index(SPC),ZT_POSITION = Z_SEC).data
    
    ###############################
    
    ###############################
    fig1,ax1 = plt.subplots()
    
    thm,rm = np.meshgrid(th,r)
    
    x = rm*np.cos(thm)
    y = rm*np.sin(thm)
    
    plot_1 = ax1.pcolormesh(x,y,data_xr,cmap=cm.plasma)
    ax1.set_aspect('equal')
    ax1.set_title('3D ' + DS_TYPE_1.attrs['data_tag'] + ': %s ' % SPC+ DS_TYPE_1.attrs['units'] + ' TS: %i ' % TIME_STPIN + 'IT: %i ' % ITERATIONIN + 'Z: %i' % Z_SEC )
    ax1.set_xlabel('cm')
    ax1.set_ylabel('cm')
    fig1.colorbar(plot_1)
    ax1.plot(x0,y0,'k')
        
    ###############################
     
    
    
    return fig1





















def build_ITERATION_PLS_1D_TEMP(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_1D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_PLS_TEMP_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_PLS_TEMP_IT.gif',R_PLOTS,fps = 3)
    
def build_ITERATION_PLS_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_1D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_PLS_DENS_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_PLS_DENS_IT.gif',R_PLOTS,fps = 3)
    
def build_ITERATION_ATM_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_1D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_ATM_DENS_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_ATM_DENS_IT.gif',R_PLOTS,fps = 3)
    
def build_ITERATION_MOL_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_1D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_MOL_DENS_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_MOL_DENS_IT.gif',R_PLOTS,fps = 3)

def build_ITERATION_ION_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_1D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_ION_DENS_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_ION_DENS_IT.gif',R_PLOTS,fps = 3)






def build_TIME_STP_PLS_1D_TEMP(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_1D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_PLS_TEMP_TS.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_PLS_TEMP_TS.gif',R_PLOTS,fps = 3)
    
def build_TIME_STP_PLS_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_1D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_PLS_DENS_TS.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_PLS_DENS_TS.gif',R_PLOTS,fps = 3)

def build_TIME_STP_ATM_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_1D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_ATM_DENS_TS.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_ATM_DENS_TS.gif',R_PLOTS,fps = 3)
    
def build_TIME_STP_MOL_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_1D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_MOL_DENS_TS.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_MOL_DENS_TS.gif',R_PLOTS,fps = 3)
    
def build_TIME_STP_ION_1D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    '''
    Build gif
    '''
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_1D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_Z_AVG_ION_DENS_TS.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_R_AVG_ION_DENS_TS.gif',R_PLOTS,fps = 3)




























def build_ITERATION_PLS_2D_TEMP(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_2D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_PLS_TEMP_IT.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_PLS_TEMP_IT.gif',Z_PLOTS,fps = 3)

def build_ITERATION_PLS_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_2D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_PLS_DENS_IT.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_PLS_DENS_IT.gif',Z_PLOTS,fps = 3)
    
def build_ITERATION_ATM_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_2D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_ATM_DENS_IT.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_ATM_DENS_IT.gif',Z_PLOTS,fps = 3)
    
def build_ITERATION_MOL_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_2D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_MOL_DENS_IT.gif',Z_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_MOL_DENS_IT.gif',R_PLOTS,fps = 3)

def build_ITERATION_ION_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.ITERATION.data)):
                
        R_FIG,Z_FIG = build_2D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_ION_DENS_IT.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_ION_DENS_IT.gif',Z_PLOTS,fps = 3)






def build_TIME_STP_PLS_2D_TEMP(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_2D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_PLS_TEMP_TS.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_PLS_TEMP_TS.gif',Z_PLOTS,fps = 3)
    
def build_TIME_STP_PLS_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_2D_PLS_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_PLS_DENS_TS.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_PLS_DENS_TS.gif',Z_PLOTS,fps = 3)

def build_TIME_STP_ATM_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_2D_ATM_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_ATM_DENS_TS.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_ATM_DENS_TS.gif',Z_PLOTS,fps = 3)
    
def build_TIME_STP_MOL_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_2D_MOL_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
        
    imageio.mimsave('EIRX_XR_YP_MOL_DENS_TS.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_ZT_MOL_DENS_TS.gif',Z_PLOTS,fps = 3)
    
def build_TIME_STP_ION_2D_DENS(DS,DS_TYPE_1,DS_TYPE_2,SPC):
    
    #----------------------------------
    import os
    import imageio
    #----------------------------------
    
    R_PLOTS = []
    Z_PLOTS = []
    
    for i in range(len(DS.TIME_STP.data)):
                
        R_FIG,Z_FIG = build_2D_ION_PLOT(DS,DS_TYPE_1,DS_TYPE_2,SPC,'NONE',i)
        R_FIG.savefig('R%i.png' % i)
        Z_FIG.savefig('Z%i.png' % i)
        
        R_PLOTS.append(imageio.imread('R%i.png' %i))
        Z_PLOTS.append(imageio.imread('Z%i.png' %i))
        
        os.remove('R%i.png' % i)
        os.remove('Z%i.png' % i)

        R_FIG.clf()
        Z_FIG.clf()
    imageio.mimsave('EIRX_XR_ZT_ION_DENS_TS.gif',R_PLOTS,fps = 3)
    imageio.mimsave('EIRX_XR_YP_ION_DENS_TS.gif',Z_PLOTS,fps = 3)
    
    
    
    
    
    
###########################################################################
###########################################################################
###########################################################################
#Newer plotting scripts
###########################################################################
###########################################################################
###########################################################################
    
    

    
def general_2D_plot(data,geom_DS,x_label,y_label,color_bar_label,SPC,units,TIME_STPIN,ITERATIONIN,Z_SEC):
    
    #----------------------------------
    import matplotlib.pyplot as plt
    from matplotlib import cm
    import matplotlib
    #----------------------------------
    
    #Create and label plot
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    data_max = data.max()
    if data_max < .001:
        data_max = .01
    data_min = data.min()
    if data_min < .001:
        data_min = .001
    
    
    norm_obj = matplotlib.colors.LogNorm(vmin =data_min ,vmax= data_max)
    cmap_obj = cm.get_cmap('plasma')
    fig1.colorbar(cm.ScalarMappable(norm=norm_obj,cmap = cmap_obj)).set_label(color_bar_label)
    ax1.set_title('%s ' % SPC + units + ' TS: %i ' % TIME_STPIN + 'IT: %i ' % ITERATIONIN + 'Z: %i' % Z_SEC )
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    ax1.set_aspect('equal')
    
    
    #Plot Vessel, Limiter, and Plasma
    ax1.plot(geom_DS.Vessel.data[0],geom_DS.Vessel.data[1],'k-')
    ax1.plot(geom_DS.Limiter.data[0],geom_DS.Limiter.data[1],'k-')
    
    polygon_list = geom_DS.Polygons.data
    
    for i in range(len(polygon_list)):
    
        x = []
        y = []
    
        for j in range(len(polygon_list[i])):
            
            x.append(polygon_list[i][j][0])
            y.append(polygon_list[i][j][1])
        
        ax1.fill(x,y,color=cmap_obj(norm_obj(data.reshape(len(polygon_list))[i])))
        
        
    return ax1,fig1



def FT_get_species(FILE_READLINES,FT_ATM_SPECIES):
    
    for i in range(len(FILE_READLINES)): 
        
        if 'PARTICLE DENSITY (ATOMS)' in FILE_READLINES[i]:
            
            FT_SPC_NAME = FILE_READLINES[i+1].strip()
            
            if FT_SPC_NAME not in FT_ATM_SPECIES:
            
                FT_ATM_SPECIES.append(FT_SPC_NAME)
                
                
                
    return FT_ATM_SPECIES


def FT_build_array(ATM_NUM,ZT_NUM,YP_NUM,XR_NUM,ITERATION_NUM,TIME_STP_NUM):
    
    #----------------------------------
    import numpy as np
    #----------------------------------
    
    ft_array = np.zeros((ATM_NUM,ZT_NUM+1,YP_NUM+1,XR_NUM+1,ITERATION_NUM,TIME_STP_NUM))
    
    
    return ft_array


def FT_get_data(ATM_DENS_FT_DATA_LINES,FT_ATM_DENS_ARRAY,DATA_TYPE_STRING,ITERATION_NUM,ZT_NUM,YP_NUM,XR_NUM,ATOM_SPC_NAMES_DENS,TIME_STP_NUM):
    
    #----------------------------------
    import numpy as np
    #----------------------------------
    
    
    FT_ITER_NUM    = 0
    FT_TMSTP_NUM   = 0 
    FT_SPECIES_IND = 0
    
    
    for i in range(len(ATM_DENS_FT_DATA_LINES)): 
        
        if DATA_TYPE_STRING in ATM_DENS_FT_DATA_LINES[i]:
            
            

            
            FT_SPC_NAME = ATM_DENS_FT_DATA_LINES[i+1].strip()
            
            
            LOOP_COND_1 = 0
            
            
            
            while LOOP_COND_1 == 0:
                
                
                if FT_SPECIES_IND == len(ATOM_SPC_NAMES_DENS):
                    
                    FT_SPECIES_IND = 0
                    FT_ITER_NUM += 1
                    
                    
                    if FT_ITER_NUM == ITERATION_NUM:
                        
                        FT_ITER_NUM = 0
                        FT_TMSTP_NUM +=1
                        
                    else:
                        
                        pass
                    
                    
                if FT_SPC_NAME == ATOM_SPC_NAMES_DENS[FT_SPECIES_IND]:
                    
                    
                    LOOP_COND_1 = 1
                    
                    
                else:
                    
                    FT_SPECIES_IND += 1
                    
                
            
            FT_FWD_IND = 0
            DATA_1D_RAW = []
            DATA_1D_CLEAN = []
            while '==============' not in ATM_DENS_FT_DATA_LINES[i+6 + FT_FWD_IND]:
                
                for j in ATM_DENS_FT_DATA_LINES[i+6 + FT_FWD_IND].strip().split(' '):
                
                    DATA_1D_RAW.append(j)
                    
                FT_FWD_IND +=1
                
            for j in DATA_1D_RAW:
                
                if j != '':
                    
                    DATA_1D_CLEAN.append(j)
                    
                
                    
            data_array = np.array(DATA_1D_CLEAN).reshape(ZT_NUM+1,YP_NUM+1,XR_NUM+1)
            
            
            
            for j in range(ZT_NUM+1):
                
                for k in range(YP_NUM+1):
                    
                    for l in range(XR_NUM+1):
                        
                        FT_ATM_DENS_ARRAY[FT_SPECIES_IND,j,k,l,FT_ITER_NUM,FT_TMSTP_NUM] = data_array[j,k,l]
                        
            FT_SPECIES_IND +=1
                        
    return FT_ATM_DENS_ARRAY
                        

def FT_build_DA(FT_ATM_DENS_ARRAY,SPC_TYPE,DS_NAME,UNITS,long_name,FT_ATM_SPECIES,ZT_NUM,YP_NUM,XR_NUM,ITERATION_NUM,TIME_STP_NUM,DATASET_DICT):
    
    #----------------------------------
    import xarray as xr
    #----------------------------------
    
    FT_DA = xr.DataArray(FT_ATM_DENS_ARRAY.copy(),
                           dims = (SPC_TYPE,'ZT_POSITION','YP_POSITION','XR_POSITION','ITERATION','TIME_STP'),
                           coords = {SPC_TYPE : FT_ATM_SPECIES,'ZT_POSITION' : range(ZT_NUM+1),'YP_POSITION' : range(YP_NUM+1),'XR_POSITION' : range(XR_NUM+1),'ITERATION' : range(ITERATION_NUM),'TIME_STP' : range(TIME_STP_NUM)})
    
    
    FT_DA.attrs['long_name'] = long_name
    FT_DA.attrs['units']  = UNITS
    
    
    DATASET_DICT.update({ DS_NAME: FT_DA})
    
    return FT_DA,DATASET_DICT
                        


def build_polygons(eirene_vert,eirene_poly,poly_num):
    
    #----------------------------------
    import numpy as np
    #----------------------------------
    
    polys = []
    
    #Sort vertices according ot the polygons they belong to
    for i in range(poly_num):
        
        shapes = []
        
        for j in range(len(eirene_poly)):
            
            if (i+1) in eirene_poly[j]:
                
                shapes.append((eirene_vert[0][j],eirene_vert[1][j]))
            
        polys.append(shapes)
        
    poly_sorted = []
    
    #Sort the ordering of the polygon vertex coordinates clockwise
    #with respect to the vertex closest to the x-axis
    for i in range(len(polys)):
        
        tri_tup = []
        fin_tup = []
        polys[i].sort()
        start_point = polys[i][0]
        
        fin_tup.append((start_point[0],start_point[1],0))
        
        for j in range(len(polys[i])-1):
            
            x = polys[i][j+1][0] - start_point[0]
            y = polys[i][j+1][1] - start_point[1]
            th = np.arctan(y/x)
            
            tri_tup.append((polys[i][j+1][0],polys[i][j+1][1],th))
            
        tri_tup.sort(key=lambda tup: tup[2])
        
        for i in tri_tup:
            
            fin_tup.append(i)
        
        poly_sorted.append(fin_tup)
        
    return  poly_sorted

                        
                        
    






















