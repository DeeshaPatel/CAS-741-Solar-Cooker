import scipy.integrate
import numpy as np
import math


def func_t_r(x0, t, params):
    stefan_const = 5.669 * math.pow(10, -8)
    h_t_int3 = 4.2
    h_ref_int2 = 4.4
    h_ref_f = 3.8
    c_r = 900
    c_f = 600
    m_f = 0.4
    m_r = 0.2
    G = 1000
    p = 0.89
    t_g = 0.48

    q11 = params.A_t * h_t_int3 * (params.T_t - x0[1])
    q12 = params.A_t * stefan_const * params.e_t * (math.pow(params.T_t, 4) - math.pow(x0[1], 4))
    q13 = params.A_ref * h_ref_int2 * params.T_int2
    q14 = p * params.A_ref * G * t_g * math.cos(90 - params.theta_ref)
    q15 = params.A_ref * stefan_const * params.e_ref * (math.pow(x0[0], 4) - math.pow(params.T_g2, 4))
    q16 = params.A_ref * stefan_const * params.e_ref * (math.pow(x0[0], 4) - math.pow(x0[1], 4))
    q17 = params.A_m * h_ref_f * (x0[0] - x0[1])

    dr = (-q13 + 4 * q14 - q15 - q16 - q17) / (m_r * c_r)
    df = (q11 + q12 + q16 + q17) / (m_f * c_f)
    print(dr, df)

    return dr, df
