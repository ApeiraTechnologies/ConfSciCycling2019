import numpy as np
import pandas as pd
# from model_perf.model_acd import est_wind
from model_perf.model_acd import inv_model_grappe_ACd
from model_perf.model_acd import inv_model_grappe_F
from utls.extract_data import extract_cedric_data

if __name__ == '__main__':

    path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'

    l_user_data = ['Cedric']
    l_etalonnage = [1]
    l_masse = [100]
    extension = ".csv"

    lut_s_v = ['25hv', '35hv', '25bv', '35bv']
    lut_s_f = ['25hf', '35hf', '25bf', '35bf']
    lut_s_acd = ['25hacd', '35hacd', '25bacd', '35bacd']

    df = pd.DataFrame()

    for j in range(len(l_user_data)):

        f_path = path_data + l_user_data[j] + extension
        l_power_mean, l_speed_mean = extract_cedric_data(f_path)

        l_speed_mean = np.array(l_speed_mean) / 3.6
        l_power_mean = np.array(l_power_mean) * 0.85 * l_etalonnage[j]
        l_ACd = []
        l_f_aero = []

        for k in range(len(l_power_mean)):
            l_ech_p = l_power_mean[k]
            l_ech_v = l_speed_mean[k]
            l_temp_f = []
            l_temp_acd = []
            for i in range(len(l_ech_p)):
                val_acd = inv_model_grappe_ACd(l_ech_p[i], l_ech_v[i],
                                               0, 20, 1015, 0.004, l_masse[j])
                val_f_aero = inv_model_grappe_F(l_ech_p[i], l_ech_v[i],
                                                0.004, l_masse[j])

                l_temp_f.append(val_f_aero)
                l_temp_acd.append(val_acd)

            l_ACd.append(l_temp_acd)
            l_f_aero.append(l_temp_f)

        for p in range(len(l_f_aero)):
            l_f = l_f_aero[p]
            l_acd = l_ACd[p]
            l_v = l_speed_mean[p]

            df[lut_s_v[p]] = l_v*3.6
            df[lut_s_f[p]] = l_f
            df[lut_s_acd[p]] = l_acd

        df.to_csv(path_data + 'res_cedric.csv')
