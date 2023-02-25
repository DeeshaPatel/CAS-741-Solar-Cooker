def energyWat(tWat):
    c_f = 600
    m_f = 0.4
    eWat = []
    for temp in tWat:
        eWat = eWat + [c_f * m_f * (temp - 30)]

    return eWat