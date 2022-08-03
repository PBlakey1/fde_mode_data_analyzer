"""
FDE_Mode_data_Analyzer is a class for extracting useful information such as the effective index, group velocities, and
dispersion curves from .mat files produced in Lumerical FDE Mode solver.
"""

import numpy as np
import matplotlib.pyplot as plt



class FDE_Mode_Data_Analyzer:

    # Define Plot Axis Settings
    axis_font = {'fontname': 'Arial', 'size': '16'}
    title_font = {'fontname': 'Arial', 'size': '20'}

    # Define useful constants
    c = 299792458                                       # Speed of Light in m/s
    nm = 1e9                                            # 1 meter = 1e9 nm
    ps_nm_km = 1e6                                      # 1 s/m^2 = 1 ps/(nm*km)

    def __init__(self, te_sweep_data, *, tm_sweep_data=''):
        self.f = te_sweep_data['f']
        self.wl = self.c/self.f
        self.cband_TE_D = te_sweep_data['D']
        self.cband_TE_neff = np.real(te_sweep_data['n'])
        self.cband_TE_GVD = -self.cband_TE_D * self.c / (self.f ** 2) / 2 / np.pi;
        if tm_sweep_data == '':
            print('Initialized FDE Mode Data Analyzer for One Mode Only... (default is TE)')
        else:
            self.cband_TM_D = tm_sweep_data['D']
            self.cband_TM_neff = np.real(tm_sweep_data['n'])
            self.cband_TM_GVD = -self.cband_TM_D * self.c / (self.f ** 2) / 2 / np.pi;

    def plot_n_eff_te(self):
        plt.plot(self.wl * self.nm, self.cband_TE_neff, color='b', label='TE')
        plt.title('TE Mode Effective Index', self.title_font)
        plt.xlabel('Wavelength (nm)', **self.axis_font)
        plt.ylabel('Effective Index $n_{eff}$', **self.axis_font)
        plt.grid('on')
        plt.legend()
        plt.show()

    def plot_n_eff_tm(self):
        plt.plot(self.wl * self.nm, self.cband_TM_neff, color='b', label='TE', lw=1.4, zorder=-1)
        plt.title('TE Mode Effective Index', **self.title_font)
        plt.xlabel('Wavelength (nm)', **self.axis_font)
        plt.ylabel('Effective Index $n_{eff}$', **self.axis_font)
        plt.grid('on')
        plt.legend(fontsize=12, frameon=False)
        plt.show()

    def plot_dispersion_te(self):

        plt.plot(self.wl * self.nm, self.cband_TE_D * self.ps_nm_km, color='b', label='TE')
        plt.title('TE Mode Dispersion Parameter', **self.title_font)
        plt.xlabel('Wavelength (nm)', **self.axis_font)
        plt.ylabel('Dispersion Parameter $D$ ps/(nm * km)', **self.axis_font)
        plt.grid('on')
        plt.legend(fontsize=12, frameon=False)
        plt.show()
