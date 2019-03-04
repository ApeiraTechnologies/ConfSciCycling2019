import numpy as np


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
