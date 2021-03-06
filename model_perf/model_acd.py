import numpy as np


def Rt_from_Pt(power, speed):
    Rt = []

    for i in range(len(power)):
        pi = power[i]
        vi = speed[i]
        temp = pi/vi
        Rt.append(temp)

    return Rt


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


def f_apeira_correction(p, v, m, Cr, debug=False):
    G = 9.81
    A = Cr * m * G
    D = m
    N = len(p)
    v_t0 = v[0]
    v_f = v[len(v)-1]
    power = np.array(p)
    speed = np.array(v)
    alpha = np.zeros(N)
    beta = v_f-v_t0

    for i in range(N):
        alpha[i] = power[i] / speed[i]

    f_average = np.mean(alpha) - A - (D / N * beta)

    if debug:
        print('Moyenne force : ', f_average)
        print('Moyenne Alpha : ', np.mean(alpha))
        print('A : ', A)
        print('D/N * Beta : ', D/N * beta)

    return f_average


def ACd_apeira_correction(p, v, m, Cr, pressure, T, debug=False):
    G = 9.81
    A = Cr * m * G
    D = m
    N = len(p)
    power = np.array(p)
    speed = np.array(v)
    alpha = np.zeros(N)
    acc = np.zeros(N)
    beta = np.zeros(N)

    for i in range(N):
        if i == 0:
            acc[i] = speed[i+1] - speed[i]
        else:
            acc[i] = speed[i] - speed[i-1]

    for i in range(N):
        alpha[i] = power[i] / (speed[i] * speed[i] * speed[i])
        beta[i] = (A + D * acc[i]) / (speed[i] * speed[i])

    ACd_average = (np.sum(alpha) / N) - (np.sum(beta) / N)
    ACd_average = ACd_average * 2 / (rho(pressure, T))

    if debug:
        print('ACd moyen : ', ACd_average)

    return ACd_average
