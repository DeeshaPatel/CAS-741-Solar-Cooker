"""
This module provides the original function to the ODE
for calculating temperature.
"""

import math
import numpy as np
from src import constant


def calculate_temp(temp, time, params):
    """
    This method calculate the temperature using initial temp,
    time and extra parameters.
    """

    # Calculate temperature inside the box
    params.t_int2 = (temp[2] + temp[3] + temp[0]) / 3

    # Solar Radiation over glass 1
    q_1 = params.a_g1 * constant.G * constant.ALPHA_G1

    # Heat flow radiation of glass 2 toward glass 1
    q_2 = params.a_g1 * constant.STEFAN_CONST * constant.E_G * (temp[2] ** 4 -
                                                                temp[4] ** 4)

    # Heat flow convection of glass 1 toward the inner 1
    q_3 = params.a_g2 * constant.H_G1_INT1 * (temp[2] - temp[4])

    # Heat flow radiation of glass 1 toward the sky
    q_4 = params.a_g1 * constant.STEFAN_CONST * constant.E_G * (temp[4] ** 4 -
                                                                (0.0552 *
                                                                 constant.
                                                                 T_AMB ** 1.5)
                                                                ** 4)

    # Heat flow convection of glass 1 toward the ambient
    q_5 = params.a_g1 * constant.H_G1_AMB * (temp[4] - constant.T_AMB)

    # Heat flow convection of glass 2 toward the inner 1
    q_6 = params.a_g2 * constant.H_G2_INT1 * (temp[2] - temp[4])

    # Heat flow radiation from the recipient lid toward glass 2
    q_7 = params.a_t * constant.STEFAN_CONST * params.e_t * (temp[3] ** 4
                                                            - temp[2] ** 4)

    # Heat flow convection of the inner 2 toward glass 2
    q_8 = params.a_g2 * constant.H_G2_INT1 * (params.t_int2 - temp[2])

    # Heat flow convection of inner 2 toward the lid
    q_9 = params.a_t * constant.H_T_INT2 * (temp[3] - params.t_int2)

    # Heat flow radiation for the sun and absorbed by the lid
    q_10 = params.a_t * constant.G * math.pow(constant.T_G, 2) * constant.\
        ALPHA_T

    # Heat flow convection of the lid toward the inner 3
    q_11 = params.a_t * constant.H_T_INT3 * (temp[3] - temp[1])

    # Heat flow radiation of the lid of the recipient toward the fluid
    q_12 = params.a_t * constant.STEFAN_CONST * params.e_t * (temp[3] ** 4 -
                                                              temp[1] ** 4)

    # Heat flow convection of recipient to the inner 2
    q_13 = params.a_ref * constant.H_REF_INT2 * (params.t_int2 - temp[0])

    # Heat flow reflection of incident radiation on the reflector
    q_14 = constant.P * params.a_ref * constant.G * math.pow(constant.T_G,
                                                            2) * math.\
        cos(90 - constant.THETA_REF)

    # Heat flow radiation of recipient toward glass 2
    q_15 = params.a_ref * constant.STEFAN_CONST * params.e_ref * (temp[0] **
                                                                 4 - temp[2]
                                                                 ** 4)

    # Heat flow radiation of recipient toward the fluid
    q_16 = params.a_ref * constant.STEFAN_CONST * params.e_ref * (temp[0] **
                                                                 4 - temp[1]
                                                                 ** 4)

    # Heat flow convection of recipient toward the fluid
    q_17 = params.a_m * constant.H_REF_F * (temp[0] - temp[1])

    # Balance of energy for glass 1
    dg1dt = q_1 + q_2 - q_3 - q_4 - q_5 / (800 * 0.00000000725)

    # Balance of energy for glass 2
    dg2dt = constant.T_G * q_1 - q_2 - q_6 + q_7 + q_8 + q_15 / (800 * 0.00000000725)

    # Balance of energy in the lid of the recipient
    dtdt = -q_7 + q_9 + q_10 - q_11 - q_12 / (900 * 0.1)

    # Balance of energy on the recipient
    drdt = (q_13 + 4 * q_14 - q_15 - q_16 - q_17) / (constant.M_R * constant.C_R)

    # Energy balance for the fluid
    dfdt = (q_11 + q_12 + q_16 + q_17) / (constant.M_F * constant.C_F)

    # print('g1', dg1dt, 'g2', dg2dt, 't', dtdt, 'r', drdt, 'f', dfdt)

    return np.array([drdt, dfdt, dg2dt, dtdt, dg1dt])
