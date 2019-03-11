from skcycling.io import bikeread
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import datetime

if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurDenis/'
    s_date = '2018-05-18'
    # f_name = ['2018-05-18-14-10-54']
    f_name = ['2018-05-18-16-09-15']
    exten = '.fit'

    f_crop = 'crop_denis.csv'
    f_list_pic = 'list_pic_denis.csv'
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

        df3 = pd.DataFrame()

        for i in range(len(all_time_debut)):
            print('Index du crop : ', i)
            debut = str(all_time_debut[i])
            fin = str(all_time_fin[i])
            ride_crop = ride[debut:fin]
            speed = ride_crop['speed']
            power = ride_crop['power'].tolist()
            mean_power = np.mean(power)

            l_pic_h = []
            l_pic_b = []

            x = []

            for n in range(len(power)):
                x.append(x)

            l_plot_h = np.zeros(len(power))
            l_plot_b = np.zeros(len(power))
            acc_b = 0
            acc_h = 0
            ontop = False
            if power[0] >= mean_power:
                ontop = True
            else:
                ontop = False

            for ech in range(len(power)):
                if power[ech] >= mean_power:
                    if ontop is False:
                        l_pic_b.append(acc_b)
                        acc_b = 0
                        acc_h += (power[ech] - mean_power)
                        l_plot_h[ech] = 400
                        ontop = True
                    else:
                        acc_h += (power[ech] - mean_power)
                        l_plot_h[ech] = 400
                else:
                    if ontop is False:
                        acc_b += np.abs(power[ech] - mean_power)
                        l_plot_b[ech] = 100

                    else:
                        l_pic_h.append(acc_h)
                        acc_h = 0
                        ontop = False
                        acc_b += np.abs(power[ech] - mean_power)
                        l_plot_b[ech] = 100

            dic[debut+'-sup'] = l_pic_h
            dic[debut+'-inf'] = l_pic_b
            acc_h = 0
            acc_b = 0

            # df3['power'] = power
            # df3['haut'] = l_plot_h
            # df3['bas'] = l_plot_b
            # df3.to_csv(str(all_time_debut[i]))

    df2 = pd.DataFrame.from_dict(dic, orient='index').T
    df2.to_csv(f_list_pic)
