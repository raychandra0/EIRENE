#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:14:42 2019

@author: nathanbartlett
"""

def pls_temp_3D_poloidal_view(data_DS,geom_DS,SPC,ZT_SEC = 0,ITERATION_='NONE',TIME_STP_='NONE'):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------

    #Get data to be plotted
    if ITERATION_ == 'NONE':
        
        ITERATION_ = data_DS.ITERATION.data.min()
        
    if TIME_STP_ == 'NONE':
        
        TIME_STP_ = data_DS.TIME_STP.data.min()
    
    #Get the shape to pull non-average data from arrays
    bound1 =data_DS.FT_PLS_TEMP.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[0]
    bound2 =data_DS.FT_PLS_TEMP.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[1]

    #Get atm data
    data = data_DS.FT_PLS_TEMP.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data[:bound1-1,:bound2-1]
    
    ax1,fig1 = IC.general_2D_plot(data, geom_DS,'[M]','[M]','Density : cm-3',SPC,'cm-3',TIME_STP_,ITERATION_,ZT_SEC)
    
    return fig1

def pls_dens_3D_poloidal_view(data_DS,geom_DS,SPC,ZT_SEC = 0,ITERATION_='NONE',TIME_STP_='NONE'):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------

    #Get data to be plotted
    if ITERATION_ == 'NONE':
        
        ITERATION_ = data_DS.ITERATION.data.min()
        
    if TIME_STP_ == 'NONE':
        
        TIME_STP_ = data_DS.TIME_STP.data.min()
    
    #Get the shape to pull non-average data from arrays
    bound1 =data_DS.FT_PLS_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[0]
    bound2 =data_DS.FT_PLS_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[1]

    #Get atm data
    data = data_DS.FT_PLS_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,PLS_SPECIES = list(data_DS.PLS_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data[:bound1-1,:bound2-1]
    
    ax1,fig1 = IC.general_2D_plot(data, geom_DS,'[M]','[M]','Density : cm-3',SPC,'cm-3',TIME_STP_,ITERATION_,ZT_SEC)
    
    return fig1

def atm_dens_3D_poloidal_view(data_DS,geom_DS,SPC,ZT_SEC = 0,ITERATION_='NONE',TIME_STP_='NONE'):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------

    #Get data to be plotted
    if ITERATION_ == 'NONE':
        
        ITERATION_ = data_DS.ITERATION.data.min()
        
    if TIME_STP_ == 'NONE':
        
        TIME_STP_ = data_DS.TIME_STP.data.min()
    
    #Get the shape to pull non-average data from arrays
    bound1 =data_DS.FT_ATM_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ATM_SPECIES = list(data_DS.ATM_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[0]
    bound2 =data_DS.FT_ATM_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ATM_SPECIES = list(data_DS.ATM_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[1]

    #Get atm data
    data = data_DS.FT_ATM_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ATM_SPECIES = list(data_DS.ATM_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data[:bound1-1,:bound2-1]
    
    ax1,fig1 = IC.general_2D_plot(data, geom_DS,'[M]','[M]','Density : cm-3',SPC,'cm-3',TIME_STP_,ITERATION_,ZT_SEC)
    
    return fig1


def mol_dens_3D_poloidal_view(data_DS,geom_DS,SPC,ZT_SEC = 0,ITERATION_='NONE',TIME_STP_='NONE'):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------

    #Get data to be plotted
    if ITERATION_ == 'NONE':
        
        ITERATION_ = data_DS.ITERATION.data.min()
        
    if TIME_STP_ == 'NONE':
        
        TIME_STP_ = data_DS.TIME_STP.data.min()
    
    #Get the shape to pull non-average data from arrays
    bound1 =data_DS.FT_MOL_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,MOL_SPECIES = list(data_DS.MOL_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[0]
    bound2 =data_DS.FT_MOL_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,MOL_SPECIES = list(data_DS.MOL_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[1]

    #Get mol data
    data = data_DS.FT_MOL_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,MOL_SPECIES = list(data_DS.MOL_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data[:bound1-1,:bound2-1]
    
    ax1,fig1 = IC.general_2D_plot(data, geom_DS,'[M]','[M]','Density : cm-3',SPC,'cm-3',TIME_STP_,ITERATION_,ZT_SEC)
    
    return fig1

def ion_dens_3D_poloidal_view(data_DS,geom_DS,SPC,ZT_SEC = 0,ITERATION_='NONE',TIME_STP_='NONE'):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------

    #Get data to be plotted
    if ITERATION_ == 'NONE':
        
        ITERATION_ = data_DS.ITERATION.data.min()
        
    if TIME_STP_ == 'NONE':
        
        TIME_STP_ = data_DS.TIME_STP.data.min()
    
    #Get the shape to pull non-average data from arrays
    bound1 =data_DS.FT_ION_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ION_SPECIES = list(data_DS.ION_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[0]
    bound2 =data_DS.FT_ION_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ION_SPECIES = list(data_DS.ION_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data.shape[1]

    #Get ion data
    data = data_DS.FT_ION_DENS.isel(TIME_STP = TIME_STP_,ITERATION = ITERATION_,ION_SPECIES = list(data_DS.ION_SPECIES.data).index(SPC),ZT_POSITION = ZT_SEC).data[:bound1-1,:bound2-1]
    
    ax1,fig1 = IC.general_2D_plot(data, geom_DS,'[M]','[M]','Density : cm-3',SPC,'cm-3',TIME_STP_,ITERATION_,ZT_SEC)
    
    return fig1


    
    
























##########################################################################
##########################################################################
##########################################################################
#            End of New and Begining of Old Plotting Routines
##########################################################################
##########################################################################
##########################################################################
    




def avg_t_pls(DS):
    '''
    Plot block average plasma temperature across time steps
    '''
    
    DS.PLS_BLA_TEMP.isel(ITERATION = DS.ITERATION.data.size-1).plot.line(x = 'TIME_STP')
    
    
def avg_d_pls(DS):
    '''
    Plot block average plasma density across time steps
    '''
    
    DS.PLS_BLA_DENS.isel(ITERATION = DS.ITERATION.data.size-1).plot.line(x = 'TIME_STP')


def avg_d_atm(DS):
    '''
    Plot block average atom density across time steps
    '''
    
    DS.ATOM_BLA_DENS.isel(ITERATION = DS.ITERATION.data.size-1).plot.line(x = 'TIME_STP')

def avg_d_mol(DS):
    '''
    Plot block average molecule density across time steps
    '''
    
    DS.MOL_BLA_DENS.isel(ITERATION = DS.ITERATION.data.size-1).plot.line(x = 'TIME_STP')

def avg_d_ion(DS):
    '''
    Plot block average test ion density across time steps
    '''
    
    DS.ION_BLA_DENS.isel(ITERATION = DS.ITERATION.data.size-1).plot.line(x = 'TIME_STP')



def cyl_1d_t_pls(DS,SPC,ITERATIONIN = 'NONE'):
    '''
    Plot 1D plasma temperature on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    fig1,fig2 = IC.build_1D_PLS_PLOT(DS,DS.PLS_XR_TEMP,DS.PLS_ZT_TEMP,SPC,ITERATIONIN)
    
    
    
    return fig1,fig2 


def cyl_1d_d_pls(DS,SPC):
    '''
    Plot 1D plasma density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_1D_PLS_PLOT(DS,DS.PLS_XR_DENS,DS.PLS_ZT_DENS,SPC)

    
    
    
    return fig1,fig2 

def cyl_1d_d_atm(DS,SPC):
    '''
    Plot 1D atom density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_1D_ATM_PLOT(DS,DS.ATM_XR_DENS,DS.ATM_ZT_DENS,SPC)
    
    
    
    return fig1,fig2

def cyl_1d_d_mol(DS,SPC):
    '''
    Plot 1D molecule density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_1D_MOL_PLOT(DS,DS.MOL_XR_DENS,DS.MOL_ZT_DENS,SPC)
    
    
    return fig1,fig2
    
def cyl_1d_d_ion(DS,SPC):
    '''
    Plot 1D test ion density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_1D_ION_PLOT(DS,DS.ION_XR_DENS,DS.ION_ZT_DENS,SPC)
    
    
    
    return fig1,fig2 
    




def cyl_2d_t_pls(DS,SPC):
    '''
    Plot 2D plasma temperature on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_2D_PLS_PLOT(DS,DS.PLS_XR_YP_TEMP_2D,DS.PLS_XR_ZT_TEMP_2D,SPC)
    
    
    
    return fig1,fig2
    

def cyl_2d_d_pls(DS,SPC):
    '''
    Plot 2D plasma density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_2D_PLS_PLOT(DS,DS.PLS_XR_YP_DENS_2D,DS.PLS_XR_ZT_DENS_2D,SPC)
    
    
    
    return fig1,fig2

def cyl_2d_d_atm(DS,SPC):
    '''
    Plot 2D atom density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1,fig2 = IC.build_2D_ATM_PLOT(DS,DS.ATM_XR_YP_DENS_2D,DS.ATM_XR_ZT_DENS_2D,SPC)

    
    
    
    return fig1,fig2
    
def cyl_2d_d_mol(DS,SPC):
    '''
    Plot 2D molecule density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    fig1,fig2 = IC.build_2D_MOL_PLOT(DS,DS.MOL_XR_YP_DENS_2D,DS.MOL_XR_ZT_DENS_2D,SPC)
    
    
    
    return fig1,fig2
    


def cyl_2d_d_ion(DS,SPC):
    '''
    Plot 2D test ion density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    fig1,fig2 = IC.build_2D_ION_PLOT(DS,DS.ION_XR_YP_DENS_2D,DS.ION_XR_ZT_DENS_2D,SPC)
    
   
    return fig1,fig2





def cyl_3d_t_pls(DS,SPC,Z_SEC = 20):
    '''
    Plot 3D plasma temperature on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1 = IC.build_3D_PLS_PLOT(DS,DS.PLS_XR_TEMP_3D,SPC,Z_SEC,)
    
    
    
    return fig1
    

def cyl_3d_d_pls(DS,SPC,Z_SEC=20):
    '''
    Plot 3D plasma density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1 = IC.build_3D_PLS_PLOT(DS,DS.PLS_XR_DENS_3D,SPC,Z_SEC)
    
    
    
    return fig1

def cyl_3d_d_atm(DS,SPC,Z_SEC=20):
    '''
    Plot 3D atom density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    fig1 = IC.build_3D_ATM_PLOT(DS,DS.ATM_XR_DENS_3D,SPC,Z_SEC,0,0)

    
    
    
    return fig1
    
def cyl_3d_d_mol(DS,SPC,Z_SEC=20):
    '''
    Plot 3D molecule density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    fig1 = IC.build_3D_MOL_PLOT(DS,DS.MOL_XR_DENS_3D,SPC,Z_SEC)
    
    
    
    return fig1
    


def cyl_3d_d_ion(DS,SPC,Z_SEC=20):
    '''
    Plot 3D test ion density on cylindrical geometry
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    fig1 = IC.build_3D_ION_PLOT(DS,DS.ION_XR_DENS_3D,SPC,Z_SEC)
    
   
    return fig1






















def gif_ITERATION_PLS_1D_TEMP(DS,SPC):
    '''
    make gif
    '''
   #----------------------------------
    import eirenex.intern as IC
   #----------------------------------
    
    IC.build_ITERATION_PLS_1D_TEMP(DS,DS.PLS_XR_TEMP,DS.PLS_ZT_TEMP,SPC)
    
def gif_ITERATION_PLS_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_PLS_1D_DENS(DS,DS.PLS_XR_DENS,DS.PLS_ZT_DENS,SPC)
    
def gif_ITERATION_ATM_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_ATM_1D_DENS(DS,DS.ATM_XR_DENS,DS.ATM_ZT_DENS,SPC)
    
def gif_ITERATION_MOL_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_MOL_1D_DENS(DS,DS.MOL_XR_DENS,DS.MOL_ZT_DENS,SPC)
    
def gif_ITERATION_ION_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_ION_1D_DENS(DS,DS.ION_XR_DENS,DS.ION_ZT_DENS,SPC)
    
    
    
    
    
    
    
    
    
    

def gif_TIME_STP_PLS_1D_TEMP(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_PLS_1D_TEMP(DS,DS.PLS_XR_TEMP,DS.PLS_ZT_TEMP,SPC)
    
    
def gif_TIME_STP_PLS_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_PLS_1D_DENS(DS,DS.PLS_XR_DENS,DS.PLS_ZT_DENS,SPC)
    
def gif_TIME_STP_ATM_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_ATM_1D_DENS(DS,DS.ATM_XR_DENS,DS.ATM_ZT_DENS,SPC)
    
def gif_TIME_STP_MOL_1D_DENS(DS,SPC):
    '''
    make gif
    '''
   #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_MOL_1D_DENS(DS,DS.MOL_XR_DENS,DS.MOL_ZT_DENS,SPC)
    
def gif_TIME_STP_ION_1D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_ION_1D_DENS(DS,DS.ION_XR_DENS,DS.ION_ZT_DENS,SPC)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def gif_ITERATION_PLS_2D_TEMP(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_PLS_2D_TEMP(DS,DS.PLS_XR_YP_TEMP_2D,DS.PLS_XR_ZT_TEMP_2D,SPC)
    
def gif_ITERATION_PLS_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_PLS_2D_DENS(DS,DS.PLS_XR_YP_DENS_2D,DS.PLS_XR_ZT_DENS_2D,SPC)
    
def gif_ITERATION_ATM_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_ATM_2D_DENS(DS,DS.ATM_XR_YP_DENS_2D,DS.ATM_XR_ZT_DENS_2D,SPC)
    
def gif_ITERATION_MOL_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_MOL_2D_DENS(DS,DS.MOL_XR_YP_DENS_2D,DS.MOL_XR_ZT_DENS_2D,SPC)
    
def gif_ITERATION_ION_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_ITERATION_ION_2D_DENS(DS,DS.ION_XR_YP_DENS_2D,DS.ION_XR_ZT_DENS_2D,SPC)
    











def gif_TIME_STP_PLS_2D_TEMP(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_PLS_2D_TEMP(DS,DS.PLS_XR_YP_TEMP_2D,DS.PLS_XR_ZT_TEMP_2D,SPC)
    
    
def gif_TIME_STP_PLS_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_PLS_2D_DENS(DS,DS.PLS_XR_YP_DENS_2D,DS.PLS_XR_ZT_DENS_2D,SPC)
    
def gif_TIME_STP_ATM_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_ATM_2D_DENS(DS,DS.ATM_XR_YP_DENS_2D,DS.ATM_XR_ZT_DENS_2D,SPC)
    
def gif_TIME_STP_MOL_2D_DENS(DS,SPC):
    
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_MOL_2D_DENS(DS,DS.MOL_XR_YP_DENS_2D,DS.MOL_XR_ZT_DENS_2D,SPC)
    
def gif_TIME_STP_ION_2D_DENS(DS,SPC):
    '''
    make gif
    '''
    #----------------------------------
    import eirenex.intern as IC
    #----------------------------------
    
    IC.build_TIME_STP_ION_2D_DENS(DS,DS.ION_XR_YP_DENS_2D,DS.ION_XR_ZT_DENS_2D,SPC)

        
        
        


        
        
        
        
    
    



    



