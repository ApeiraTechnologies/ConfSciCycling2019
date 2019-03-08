from skcycling.io import bikeread
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import datetime

if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurGuillaume/'
    s_date = '2018-05-18'
    f_name = ['2018-05-18-14-10-54']
    exten = '.fit'

    f_crop = 'crop_guillaume.csv'
    f_list_pic = 'list_pic_guillaume.csv'
    df = pd.read_csv(f_path_data + f_path_user + f_crop)
    dic = {}

    for f in range(len(f_name)):

        filename_fit = f_path_data + f_path_user + f_name[f] + exten
        print('Nom du fichier traité : ', filename_fit)
        ride = bikeread(filename_fit, drop_nan='columns')
        ride['speed'] = ride['speed'] * 3.6
        # print('The ride is the following:\n {}'.format(ride.head()))
        # print('The available data are {}'.format(ride.columns))

        all_time_debut = pd.to_datetime(df[f_name[f]+'-debut']).tolist()
        all_time_fin = pd.to_datetime(df[f_name[f]+'-fin']).tolist()

        for i in range(len(all_time_debut)):
            print('Index du crop : ', i)
            debut = str(all_time_debut[i])
            fin = str(all_time_fin[i])
            ride_crop = ride[debut:fin]
            speed = ride_crop['speed']
            power = ride_crop['power'].tolist()
            mean_power = np.mean(power)

            l_pic = []
            acc = 0
            for ech in range(len(power)):
                if power[ech] >= mean_power:
                    acc += power[ech]
                else:
                    if acc != 0:
                        l_pic.append(acc)

                    acc = 0

            dic[debut] = l_pic
            print('NB pic : ', len(l_pic))

    df2 = pd.DataFrame.from_dict(dic, orient='index').T
    df2.to_csv(f_list_pic)
