import math
import numpy as np
import constant


def calculate_temp(temp, t, params):
    # Calculate temperature inside the box
    params.T_int2 = (temp[2] + temp[3] + temp[0]) / 3

    # Solar Radiation over glass 1
    q1 = params.A_g1 * constant.G * constant.alpha_g1

    # Heat flow radiation of glass 2 toward glass 1
    q2 = params.A_g1 * constant.stefan_const * constant.e_g * (temp[2] ** 4
                                                               - temp[4] ** 4)

    # Heat flow convection of glass 1 toward the inner 1
    q3 = params.A_g2 * constant.h_g1_int1 * (temp[2] - temp[4])

    # Heat flow radiation of glass 1 toward the sky
    q4 = params.A_g1 * constant.stefan_const * constant.e_g * (temp[4] ** 4
                                                               - (0.0552 *
                                                                  constant.
                                                                  T_amb
                                                                  ** 1.5) ** 4)

    # Heat flow convection of glass 1 toward the ambient
    q5 = params.A_g1 * constant.h_g1_amb * (temp[4] - constant.T_amb)

    # Heat flow convection of glass 2 toward the inner 1
    q6 = params.A_g2 * constant.h_g2_int1 * (temp[2] - temp[4])

    # Heat flow radiation from the recipient lid toward glass 2
    q7 = params.A_t * constant.stefan_const * params.e_t * (temp[3] ** 4
                                                            - temp[2] ** 4)

    # Heat flow convection of the inner 2 toward glass 2
    q8 = params.A_g2 * constant.h_g2_int1 * (params.T_int2 - temp[2])

    # Heat flow convection of inner 2 toward the lid
    q9 = params.A_t * constant.h_t_int2 * (temp[3] - params.T_int2)

    # Heat flow radiation for the sun and absorbed by the lid
    q10 = params.A_t * constant.G * math.pow(constant.t_g, 2) * constant.\
        alpha_t

    # Heat flow convection of the lid toward the inner 3
    q11 = params.A_t * constant.h_t_int3 * (temp[3] - temp[1])

    # Heat flow radiation of the lid of the recipient toward the fluid
    q12 = params.A_t * constant.stefan_const * params.e_t * (temp[3] ** 4
                                                             - temp[1] ** 4)

    # Heat flow convection of recipient to the inner 2
    q13 = params.A_ref * constant.h_ref_int2 * (params.T_int2 - temp[0])

    # Heat flow reflection of incident radiation on the reflector
    q14 = constant.p * params.A_ref * constant.G * math.pow(constant.t_g,
                                                            2) * math.\
        cos(90 - constant.theta_ref)

    # Heat flow radiation of recipient toward glass 2
    q15 = params.A_ref * constant.stefan_const * params.e_ref * (temp[0] **
                                                                 4 - temp[2]
                                                                 ** 4)

    # Heat flow radiation of recipient toward the fluid
    q16 = params.A_ref * constant.stefan_const * params.e_ref * (temp[0] **
                                                                 4 - temp[1]
                                                                 ** 4)

    # Heat flow convection of recipient toward the fluid
    q17 = params.A_m * constant.h_ref_f * (temp[0] - temp[1])

    # Balance of energy for glass 1
    dg1dt = q1 + q2 - q3 - q4 - q5 / (800 * 0.00000000725)

    # Balance of energy for glass 2
    dg2dt = constant.t_g * q1 - q2 - q6 + q7 + q8 + q15 / (800 * 0.00000000725)

    # Balance of energy in the lid of the recipient
    dtdt = -q7 + q9 + q10 - q11 - q12 / (900 * 0.1)

    # Balance of energy on the recipient
    drdt = (q13 + 4 * q14 - q15 - q16 - q17) / (constant.m_r * constant.c_r)

    # Energy balance for the fluid
    dfdt = (q11 + q12 + q16 + q17) / (constant.m_f * constant.c_f)

    # print('g1', dg1dt, 'g2', dg2dt, 't', dtdt, 'r', drdt, 'f', dfdt)

    return np.array([drdt, dfdt, dg2dt, dtdt, dg1dt])
