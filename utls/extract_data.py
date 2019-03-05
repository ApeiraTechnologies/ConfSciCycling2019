import numpy as np
import pandas as pd


def extract_from_int(power, speed, l_d_int, l_f_int):

    nb_sec_d = []
    nb_sec_f = []

    l_speed = []
    l_power = []

    for i in range(len(l_d_int)):
        nb_sec_d.append(l_d_int[i][0] * 3600 + l_d_int[i][1] * 60
                        + l_d_int[i][2])

        nb_sec_f.append(l_f_int[i][0] * 3600 + l_f_int[i][1] * 60
                        + l_d_int[i][2])

    for ind, elt in enumerate(nb_sec_d):
        pos = elt

        ech_speed = []
        ech_power = []

        while pos <= nb_sec_f[ind]:
            ech_power.append(power[pos])
            ech_speed.append(speed[pos])
            pos += 1

        l_speed.append(ech_speed)
        l_power.append(ech_power)

    return l_power, l_speed


def create_visu_vec(size, nb_sec_d, nb_sec_f):

    vis_int = np.zeros(size)

    for ind, elt in enumerate(nb_sec_d):
        pos = elt

        while pos <= nb_sec_f[ind]:
            vis_int[pos] = 800
            pos += 1

    return vis_int


def extract_with_pandas(f_name):
    # version specifique data Cedric
    df = pd.read_csv(f_name)
    l_25hv = df['25hv'].astype(float)
    l_25hp = df['25hp'].astype(float)
    l_35hv = df['35hv'].astype(float)
    l_35hp = df['35hp'].astype(float)
    l_25bv = df['25bv'].astype(float)
    l_25bp = df['25bp'].astype(float)
    l_35bv = df['35bv'].astype(float)
    l_35bp = df['35bp'].astype(float)

    l_25hv_m = np.mean(l_25hv)
    l_25hp_m = np.mean(l_25hp)
    l_35hv_m = np.mean(l_35hv)
    l_35hp_m = np.mean(l_35hp)
    l_25bv_m = np.mean(l_25bv)
    l_25bp_m = np.mean(l_25bp)
    l_35bv_m = np.mean(l_35bv)
    l_35bp_m = np.mean(l_35bp)

    l_power = [l_25hp_m, l_35hp_m, l_25bp_m, l_35bp_m]
    l_speed = [l_25hv_m, l_35hv_m, l_25bv_m, l_35bv_m]

    return l_power, l_speed
