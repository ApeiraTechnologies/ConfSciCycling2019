import numpy as np
# from model_perf.model_acd import est_wind
from model_perf.model_acd import inv_model_grappe_ACd
from model_perf.model_acd import inv_model_grappe_F
from utls.extract_data import extract_with_pandas


if __name__ == '__main__':

    path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'

    user_data = 'Cedric.csv'

    l_power_mean, l_speed_mean = extract_with_pandas(path_data + user_data)

    # l_power_mean = [117, 139, 165, 212, 240, 283,
    #                 124, 146, 156, 214, 226, 278]
    # l_speed_mean = [25.1, 25.5, 30.5, 30.6, 34.8,
    #                 34.3, 27.1, 26.9, 31.3, 30.3,
    #                 34.8, 34.7]

    l_speed_mean = np.array(l_speed_mean) / 3.6
    l_power_mean = np.array(l_power_mean) * 0.85
    l_ACd = []
    l_f_aero = []
    # l_wind = []

    # for i in range(len(l_power_mean)):
    #     if i % 2 == 0:
    #         val_wind = est_wind(l_power_mean[i], l_power_mean[i+1],
    #                             l_speed_mean[i], l_speed_mean[i+1])
    #         l_wind.append(val_wind)

    # np.array(l_wind)
    # wind_mean = np.mean(l_wind)

    for i in range(len(l_power_mean)):
        val_acd = inv_model_grappe_ACd(l_power_mean[i], l_speed_mean[i],
                                       0, 20, 1015, 0.004, 100)
        val_f_aero = inv_model_grappe_F(l_power_mean[i], l_speed_mean[i],
                                        0.004, 100)
        l_f_aero.append(val_f_aero)
        l_ACd.append(val_acd)

        l_ACd_f = []

    # for i in range(6):
    #     print("ACd : ", l_ACd[i], "Aero Drag : ", l_f_aero[i])

    # for i in range(len(l_power_mean)):
    #     if i % 2 == 0:
    #         moy_acd = (l_ACd[i] + l_ACd[i+1]) / 2
    #         moy_f = (l_f_aero[i] + l_f_aero[i+1]) / 2
    #         l_ACd_f.append([moy_acd, moy_f])

    print("Valeur main en haut : Vitesse -  ACd - F")
    for i in range(len(l_power_mean) // 2):
        print(l_speed_mean[i]*3.6, "-", l_ACd[i], " - ", l_f_aero[i])

    print("Valeur main en bas : Vitesse - ACd - F")
    for i in range(len(l_power_mean) // 2):
        idx = i+len(l_power_mean) // 2
        print(l_speed_mean[idx]*3.6, "-", l_ACd[idx], " - ", l_f_aero[idx])
