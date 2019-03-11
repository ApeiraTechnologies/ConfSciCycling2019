from skcycling.io import bikeread
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame()

path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
user = 'UtilisateurCedric/'
# user = 'UtilisateurGuillaume/'
# user = 'UtilisateurDenis/'
# user = 'UtilisateurAurel/'
f_name = '2018-05-18-15-06-46.fit'
filename_fit = path_data + user + f_name
ride = bikeread(filename_fit, drop_nan='columns')
print('The ride is the following:\n {}'.format(ride.head()))
print('The available data are {}'.format(ride.columns))

# ride['power'].plot(legend=True)

# df['power'] = ride['power']
# df['speed'] = ride['speed'] * 36
# power = df['power'].tolist()
# speed = df['speed'].tolist()
#  df.to_csv('data22.csv')

# l_val = df.index.tolist()
# l_val_c = l_val[0:len(power)]

ride['speed'] = ride['speed'] * 36

columns = ['power', 'speed']
ride[columns].plot(legend=True)
# plt.plot(l_val_c, power, '--r', l_val, speed, '--b')
plt.xlabel('Time')
plt.show()
