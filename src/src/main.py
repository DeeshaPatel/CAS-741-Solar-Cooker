"""
This module provides the SCEC main module functionalities.
"""

from scipy.integrate import odeint
import numpy as np
import load_params
import calculation
import verify_params
import plot
import energy_calculation


# Load input file
FILENAME = 'test.in'
params = load_params.load_params(FILENAME)

# Verify inputs are valid or not
verify_params.verify_input(params)

# Set initial temperature value of the
# reflector, fluid, glass2, lid, and glass1
init_temp = [params.t_ref,
             params.t_f,
             params.t_g2,
             params.t_t,
             params.t_g2]

# declare a time vector (time window)
time_vector = np.arange(0, 3600, 60)

# calculate temperature using the function
calc_temp = odeint(calculation.calculate_temp,
                   init_temp, time_vector, args=(params,))

# calculate energy of fluid
eF = energy_calculation.energywat(calc_temp[:, 1], params.t_f)

# Plot the result
plot.plot_result(time_vector, calc_temp, eF)
