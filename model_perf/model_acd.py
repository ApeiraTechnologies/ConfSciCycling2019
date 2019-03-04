import numpy as np


def est_wind(p1, p2, v1, v2):
    v1_ms = v1 / 3.6
    v2_ms = v2 / 3.6

    f1 = p1/v1
    f2 = p2/v2
    s_f1 = np.sqrt(f1)
    s_f2 = np.sqrt(f2)

    v_wind = ((s_f1) * v2_ms) - ((s_f2) * v1_ms) / (s_f1 + s_f2)
    return v_wind


def inv_model_grappe_ACd(power, v, va, temperature, pressure, cr, m):
    G = 9.81
    val_rho = rho(pressure, temperature)
    A = cr * m * G
    B = 0.5 * val_rho

    ACd = (power - v * A) / (B * (v + va)**2 * v)

    return ACd


def rho(P, T):
    T_c = T + 273.15
    P_kPa = P / 10
    P_mmHg = P_kPa / 0.133322
    rho_0 = 1.27
    val_rho = rho_0 * (P_mmHg / 760) * (273 / T_c)

    return val_rho


def inv_model_grappe_F(power, v, cr, m):
    G = 9.81
    A = cr * m * G

    f_aero = ((power/v) - A)

    return f_aero
