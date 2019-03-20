import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


if __name__ == '__main__':

    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurCedric/'
    s_date = '2018-05-18'
    f_name = ['RT_V']

    exten = '.csv'

    df = pd.read_csv(f_path_data + f_path_user + f_name[0] + exten)

    Rab = df['Rab'].tolist()
    Vh = df['Vb'].tolist()

    Rab = np.array(Rab)
    Vh = np.array(Vh)

    Vh2 = np.power(Vh, 2)
    slope, intercept, r_value, p_value, std_err = stats.linregress(Vh2, Rab)
    print("slope: %f    intercept: %f" % (slope, intercept))
    print("r-squared: %f" % r_value**2)
    plt.plot(Vh2, Rab, 'o', label='original data')
    plt.plot(Vh2, intercept + slope*Rab, 'r', label='fitted line')
    plt.legend()
    plt.show()
