import eirenex 
import matplotlib.pyplot as plt

DS = eirenex.data.run('examples/cylinder/test_2D_raw/test_2D.in','examples/cylinder/test_2D_raw/test_2D.out')
DS_3d = eirenex.data.run('examples/cylinder/test_3D_raw/TEST_3D.in','examples/cylinder/test_3D_raw/TEST_3D.out')
aug_toy_data = eirenex.data.run('examples/cylinder/test_geom/input.dat', 'examples/cylinder/test_geom/run.log','examples/cylinder/test_geom/fort.90','examples/cylinder/test_geom/fort.91','examples/cylinder/test_geom/fort.92','examples/cylinder/test_geom/fort.93','examples/cylinder/test_geom/fort.94')
aug_geom = eirenex.geometry.AUG_TOY_GEOM()


class Testplot0d:
    
    def test_atm_dens_0d(self):
        
        eirenex.plot.avg_d_atm(DS)
        
        pass
    
    def test_mol_dens_0d(self):
        
        eirenex.plot.avg_d_mol(DS)
        
        pass
    
    def test_ion_dens_0d(self):
        
        eirenex.plot.avg_d_ion(DS)
        
        pass
    
    def test_pls_dens_0d(self):
        
        eirenex.plot.avg_d_pls(DS)
        
        pass
    
    def test_pls_temp_0d(self):
        
        eirenex.plot.avg_t_pls(DS)
        
        pass
    
class Testplot1d:
    
    def test_pls_temp_1d(self):
        
        fig1,fig2 = eirenex.plot.cyl_1d_t_pls(DS,'D+')
        plt.close(fig1)
        plt.close(fig2)
    
    def test_pls_dens_1d(self):
        
        fig1,fig2 = eirenex.plot.cyl_1d_d_pls(DS,'D+')
        plt.close(fig1)
        plt.close(fig2)
    
    def test_atm_dens_1d(self):
        
        fig1,fig2 = eirenex.plot.cyl_1d_d_atm(DS,'D')
        plt.close(fig1)
        plt.close(fig2)
    
    def test_mol_dens_1d(self):
        
        fig1,fig2 = eirenex.plot.cyl_1d_d_mol(DS,'D2')
        plt.close(fig1)
        plt.close(fig2)
        
    def test_ion_dens_1d(self):
        
        fig1,fig2 = eirenex.plot.cyl_1d_d_ion(DS,'D2+')
        plt.close(fig1)
        plt.close(fig2)
        
        
class Testplot2d:
    
    def test_pls_temp_2d(self):
        
        fig1,fig2 = eirenex.plot.cyl_2d_t_pls(DS,'D+')
        plt.close(fig1)
        plt.close(fig2)
    
    def test_pls_dens_2d(self):
        
        fig1,fig2 = eirenex.plot.cyl_2d_d_pls(DS,'D+')
        plt.close(fig1)
        plt.close(fig2)
        
    def test_atm_dens_2d(self):
        
        fig1,fig2 = eirenex.plot.cyl_2d_d_atm(DS,'D')
        plt.close(fig1)
        plt.close(fig2)
    
    def test_mol_dens_2d(self):
        
        fig1,fig2 = eirenex.plot.cyl_2d_d_mol(DS,'D2')
        plt.close(fig1)
        plt.close(fig2)
        
    def test_ion_dens_2d(self):
        
        fig1,fig2 = eirenex.plot.cyl_2d_d_ion(DS,'D2+')
        plt.close(fig1)
        plt.close(fig2)
        
class Testplot3d:
    
    def test_pls_temp_3d(self):
        
        fig1 = eirenex.plot.cyl_3d_t_pls(DS_3d, 'D+')
        plt.close(fig1)
        
    def test_pls_dens_3d(self):
        
        fig1 = eirenex.plot.cyl_3d_d_pls(DS_3d, 'D+')
        plt.close(fig1)
        
    def test_atm_dnes_3d(self):
        
        fig1 = eirenex.plot.cyl_3d_d_atm(DS_3d, 'D')
        plt.close(fig1)
        
    def test_mol_dens_3d(self):
        
        fig1 = eirenex.plot.cyl_3d_d_mol(DS_3d, 'D2')
        plt.close(fig1)
        
    def test_ion_dens_3d(self):
        
        fig1 = eirenex.plot.cyl_3d_d_ion(DS_3d, 'D2+')
        plt.close(fig1)
        
        
class TestGenPlot:
    
    def test_pls_temp_gen_plot_poloidal_view(self):
        
        fig1 = eirenex.plot.pls_temp_3D_poloidal_view(aug_toy_data, aug_geom, 'D+')
        plt.close(fig1)
        
    def test_pls_dens_gen_plot_poloidal_view(self):
        
        fig1 = eirenex.plot.pls_dens_3D_poloidal_view(aug_toy_data, aug_geom, 'D+')
        plt.close(fig1)
    
    def test_atm_dens_gen_plot_poloidal_view(self):
        
        fig1 = eirenex.plot.atm_dens_3D_poloidal_view(aug_toy_data, aug_geom, 'D')
        plt.close(fig1)
        
    def test_mol_dens_gen_plot_poloidal_view(self):
        
        fig1 = eirenex.plot.mol_dens_3D_poloidal_view(aug_toy_data, aug_geom, 'D2')
        plt.close(fig1)
        
    def test_ion_dens_gen_plot_poloidal_view(self):
        
        fig1 = eirenex.plot.ion_dens_3D_poloidal_view(aug_toy_data, aug_geom, 'D2+')
        plt.close(fig1)
        
        
    

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
