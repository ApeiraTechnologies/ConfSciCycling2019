import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def mse(A, B):
    mse = ((A - B)**2).mean()
    return mse


if __name__ == '__main__':

    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'UtilisateurGuillaume/'
    s_date = '2018-05-18'
    f_name = ['RT_V']

    exten = '.csv'

    df = pd.read_csv(f_path_data + f_path_user + f_name[0] + exten)

    print('Avant sorting : ', df)
    df = df.sort_values(by=['Vh'])
    print('Après sorting : ', df)

    Rab = df['Rah'].tolist()
    Vh = df['Vh'].tolist()

    Rab = np.array(Rab)
    Vh = np.array(Vh)

    Vh2 = np.power(Vh, 2)
    slope, intercept, r_value, p_value, std_err = stats.linregress(Vh2, Rab)

    Rab_fit = intercept + slope * Vh2
    mse_data = mse(Rab, Rab_fit)
    std_fit = np.std((Rab - Rab_fit))
    print("slope: %f    intercept: %f" % (slope, intercept))
    print("r-squared: %f" % r_value**2)
    plt.plot(Vh2, Rab, 'o', label='original data')
    plt.plot(Vh2, intercept + slope*Vh2, 'r', label='fitted line')
    plt.plot(Vh2, (intercept - 2*std_fit) + slope*Vh2,
             '--k', label='fit - 2 sigma')
    plt.plot(Vh2, (intercept + 2*std_fit) + slope*Vh2,
             '--k', label='fit + 2 sigma')
    plt.legend()
    plt.show()
