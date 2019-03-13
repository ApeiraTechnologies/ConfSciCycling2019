# from skcycling.io import bikeread
import matplotlib.pyplot as plt
import pandas as pd


path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
# user = 'UtilisateurCedric/'
# user = 'UtilisateurGuillaume/'
# user = 'UtilisateurDenis/'
user = 'UtilisateurAurel/'
f_name = 'recup_data_aurel.csv'
filename_fit = path_data + user + f_name
df = pd.read_csv(filename_fit)

# ride['power'].plot(legend=True)

# df['power'] = ride['power']
# df['speed'] = ride['speed'] * 36
# power = df['power'].tolist()
# speed = df['speed'].tolist()
#  df.to_csv('data22.csv')

# l_val = df.index.tolist()
# l_val_c = l_val[0:len(power)]

df['speed'] = df['speed'] * 36
speed = df['speed'].tolist()
power = df['power'].tolist()

val_x = []
for i in range(len(speed)):
    val_x.append(i)

plt.plot(val_x, power, '--r', val_x, speed, '--b')
plt.xlabel('Time')
plt.show()
