#----------------------
import eirenex 
import numpy as np
#----------------------

DS = eirenex.data.run('examples/cylinder/test_2D_raw/test_2D.in','examples/cylinder/test_2D_raw/test_2D.out')
DS3 = eirenex.data.run('examples/cylinder/test_3D_raw/TEST_3D.in','examples/cylinder/test_3D_raw/TEST_3D.out')
DS_fort = eirenex.data.run('examples/cylinder/test_fort/input.dat','examples/cylinder/test_fort/run.log','examples/cylinder/test_fort/fort.90','examples/cylinder/test_fort/fort.91','examples/cylinder/test_fort/fort.92','examples/cylinder/test_fort/fort.93','examples/cylinder/test_fort/fort.94')
    
class TestRuninput:
    '''
    Check reading of input data and metadata of the run
    '''
    
    def test_meta_despription(self):
        
        assert ('EIRENE' in DS.attrs['INFO'])
        
    def test_date(self):
        
        assert ('30 12 2019\n' in DS.attrs['DATE'])
        
    def test_time(self):
        
        assert ('15 41 10\n' in DS.attrs['TIME'])
        
    def test_atm_species_num(self):
        '''
        Check the number of atom species read from the input file
        '''
        assert DS.ATM_SPECIES.size == 6
        
    def test_ion_species_num(self):
        '''
        Check the number of test ion species read from the input file
        '''
        assert DS.ION_SPECIES.size == 8
        
    def test_mol_species_num(self):
        '''
        Check the number of mol species read from the input file
        '''
        assert DS.MOL_SPECIES.size == 6
        
    def test_pls_species_num(self):
        '''
        Check the number of plasma species read from the input file
        '''
        assert DS.PLS_SPECIES.size == 111
        
    def test_time_stp_num(self):
        '''
        Check the number of time steps read from the input file
        '''
        assert DS.TIME_STP.size == 5
        
    def test_iter_num(self):
        '''
        Check the number of iterations read from the input file
        '''
        assert DS.ITERATION.size == 3
        
    def test_xr_num(self):
        '''
        Check the number of XR positions read from the input file
        '''
        assert DS.XR_POSITION.size == 39
        
    def test_yp_num(self):
        '''
        Check the number of YP positions read from the input file
        '''
        assert DS.YP_POSITION.size == 11
        
    def test_zt_num(self):
        '''
        Check the number of ZT positions read from the input file
        '''
        assert DS.ZT_POSITION.size == 39
        
    def test_block_11_cond_str(self):
        '''
        Check the block 11 conditional list that says what data should be printed
        '''
        
        assert DS.attrs['BLOCK_11_CL'] == 'TFFFTTFFFTFFTFFTTTTTFFFFFFFFFFFFFFTFFF'
        
    def test_block_11_vol_avg_dict(self):
        
        assert DS.attrs['VOL_AVG_FLAGS'] == [-2, -4, 1, 2, 3]
        
        
class TestRunOutput:
    '''
    Testing the output read by the code is correct
    '''
    
    def test_PLS_SPC_NAMES(self):
        
        assert (DS.PLS_SPECIES.data == np.array(['D+', 'HE+', 'HE++', 'N+', 'N++', 'N3+', 'N4+', 'N5+', 'N6+',
                                                 'N7+', 'N2*(A)D(', 'D2+D(B)', 'D2+N(B)', 'N2*(A)D2', 'N*(2D)D2',
                                                 'D2+D2(B)', 'D2+N2(B)', 'D3+N2(B)', 'NN2*(A)(', 'D2+ND(B)',
                                                 'D3+ND(B)', 'D2+ND2(B', 'D3+ND2(B', 'D2+ND3(B', 'D3+ND3(B',
                                                 'N2*(A)ND', 'N*(2D)ND', 'D2ND+(B)', 'D2ND2+(B', 'D(B)', 'D2(B)',
                                                 'DD2(B)', 'D2D(B)', 'DHE(B)', 'HED(B)', 'D2HE(B)', 'HED2(B)',
                                                 'HE(B)', 'DN(B)', 'ND(B)', 'D2N(B)', 'ND2(B)', 'HEN(B)', 'NHE(B)',
                                                 'N(B)', 'DN2(B)', 'N2D(B)', 'D2N2(B)', 'N2D2(B)', 'HEN2(B)',
                                                 'N2HE(B)', 'NN2(B)', 'N2N(B)', 'N2N2(B)', 'ND3(B)', 'AR+',
                                                 'DAR(B)', 'ARD(B)', 'DND(B)', 'NDD(B)', 'DND2(B)', 'ND2D(B)',
                                                 'DND3(B)', 'ND3D(B)', 'NAR(B)', 'ARN(B)', 'NND(B)', 'NDN(B)',
                                                 'NND2(B)', 'ND2N(B)', 'NND3(B)', 'ND3N(B)', 'HEAR(B)', 'ARHE(B)',
                                                 'HEND(B)', 'NDHE(B)', 'HEND2(B)', 'ND2HE(B)', 'HEND3(B)',
                                                 'ND3HE(B)', 'D2AR(B)', 'ARD2(B)', 'D2ND(B)', 'NDD2(B)', 'D2ND2(B)',
                                                 'ND2D2(B)', 'D2ND3(B)', 'ND3D2(B)', 'N2AR(B)', 'ARN2(B)',
                                                 'N2ND(B)', 'NDN2(B)', 'N2ND2(B)', 'ND2N2(B)', 'N2ND3(B)',
                                                 'ND3N2(B)', 'ARND(B)', 'NDAR(B)', 'ARND2(B)', 'ND2AR(B)',
                                                 'ARND3(B)', 'ND3AR(B)', 'ARAR(B)', 'NDND(B)', 'NDND2(B)',
                                                 'ND2ND(B)', 'NDND3(B)', 'ND3ND(B)', 'ND2(B)', 'ND23(B)', 'ND32(B)'])).all()
    
    def test_ATM_SPC_NAMES(self):
        
        assert (DS.ATM_SPECIES.data == np.array(['D', 'HE', 'N', 'N*(2P)', 'N*(2D)', 'AR'], dtype='<U6')).all()
    
    def test_MOL_SPC_NAMES(self):
        
        assert (DS.MOL_SPECIES.data == np.array(['D2', 'N2', 'N2*(A)', 'ND', 'ND2', 'ND3'], dtype='<U6')).all()
        
    def test_ION_SPC_NAMES(self):
        
        assert (DS.ION_SPECIES.data == np.array(['D2+', 'D3+', 'ND+', 'ND2+', 'ND3+', 'ND4+', 'N2+', 'N2D+'],
                                                dtype='<U4')).all()
    
    def test_PLS_BLA_TEMP(self):
        '''
        '''
        assert DS.PLS_BLA_TEMP.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array(2.8987)
    
    def test_PLS_BLA_DENS(self):
        '''
        '''
        assert DS.PLS_BLA_DENS.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array(1.8146E12)
        
    def test_ATM_BLA_DENS(self):
        '''
        '''
        assert DS.ATOM_BLA_DENS.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0).data == np.array(6.0686E+06)

    def test_MOL_BLA_DENS(self):
        '''
        '''
        assert DS.MOL_BLA_DENS.isel(TIME_STP = 1,ITERATION = 0,MOL_SPECIES = 0).data == np.array(535530.)
        
    def test_ION_BLA_DENS(self):
        '''
        '''
        assert DS.ION_BLA_DENS.isel(TIME_STP = 1,ITERATION = 0,ION_SPECIES = 0).data == np.array(2.0901E+04)
    


    def test_PLS_1D_T_XR(self):
        '''
        '''
        assert (DS.PLS_XR_TEMP.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([ 2.5900E-02     ,    2.5337E-02     ,    2.5324E-02     ,    1.2950E-02     ,    0.0000E+00
    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02
    ,    1.7267E-02    ,    0.0000E+00    ,    0.0000E+00    ,    2.5900E-02    ,    1.7267E-02
    ,    1.2950E-02    ,    1.2950E-02    ,    2.5900E-02    ,    8.7418E+00    ,    8.7554E+00
    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02
    ,    0.0000E+00    ,    1.9425E-02    ,    1.9425E-02    ,    1.7267E-02    ,    1.2950E-02
    ,    2.5900E-02    ,    1.9425E-02    ,    1.9425E-02    ,    1.9425E-02    ,    1.7267E-02
    ,    1.7267E-02    ,    1.7267E-02    ,    1.7267E-02    ,    0.0000E+00  ])).all()
        
    def test_PLS_1D_T_YP(self):
        '''
        '''
        assert (DS.PLS_YP_TEMP.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([ 0.0000E+00     ,    2.5673E-02     ,    0.0000E+00     ,    0.0000E+00     ,    9.3650E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    2.3743E-02
    ,    2.4331E-02  ])).all()
        
    def test_PLS_1D_T_ZT(self):
        '''
        '''
        assert (DS.PLS_ZT_TEMP.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([ 9.3650E+00     ,    2.5307E-02     ,    1.1655E-02     ,    0.0000E+00     ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00  ])).all()
        
        
    



    
    def test_PLS_1D_D_XR(self):
        '''
        '''
        assert (DS.PLS_XR_DENS.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([5.1282E+11, 
                1.1795E+13, 1.1538E+13, 5.1282E+11, 0.0000E+00,
        7.6923E+11    ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11
   ,    7.6923E+11    ,    0.0000E+00    ,    7.6923E+11    ,    5.1282E+11    ,    7.6923E+11
   ,    5.1282E+11    ,    5.1282E+11    ,    5.1282E+11    ,    1.1538E+13    ,    1.1795E+13
   ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11
   ,    0.0000E+00    ,    1.0256E+12    ,    1.0256E+12    ,    7.6923E+11    ,    5.1282E+11
   ,    7.6923E+11    ,    1.0256E+12    ,    1.0256E+12    ,    1.0256E+12    ,    7.6923E+11
   ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11    ,    7.6923E+11])).all()
    
    
    def test_PLS_1D_D_YP(self):
        '''
        '''
        assert (DS.PLS_YP_DENS.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([   2.3143E+12     ,    8.2448E+12     ,    0.0000E+00     ,    0.0000E+00     ,    6.1473E+12
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    8.6782E+11
   ,    2.3866E+12])).all()
    
    def test_PLS_1D_D_ZT(self):
        '''
        '''
        assert (DS.PLS_ZT_DENS.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0).data == np.array([   2.1795E+13     ,    3.3590E+13     ,    1.5385E+13     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00])).all()
    
    
    
    def test_ATM_1D_D_XR(self):
        '''
        '''
        assert (DS.ATM_XR_DENS.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0).data == np.array([ 0.0000E+00     ,    1.0066E+07     ,    2.6890E+07     ,    2.3839E+06     ,    2.0541E+07
   ,    2.3000E+07    ,    2.3960E+07    ,    3.3896E+06    ,    4.8187E+05    ,    3.9645E+06
   ,    3.2914E+05    ,    3.1090E+05    ,    2.9539E+05    ,    2.8200E+05    ,    2.7027E+05
   ,    2.5990E+05    ,    2.5064E+05    ,    2.4230E+05    ,    7.2690E+06    ,    7.0757E+06
   ,    6.8363E+06    ,    1.0365E+07    ,    9.6685E+06    ,    9.2797E+06    ,    7.6947E+06
   ,    3.0958E+06    ,    3.0293E+06    ,    2.9669E+06    ,    6.2121E+06    ,    2.8528E+06
   ,    2.8005E+06    ,    2.7510E+06    ,    5.7353E+06    ,    7.3437E+06    ,    7.0974E+06
   ,    6.8776E+06    ,    6.6795E+06    ,    2.9636E+06    ,    1.1611E+06   ])).all()
    
    def test_ATM_1D_D_YP(self):
        '''
        '''
        assert (DS.ATM_YP_DENS.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0).data == np.array([  0.0000E+00     ,    1.4556E+07     ,    3.2300E+06     ,    1.5394E+07     ,    6.2652E+05
   ,    4.6841E+05    ,    7.5576E+05    ,    1.6793E+06    ,    1.1170E+07    ,    8.3843E+06
   ,    1.0491E+07  ])).all()
        
    def test_ATM_1D_D_ZT(self):
        '''
        '''
        assert (DS.ATM_ZT_DENS.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0).data == np.array([ 7.9292E+06     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    2.1179E+07    ,    1.6932E+06    ,    3.6135E+06    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    8.1731E+07    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    4.3677E+07    ,    0.0000E+00    ,    0.0000E+00    ,    3.3039E+06    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    6.2097E+07    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    1.1452E+07    ,    0.0000E+00    ,    0.0000E+00   ])).all()
        
        
        
        
    def test_MOL_1D_D_XR(self):
        '''
        '''
        assert (DS.MOL_XR_DENS.isel(TIME_STP = 1,ITERATION = 0,MOL_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    1.0276E+07    ,    1.0615E+07  ])).all()
        
    def test_MOL_1D_D_YP(self):
        '''
        '''
        assert (DS.MOL_YP_DENS.isel(TIME_STP = 1,ITERATION = 0,MOL_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    5.8908E+06     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00  ])).all()
        
    def test_MOL_1D_D_ZT(self):
        '''
        '''
        assert (DS.MOL_ZT_DENS.isel(TIME_STP = 1,ITERATION = 0,MOL_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    2.0886E+07    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00  ])).all()
        
        
        
        
        
        
        
    def test_ION_1D_D_XR(self):
        '''
        '''
        assert (DS.ION_XR_DENS.isel(TIME_STP = 1,ITERATION = 0,ION_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    8.1515E+05    ,    0.0000E+00  ])).all()
        
    def test_ION_1D_D_YP(self):
        '''
        '''
        assert (DS.ION_YP_DENS.isel(TIME_STP = 1,ITERATION = 0,ION_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    2.2992E+05     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00   ])).all()
        
    def test_ION_1D_D_ZT(self):
        '''
        '''
        assert (DS.ION_ZT_DENS.isel(TIME_STP = 1,ITERATION = 0,ION_SPECIES = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    8.1515E+05    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00 ])).all()
    
    
    def test_PLS_2D_T_YP_ZT(self):
        
        assert (DS.PLS_YP_ZT_TEMP_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,ZT_POSITION = 0).data == np.array([0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    9.3650E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00])).all()
    
    def test_PLS_2D_T_XR_YP(self):
        
        assert (DS.PLS_XR_YP_TEMP_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,YP_POSITION = 1).data == np.array([2.5900E-02     ,    2.5900E-02     ,    2.5900E-02     ,    0.0000E+00     ,    0.0000E+00
   ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02
   ,    2.5900E-02    ,    0.0000E+00    ,    0.0000E+00    ,    2.5900E-02    ,    2.5900E-02
   ,    2.5900E-02    ,    0.0000E+00    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02
   ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02
   ,    0.0000E+00    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    0.0000E+00
   ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    2.5900E-02    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ])).all()
    
    
    def test_PLS_2D_T_XR_ZT(self):
        
        assert (DS.PLS_XR_ZT_TEMP_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,ZT_POSITION = 0).data == np.array([0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ])).all()
    
    
    def test_PLS_2D_D_YP_ZT(self):
        
        assert (DS.PLS_YP_ZT_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    2.3975E+14
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00 ])).all()
       
    def test_PLS_2D_D_XR_YP(self):
        
        assert (DS.PLS_XR_YP_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,YP_POSITION = 0).data == np.array([ 0.0000E+00     ,    2.8205E+12     ,    2.8205E+12     ,    2.8205E+12     ,    0.0000E+00
   ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12
   ,    2.8205E+12    ,    0.0000E+00    ,    2.8205E+12    ,    0.0000E+00    ,    2.8205E+12
   ,    2.8205E+12    ,    2.8205E+12    ,    0.0000E+00    ,    2.8205E+12    ,    2.8205E+12
   ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12
   ,    0.0000E+00    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12
   ,    0.0000E+00    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12
   ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12    ,    2.8205E+12 ])).all()
    
    def test_PLS_2D_D_XR_ZT(self):
        
        assert (DS.PLS_XR_ZT_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,ZT_POSITION = 0).data == np.array([0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    4.2000E+14    ,    4.3000E+14
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00  ])).all()
    
    def test_ATM_2D_D_YP_ZT(self):
        
        assert (DS.ATM_YP_ZT_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 0.0000E+00     ,    8.7221E+07     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00 ])).all()
       
    def test_ATM_2D_D_XR_YP(self):
        
        assert (DS.ATM_XR_YP_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0,YP_POSITION = 1).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    8.7219E+07    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    7.7377E+07    ,    7.5327E+07
   ,    7.2762E+07    ,    7.0443E+07    ,    6.8333E+07    ,    6.6401E+07    ,    4.9805E+07
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00 ])).all()
    
    def test_ATM_2D_D_XR_ZT(self):
        
        assert (DS.ATM_XR_ZT_DENS_2D.isel(TIME_STP = 1,ITERATION = 0,ATM_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    3.0923E+08    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00 ])).all()
    
    def test_MOL_2D_D_YP_ZT(self):
        
        assert (DS.MOL_YP_ZT_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,MOL_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 5.5462E+02     ,    3.8532E+02     ,    9.0742E+02     ,    1.0960E+03     ,    4.0094E+02
   ,    2.1372E+02    ,    2.5246E+02    ,    6.4583E+02    ,    1.3870E+03    ,    2.3935E+03
   ,    1.4154E+03 ])).all()
       
    def test_MOL_2D_D_XR_YP(self):
        
        assert (DS.MOL_XR_YP_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,MOL_SPECIES = 0,YP_POSITION = 0).data == np.array([ 2.8418E+02     ,    0.0000E+00     ,    6.3487E+01     ,    6.6568E+02     ,    4.4786E+02
   ,    4.2633E+02    ,    5.5914E+02    ,    1.1828E+03    ,    1.0610E+03    ,    9.7100E+02
   ,    9.7586E+02    ,    2.0725E+03    ,    2.9920E+03    ,    1.8383E+03    ,    2.1196E+04
   ,    7.2882E+03    ,    4.8150E+03    ,    1.9270E+03    ,    1.8025E+03    ,    1.6916E+03
   ,    1.6038E+03    ,    5.2659E+03    ,    1.8264E+03    ,    1.7202E+03    ,    1.6812E+03
   ,    1.6129E+03    ,    1.5546E+03    ,    1.5035E+03    ,    1.4581E+03    ,    1.3409E+03
   ,    1.2497E+03    ,    1.2179E+03    ,    1.8915E+03    ,    2.3623E+03    ,    1.5645E+03
   ,    1.7280E+03    ,    2.1148E+03    ,    2.4274E+03    ,    1.0390E+03 ])).all()
    
    def test_MOL_2D_D_XR_ZT(self):
        
        assert (DS.MOL_XR_ZT_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,MOL_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 8.0336E+02     ,    3.7959E+02     ,    2.8448E+02     ,    4.0104E+03     ,    2.8063E+03
   ,    2.3089E+03    ,    2.1565E+03    ,    1.5375E+03    ,    1.2838E+03    ,    1.1637E+03
   ,    1.0735E+03    ,    1.0021E+03    ,    9.4364E+02    ,    8.9455E+02    ,    8.5252E+02
   ,    8.1600E+02    ,    7.8385E+02    ,    7.5527E+02    ,    7.2963E+02    ,    7.0645E+02
   ,    6.8537E+02    ,    6.6608E+02    ,    6.4835E+02    ,    6.3196E+02    ,    6.1677E+02
   ,    6.0262E+02    ,    5.8941E+02    ,    5.7703E+02    ,    5.6541E+02    ,    5.5446E+02
   ,    5.4413E+02    ,    3.9083E+02    ,    3.3739E+02    ,    3.3179E+02    ,    2.7113E+02
   ,    2.6659E+02    ,    2.6259E+02    ,    2.5877E+02    ,    1.2835E+02 ])).all()
      
    def test_ION_2D_D_YP_ZT(self):
        
        assert (DS.ION_YP_ZT_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,ION_SPECIES = 0,ZT_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    4.0126E+00    ,    8.0251E+00    ,    0.0000E+00
   ,    0.0000E+00 ])).all()
       
    def test_ION_2D_D_XR_YP(self):
        
        assert (DS.ION_XR_YP_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,ION_SPECIES = 0,YP_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    3.2100E+01    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    6.4200E+01    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00 ])).all()
    
    def test_ION_2D_D_XR_ZT(self):
        
        assert (DS.ION_XR_ZT_DENS_2D.isel(TIME_STP = 2,ITERATION = 1,ION_SPECIES = 0,ZT_POSITION = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    2.8452E+01    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    1.4226E+01
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00])).all()
    
    
    
    def test_PLS_3D_T(self):
        
        assert (DS3.PLS_XR_TEMP_3D.isel(TIME_STP = 1,ITERATION = 0,PLS_SPECIES = 0,ZT_POSITION = 0,YP_POSITION = 0).data == np.array([  9.3650E+00     ,    9.3650E+00     ,    9.3650E+00     ,    9.3650E+00     ,    0.0000E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    0.0000E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    0.0000E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    0.0000E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00
   ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00    ,    9.3650E+00 ])).all()
    
    def test_PLS_3D_D(self):
        
        assert (DS3.PLS_XR_DENS_3D.isel(TIME_STP = 0,ITERATION = 1,PLS_SPECIES = 0,ZT_POSITION = 0,YP_POSITION = 4).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    5.0000E+14    ,    5.0000E+14
   ,    5.0000E+14    ,    5.0000E+14    ,    0.0000E+00    ,    5.0000E+14    ,    5.0000E+14
   ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14
   ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14
   ,    0.0000E+00    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14
   ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14    ,    5.0000E+14 ])).all()
    
    
    def test_ATM_3D_D(self):
        
        assert (DS3.ATM_XR_DENS_3D.isel(TIME_STP = 0,ITERATION = 1,ATM_SPECIES = 0,ZT_POSITION = 0,YP_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    1.9399E+08    ,    9.2470E+08    ,    8.8757E+08
   ,    8.5458E+08    ,    1.3372E+09    ,    1.9864E+09    ,    1.9154E+09    ,    2.1076E+09
   ,    2.2415E+09    ,    2.1740E+09    ,    2.2405E+09    ,    2.6300E+09    ,    1.6714E+09
   ,    2.7962E+09    ,    2.6470E+09    ,    2.6331E+09    ,    1.0925E+10    ,    5.3820E+09
   ,    8.0182E+09    ,    1.2297E+10    ,    1.8961E+10    ,    2.7874E+10    ,    2.4280E+10
   ,    2.5679E+10    ,    2.7865E+10    ,    3.6966E+10    ,    2.7194E+10])).all()
    
    def test_MOL_3D_D(self):
        
        assert (DS3.MOL_XR_DENS_3D.isel(TIME_STP = 0,ITERATION = 1,MOL_SPECIES = 0,ZT_POSITION = 0,YP_POSITION = 0).data == np.array([ 0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    7.6425E+09    ,    9.3820E+09    ,    9.2356E+09    ,    1.9378E+10
   ,    4.2687E+10    ,    7.7550E+10    ,    2.6706E+11    ,    2.8638E+11 ])).all()
    
    def test_ION_3D_D(self):
        
        assert (DS3.ION_XR_DENS_3D.isel(TIME_STP = 0,ITERATION = 1,ION_SPECIES = 0,ZT_POSITION = 0,YP_POSITION = 0).data == np.array([  0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00     ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00    ,    0.0000E+00
   ,    0.0000E+00    ,    7.1012E+08    ,    0.0000E+00    ,    0.0000E+00    ,    1.7753E+09
   ,    1.4202E+09    ,    4.2607E+09    ,    9.4091E+09    ,    1.1723E+10])).all()
        
    def test_fort_with_old_data_pls_temp(self):
        
        a = DS_fort.FT_PLS_TEMP.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=0,PLS_SPECIES=0,YP_POSITION=0).data
        a = a[0:len(a)-1]
        b = DS_fort.PLS_XR_TEMP_3D.isel(ITERATION=0,TIME_STP=0,PLS_SPECIES=0,ZT_POSITION=0,YP_POSITION=0).data
        b = b[0:len(b)-1]
        
        assert np.isclose(a,b,1e-3).all()
        
        
        a1 = DS_fort.FT_PLS_TEMP.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=32,PLS_SPECIES=0,YP_POSITION=6).data
        a1 = a1[0:len(a1)-1]
        b1 = DS_fort.PLS_XR_TEMP_3D.isel(ITERATION=0,TIME_STP=0,PLS_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b1 = b1[0:len(b1)-1]
        
        assert np.isclose(a1,b1,1e-3).all()
        
        a2 = DS_fort.FT_PLS_TEMP.isel(TIME_STP=1,ITERATION=1,ZT_POSITION=32,PLS_SPECIES=4,YP_POSITION=6).data
        a2 = a2[0:len(a2)-1]
        b2 = DS_fort.PLS_XR_TEMP_3D.isel(ITERATION=1,TIME_STP=1,PLS_SPECIES=4,ZT_POSITION=32,YP_POSITION=6).data
        b2 = b2[0:len(b2)-1]
        
        assert np.isclose(a2,b2,1e-3).all()   
        
    def test_fort_with_old_data_pls_dens(self):
        
        a = DS_fort.FT_PLS_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=0,PLS_SPECIES=0,YP_POSITION=0).data
        a = a[0:len(a)-1]
        b = DS_fort.PLS_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,PLS_SPECIES=0,ZT_POSITION=0,YP_POSITION=0).data
        b = b[0:len(b)-1]
        
        assert np.isclose(a,b,1e-3).all()
        
        
        a1 = DS_fort.FT_PLS_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=32,PLS_SPECIES=0,YP_POSITION=6).data
        a1 = a1[0:len(a1)-1]
        b1 = DS_fort.PLS_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,PLS_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b1 = b1[0:len(b1)-1]
        
        assert np.isclose(a1,b1,1e-3).all()
        
        a2 = DS_fort.FT_PLS_DENS.isel(TIME_STP=1,ITERATION=1,ZT_POSITION=32,PLS_SPECIES=4,YP_POSITION=6).data
        a2 = a2[0:len(a2)-1]
        b2 = DS_fort.PLS_XR_DENS_3D.isel(ITERATION=1,TIME_STP=1,PLS_SPECIES=4,ZT_POSITION=32,YP_POSITION=6).data
        b2 = b2[0:len(b2)-1]
        
        assert np.isclose(a2,b2,1e-3).all()
        
    def test_fort_with_old_data_atm_dens(self):
        
        a = DS_fort.FT_ATM_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=0,ATM_SPECIES=0,YP_POSITION=0).data
        a = a[0:len(a)-1]
        b = DS_fort.ATM_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,ATM_SPECIES=0,ZT_POSITION=0,YP_POSITION=0).data
        b = b[0:len(b)-1]
        
        assert np.isclose(a,b,1e-3).all()
        
        
        a1 = DS_fort.FT_ATM_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=32,ATM_SPECIES=0,YP_POSITION=6).data
        a1 = a1[0:len(a1)-1]
        b1 = DS_fort.ATM_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,ATM_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b1 = b1[0:len(b1)-1]
        
        assert np.isclose(a1,b1,1e-3).all()
        
        a2 = DS_fort.FT_ATM_DENS.isel(TIME_STP=1,ITERATION=1,ZT_POSITION=32,ATM_SPECIES=1,YP_POSITION=6).data
        a2 = a2[0:len(a2)-1]
        b2 = DS_fort.ATM_XR_DENS_3D.isel(ITERATION=1,TIME_STP=1,ATM_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b2 = b2[0:len(b2)-1]
        
        assert np.isclose(a2,b2,1e-3).all()
        
    def test_fort_with_old_data_mol_dens(self):
        
        a = DS_fort.FT_MOL_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=0,MOL_SPECIES=0,YP_POSITION=0).data
        a = a[0:len(a)-1]
        b = DS_fort.MOL_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,MOL_SPECIES=0,ZT_POSITION=0,YP_POSITION=0).data
        b = b[0:len(b)-1]
        
        assert np.isclose(a,b,1e-3).all()
        
        
        a1 = DS_fort.FT_MOL_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=32,MOL_SPECIES=0,YP_POSITION=6).data
        a1 = a1[0:len(a1)-1]
        b1 = DS_fort.MOL_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,MOL_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b1 = b1[0:len(b1)-1]
        
        assert np.isclose(a1,b1,1e-3).all()
        
        a2 = DS_fort.FT_MOL_DENS.isel(TIME_STP=2,ITERATION=1,ZT_POSITION=32,MOL_SPECIES=1,YP_POSITION=6).data
        a2 = a2[0:len(a2)-1]
        b2 = DS_fort.MOL_XR_DENS_3D.isel(ITERATION=1,TIME_STP=2,MOL_SPECIES=2,ZT_POSITION=32,YP_POSITION=6).data
        b2 = b2[0:len(b2)-1]
        
        assert np.isclose(a2,b2,1e-3).all()
        
    def test_fort_with_old_data_ion_dens(self):
        
        a = DS_fort.FT_ION_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=0,ION_SPECIES=0,YP_POSITION=0).data
        a = a[0:len(a)-1]
        b = DS_fort.ION_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,ION_SPECIES=0,ZT_POSITION=0,YP_POSITION=0).data
        b = b[0:len(b)-1]
        
        assert np.isclose(a,b,1e-3).all()
        
        
        a1 = DS_fort.FT_ION_DENS.isel(TIME_STP=0,ITERATION=0,ZT_POSITION=32,ION_SPECIES=0,YP_POSITION=6).data
        a1 = a1[0:len(a1)-1]
        b1 = DS_fort.ION_XR_DENS_3D.isel(ITERATION=0,TIME_STP=0,ION_SPECIES=0,ZT_POSITION=32,YP_POSITION=6).data
        b1 = b1[0:len(b1)-1]
        
        assert np.isclose(a1,b1,1e-3).all()
        
        a2 = DS_fort.FT_ION_DENS.isel(TIME_STP=2,ITERATION=1,ZT_POSITION=32,ION_SPECIES=1,YP_POSITION=6).data
        a2 = a2[0:len(a2)-1]
        b2 = DS_fort.ION_XR_DENS_3D.isel(ITERATION=1,TIME_STP=2,ION_SPECIES=2,ZT_POSITION=32,YP_POSITION=6).data
        b2 = b2[0:len(b2)-1]
        
        assert np.isclose(a2,b2,1e-3).all()
        
        
        
        
        
        

        
    
    
    
    
    
    
    
    
    
    
    

