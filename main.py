import numpy as np
# from model_perf.model_acd import est_wind
from model_perf.model_acd import inv_model_grappe_ACd
from model_perf.model_acd import inv_model_grappe_F

if __name__ == '__main__':

    path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'

    l_user_data = ['Guillaume', 'Denis', 'Aurel']
    l_etalonnage = [1.02, 1, 1.61]
    l_masse = [88, 78, 78]
    extension = ".csv"

    for j in range(len(l_user_data)):

        f_path = path_data + l_user_data[j] + extension
        print(f_path)
        l_power_mean, l_speed_mean = extract_with_pandas(f_path)

        l_speed_mean = np.array(l_speed_mean) / 3.6
        l_power_mean = np.array(l_power_mean) * 0.85 * l_etalonnage[j]
        l_ACd = []
        l_f_aero = []

        for i in range(len(l_power_mean)):
            val_acd = inv_model_grappe_ACd(l_power_mean[i], l_speed_mean[i],
                                           0, 20, 1015, 0.004, l_masse[j])
            val_f_aero = inv_model_grappe_F(l_power_mean[i], l_speed_mean[i],
                                            0.004, l_masse[j])
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

        print("User : ", l_user_data[j])
        print("Valeur main en haut : Vitesse - ACd - F")
        for i in range(len(l_power_mean) // 3):
            print(l_speed_mean[i]*3.6, "-", l_ACd[i], " - ", l_f_aero[i])

        print("Valeur main aux poignées : Vitesse - ACd - F")
        for i in range(len(l_power_mean) // 3, 2 * len(l_power_mean) // 3):
            idx = i
            print(l_speed_mean[idx]*3.6, "-", l_ACd[idx], " - ", l_f_aero[idx])

        print("Valeur main en bas : Vitesse - ACd - F")
        for i in range(2 * len(l_power_mean) // 3, len(l_power_mean)):
            idx = i
            print(l_speed_mean[idx]*3.6, "-", l_ACd[idx], " - ", l_f_aero[idx])
        print("\n")
        print("\n")
