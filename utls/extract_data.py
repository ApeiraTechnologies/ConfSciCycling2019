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


def extract_cedric_data(f_name):
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


def extract_with_pandas(f_name):
    # version specifique data Cedric
    df = pd.read_csv(f_name)

    l_25hv = df['25hv'].astype(float)
    l_25hp = df['25hp'].astype(float)
    l_30hv = df['30hv'].astype(float)
    l_30hp = df['30hp'].astype(float)
    l_35hv = df['35hv'].astype(float)
    l_35hp = df['35hp'].astype(float)
    l_40hv = df['40hv'].astype(float)
    l_40hp = df['40hp'].astype(float)

    l_25pv = df['25pv'].astype(float)
    l_25pp = df['25pp'].astype(float)
    l_30pv = df['30pv'].astype(float)
    l_30pp = df['30pp'].astype(float)
    l_35pv = df['35pv'].astype(float)
    l_35pp = df['35pp'].astype(float)
    l_40pv = df['40pv'].astype(float)
    l_40pp = df['40pp'].astype(float)

    l_25bv = df['25bv'].astype(float)
    l_25bp = df['25bp'].astype(float)
    l_30bv = df['30bv'].astype(float)
    l_30bp = df['30bp'].astype(float)
    l_35bv = df['35bv'].astype(float)
    l_35bp = df['35bp'].astype(float)
    l_40bv = df['40bv'].astype(float)
    l_40bp = df['40bp'].astype(float)

    l_25hv_m = np.mean(l_25hv)
    l_25hp_m = np.mean(l_25hp)
    l_30hv_m = np.mean(l_30hv)
    l_30hp_m = np.mean(l_30hp)
    l_35hv_m = np.mean(l_35hv)
    l_35hp_m = np.mean(l_35hp)
    l_40hv_m = np.mean(l_40hv)
    l_40hp_m = np.mean(l_40hp)

    l_25pv_m = np.mean(l_25pv)
    l_25pp_m = np.mean(l_25pp)
    l_30pv_m = np.mean(l_30pv)
    l_30pp_m = np.mean(l_30pp)
    l_35pv_m = np.mean(l_35pv)
    l_35pp_m = np.mean(l_35pp)
    l_40pv_m = np.mean(l_40pv)
    l_40pp_m = np.mean(l_40pp)

    l_25bv_m = np.mean(l_25bv)
    l_25bp_m = np.mean(l_25bp)
    l_30bv_m = np.mean(l_30bv)
    l_30bp_m = np.mean(l_30bp)
    l_35bv_m = np.mean(l_35bv)
    l_35bp_m = np.mean(l_35bp)
    l_40bv_m = np.mean(l_40bv)
    l_40bp_m = np.mean(l_40bp)

    l_power = [l_25hp_m, l_30hp_m, l_35hp_m, l_40hp_m,
               l_25pp_m, l_30pp_m, l_35pp_m, l_40pp_m,
               l_25bp_m, l_30bp_m, l_35bp_m, l_40bp_m]

    l_speed = [l_25hv_m, l_30hv_m, l_35hv_m, l_40hv_m,
               l_25pv_m, l_30pv_m, l_35pv_m, l_40pv_m,
               l_25bv_m, l_30bv_m, l_35bv_m, l_40bv_m]

    return l_power, l_speed
