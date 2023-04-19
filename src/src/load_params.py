"""
This module load the parameters using the input file.
"""

import parameters
# import src.parameters as parameters


def load_params(filename):
    """
    This function load parameters.
    """

    # Open given file in read mode
    file = open(filename, 'r')
    param = []

    # Loop for fetching all parameters and append in the array
    for line in file:
        if line[0] == '#':
            continue
        param.append(float(line))

    # Close the read only file
    file.close()

    # Assign parameter values defined in array to the Parameter class.
    params = parameters.Parameters()
    params.a_t = param[0]
    params.t_t = param[1]
    params.t_f = param[2]
    params.e_t = param[3]
    params.a_ref = param[4]
    params.t_ref = param[5]
    params.e_ref = param[6]
    params.t_g2 = param[7]
    params.a_m = param[8]
    params.a_g1 = param[9]
    params.a_g2 = param[10]

    return params
