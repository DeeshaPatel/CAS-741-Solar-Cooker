# from src import parameters
import src.parameters as parameters


def load_params(filename):
    # Open given file in read mode
    f = open(filename, 'r')
    param = []

    # Loop for fetching all parameters and append in the array
    for line in f:
        if line[0] == '#':
            continue
        else:
            param.append(float(line))

    # Close the read only file
    f.close()

    # Assign parameter values defined in array to the Parameter class.
    params = parameters.Parameters()
    params.A_t = param[0]
    params.T_t = param[1]
    params.T_f = param[2]
    params.e_t = param[3]
    params.A_ref = param[4]
    params.T_ref = param[5]
    params.e_ref = param[6]
    params.T_g2 = param[7]
    params.A_m = param[8]
    params.A_g1 = param[9]
    params.A_g2 = param[10]

    return params
