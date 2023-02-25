import load_params
import calculation
import numpy as np
from scipy.integrate import odeint
import plot
import energy_calculation

# Load file having input parameters
filename = 'text.in'
params = load_params.load_params(filename)

# set initial condition
x0 = [30, 30]

# declare a time vector (time window)
t = np.linspace(0, 100, 50000)

# call the function
x = odeint(calculation.func_t_r, x0, t, args=(params,))

Ef = energy_calculation.energyWat(x[:, 1])

# Plot the result
plot.plot_result(t, x, Ef)


