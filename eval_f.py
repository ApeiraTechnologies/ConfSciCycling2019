from skcycling.io import bikeread
from model_perf.model_acd import f_apeira_correction
from model_perf.model_acd import ACd_apeira_correction
from utls.extract_data import check_crop
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import datetime


def draw(index, power, speed, debut, fin, name):
    l_draw = np.zeros(len(power))
    b_draw = False
    for j in range(len(debut)):
        b_draw = False
        for i in range(len(power)):
            # print('debut', debut[j])
            # print('fin', fin[j])
            # print('type index', type(index[i]))
            # print('type debut', type(debut[j]))
            if str(index[i]) == debut[j]:
                b_draw = True
            if str(index[i]) == fin[j]:
                l_draw[i] = 400
                b_draw = False
            if b_draw is True:
                l_draw[i] = 400

    df = pd.DataFrame()

    df['speed'] = speed
    df['power'] = power
    df['crop'] = l_draw
    df.to_csv(name+'.csv')


if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurGuillaume/'
    s_date = '2018-05-18'
    f_name = ['2018-05-18-11-12-07',
              '2018-05-18-14-10-54']

    exten = '.fit'

    f_crop = 'crop_guillaume_v2.csv'
    df = pd.read_csv(f_path_data + f_path_user + f_crop)

    df_out = pd.DataFrame()

    for f in range(len(f_name)):

        filename_fit = f_path_data + f_path_user + f_name[f] + exten
        print('Nom du fichier traité : ', filename_fit)
        ride = bikeread(filename_fit, drop_nan='columns')
        # ride['speed'] = ride['speed']
        ride_all = ride['speed'].tolist()
        power_all = ride['power'].tolist()
        l_crop = np.zeros(len(power_all))
        # print('The ride is the following:\n {}'.format(ride.head()))
        # print('The available data are {}'.format(ride.columns))
        all_index = ride.index.tolist()
        all_speed = ride['speed']
        all_power = ride['power']
        all_time_debut = df[f_name[f]+'-debut'].tolist()
        all_time_fin = df[f_name[f]+'-fin'].tolist()

        draw(all_index,
             all_power,
             all_speed,
             all_time_debut,
             all_time_fin,
             f_name[f])

        f_moy = []
        ACd_moy = []
        v_moy_q = []
        v_moy = []
        l_b_few = []
        l_b_period = []
        l_val_rest = []
        l_period = []

        for i in range(len(all_time_debut)):
            print('Index du crop : ', i)
            debut = str(all_time_debut[i])
            fin = str(all_time_fin[i])
            ride_crop = ride[debut:fin]
            speed = ride_crop['speed'].tolist()
            power = ride_crop['power'].tolist()
            # check if  there is enough data
            b_few, b_period, period, val_rest = check_crop(power,
                                                           speed,
                                                           100,
                                                           3,
                                                           1)
            l_b_few.append(b_few)
            l_b_period.append(b_period)
            l_val_rest.append(val_rest)
            l_period.append(period)

            temp = f_apeira_correction(power,
                                       speed,
                                       88,
                                       0.004,
                                       debug=True)
            temp1 = ACd_apeira_correction(power,
                                          speed,
                                          88,
                                          0.004,
                                          1010,
                                          20,
                                          debug=True)

            f_moy.append(temp)
            ACd_moy.append(temp1)
            v_moy.append(np.mean(speed))
            s_pow_2 = np.power(speed, 2)
            v_moy_q.append(np.sqrt(np.mean(s_pow_2)))

        print('Liste f_moy : ', f_moy)
        df_out[f_name[f]+'-force'] = f_moy
        df_out[f_name[f]+'-ACd'] = ACd_moy
        df_out[f_name[f]+'-vitesse moyenne'] = v_moy
        df_out[f_name[f]+'-vitesse moyenne quadratique'] = v_moy_q
        df_out[f_name[f]+'-b_few'] = l_b_few
        df_out[f_name[f]+'-b_period'] = l_b_period
        df_out[f_name[f]+'-val reste'] = l_val_rest
        df_out[f_name[f]+'-Nb periode'] = l_period

    df_out.to_csv('res_guillaume_v2_88.csv')
