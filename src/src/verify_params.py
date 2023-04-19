"""
This module is used to verify inputs.
"""


def verify_input(params):
    """
    This method is used to verify inputs using params input.
    """
    if params.a_t <= 0:
        raise ValueError('Area of lid must be > 0 \n')
    if params.a_ref <= 0:
        raise ValueError('Area of reflector must be > 0 \n')
    if params.a_m <= 0:
        raise ValueError('Area of mass must be > 0 \n')
    if params.a_t >= 20:
        raise ValueError('Area of lid must be between 0 to 20 \n')
    if params.a_ref >= 20:
        raise ValueError('Area of reflector must be between 0 to 20 \n')
    if params.a_m >= 20:
        raise ValueError('Area of mass must be between 0 to 20 \n')
    if params.a_g1 <= 0:
        raise ValueError('Area of glass 1 must be > 0 \n')
    if params.a_g2 <= 0:
        raise ValueError('Area of glass 2 must be > 0 \n')
    if params.a_g1 > 5:
        raise ValueError('Area of glass 1 must be between 0 to 5 \n')
    if params.a_g2 > 5:
        raise ValueError('Area of glass 2 must be between 0 to 5 \n')
    if params.t_t <= 0:
        raise ValueError('Temperature of lid must be > 0 \n')
    if params.t_f <= 0:
        raise ValueError('Temperature of fluid must be > 0 \n')
    if params.t_ref <= 0:
        raise ValueError('Temperature of reflector must be > 0 \n')
    if params.t_g2 <= 0:
        raise ValueError('Temperature of glass 2 must be > 0 \n')
    if params.t_t >= 45:
        raise ValueError('Excess temperature value of lid \n')
    if params.t_f >= 45:
        raise ValueError('Excess temperature value of fluid \n')
    if params.t_ref >= 45:
        raise ValueError('Excess temperature value of reflector \n')
    if params.t_g2 >= 45:
        raise ValueError('Excess temperature value of glass 2 \n')
    if (params.e_t <= 0) or (params.e_t >= 1):
        raise ValueError('The given input of emissivity must be between '
                         '0 and 1 \n')
    if (params.e_ref <= 0) or (params.e_ref >= 1):
        raise ValueError('The given input of emissivity must be between '
                         '0 and 1 \n')
