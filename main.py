import mat73 as mat73
import numpy as np
import scipy.io

from fde_mode_data_analyzer import FDE_Mode_Data_Analyzer




te_simulation_data = mat73.loadmat('silicon_experiments//Data_30_by_30_1_to_1.mat')
silicon_test = FDE_Mode_Data_Analyzer(te_simulation_data)
silicon_test.plot_dispersion_te()