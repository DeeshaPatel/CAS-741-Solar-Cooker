import constant


def energywat(twat, temp_fluid):
    ewat = []
    for temp in twat:
        ewat = ewat + [constant.c_f * constant.m_f
                       * (temp - temp_fluid)]

    return ewat
