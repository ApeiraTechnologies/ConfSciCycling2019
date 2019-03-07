from skcycling.io import bikeread
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurCedric/'
    s_date = '2018-05-18'
    f_name = ['2018-05-18-11-37-45',
              '2018-05-18-11-46-19',
              '2018-05-18-13-55-23',
              '2018-05-18-14-37-07',
              '2018-05-18-15-00-26',
              '2018-05-18-15-06-46']

    exten = '.fit'

    f_crop = 'check_std_cedric.csv'
    df = pd.read_csv(f_path_data + f_path_user + f_crop)

    for f in range(len(f_name)):

        filename_fit = f_path_data + f_path_user + f_name[f] + exten
        print('Nom du fichier traité : ', filename_fit)
        ride = bikeread(filename_fit, drop_nan='columns')
        ride['speed'] = ride['speed'] * 3.6
        # print('The ride is the following:\n {}'.format(ride.head()))
        # print('The available data are {}'.format(ride.columns))

        all_time = pd.to_datetime(df[f_name[f]]).tolist()
        all_time_15s = []

        for t in all_time:
            t_15s = t + datetime.timedelta(seconds=15)
            all_time_15s.append(t_15s)

        for i in range(len(all_time)):
            print('Index du crop : ', i)
            debut = str(all_time[i])
            fin = str(all_time_15s[i])
            ride_crop = ride[debut:fin]
            speed = ride_crop['speed']
            mean_power = ride_crop['power'].mean()
            speed_carre = np.power(speed, 2)
            speed_quadra = np.sqrt(np.mean(speed_carre))
            mean_speed = ride_crop['speed'].mean()
            std_speed = ride_crop['speed'].std()

            print('vitesse moyenne : ', mean_speed)
            print('moyenne quadratique : ', speed_quadra)
            print('vitesse écart type : ', std_speed)
            print('puissance moyenne : ', mean_power)
