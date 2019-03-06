from skcycling.io import bikeread
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurCedric/'
    f_name = '2018-05-18-11-37-45.fit'
    filename_fit = f_path_data + f_path_user + f_name
    ride = bikeread(filename_fit, drop_nan='columns')
    print('The ride is the following:\n {}'.format(ride.head()))
    print('The available data are {}'.format(ride.columns))

    # ride['power'].plot(legend=True)
    ride['speed'] = ride['speed'] * 3.6
    ride['speed'].plot(legend=True)
    # ride_crop = ride['2018-05-18 09:46:29':'2018-05-18 09:47:13']
    # speed = ride_crop['speed']
    # speed_carre = np.power(speed, 2)
    # speed_quadra = np.sqrt(np.mean(speed_carre))
    # mean_speed = ride_crop['speed'].mean()
    # std_speed = ride_crop['speed'].std()

    # print('vitesse moyenne : ', mean_speed)
    # print('moyenne quadratique : ', speed_quadra)
    # print('vitesse écart type : ', std_speed)

    plt.xlabel('Time')
    plt.ylabel('Power (W)')
    plt.show()
