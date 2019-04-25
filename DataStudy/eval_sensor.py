import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def find_best_shift(pref, po, max_shift):
    l_diff = []
    for i in range(max_shift):
        po_sh = np.roll(po, i)
        y1 = po_sh[i:]
        y2 = pref[i:]
        l_diff.append(np.sum((y1-y2)**2))
    mini = l_diff[0]
    indx_mini = 0
    for i in range(max_shift):
        if l_diff[i] < mini:
            mini = l_diff[0]
            indx_mini = i

    return indx_mini, l_diff


def clean_pic(p1, p2, thresold):
    p1_c = []
    p2_c = []

    for i in range(len(p1)):
        if p1[i] < thresold and p2[i] < thresold:
            p1_c.append(p1[i])
            p2_c.append(p2[i])

    p1_c = np.array(p1_c)
    p2_c = np.array(p2_c)

    return p1_c, p2_c


if __name__ == '__main__':
    f_path_data = '/home/cedric/Documents/Ergocycle/data/DataEstACd/20180515/'
    f_path_user = 'TestCapteur/'
    f_name = ['ValRaw']
    exten = '.csv'

    df = pd.read_csv(f_path_data + f_path_user + f_name[0] + exten)

    pref = df['inpower'].tolist()
    po = df['powertap'].tolist()

    po = np.array(po)
    pref = np.array(pref)

    # find best shift

    delta, l_diff = find_best_shift(po, pref, 10)
    pref = np.roll(pref, delta-2)
    po_s = po[delta:]
    pref_s = pref[delta:]
    print("Best shift : ", delta)

    t_index = np.linspace(0, len(po_s), len(po_s))
    plt.figure(1)
    plt.plot(t_index, po_s, 'r', label="inpower(celui de Bourges)")
    plt.plot(t_index, pref_s, 'y', label="powertap")
    plt.legend()

    # po_c, pref_c = clean_pic(po_s, pref_s, 360)
    po_c = po_s
    pref_c = pref_s
    sorted_idx = np.argsort(pref_c)

    pref_sort = pref_c[sorted_idx]
    po_sort = po_c[sorted_idx]

    ypredict = np.zeros(len(pref_sort))
    slope, intercept, r_value, p_value, std_err = stats.linregress(pref_sort,
                                                                   po_sort)

    for i in range(len(po_sort)):
        ypredict[i] = intercept + pref_sort[i] * slope

    std_model = np.std(po_sort - ypredict)

    print("R2 : ", r_value**2)
    print("p value : ", p_value)
    print("Slope : ", slope)
    print("Intercept : ", intercept)

    plt.figure(0)
    plt.plot(pref_sort, po_sort, 'o', label='raw data')
    plt.plot(pref_sort, ypredict, 'r', label='model')
    plt.plot(pref_sort, (intercept + 2 * std_model) + pref_sort * slope, '--y',
             label='+2 sigma')
    plt.plot(pref_sort, (intercept - 2 * std_model) + pref_sort * slope, '--b',
             label='-2 sigma')
    plt.legend()

    plt.show()
