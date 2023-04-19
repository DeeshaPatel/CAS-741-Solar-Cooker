"""
This module calculates the energy of fluid.
"""

import constant


def energywat(twat, temp_fluid):
    """
    This function calculates the energy of fluid.
    """
    ewat = []
    for temp in twat:
        ewat = ewat + [constant.C_F * constant.M_F
                       * (temp - temp_fluid)]

    return ewat
