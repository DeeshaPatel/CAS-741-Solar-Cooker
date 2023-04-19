"""
This module is used to plot the result.
"""

import matplotlib.pyplot as plt


def plot_result(time, temp, energy):
    """
    This method is used to plot the result using inputs.
    """

    # plot the result of temperature reflector and fluid
    plt.subplot(121)
    plt.semilogy(time, temp[:, 0], label='Reflector')
    plt.semilogy(time, temp[:, 1], label="Fluid")
    plt.legend()
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")

    # plot the result for energy of fluid
    plt.subplot(122)
    plt.semilogy(time, energy, label='Fluid')
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")
    plt.legend()
    plt.tight_layout()
    plt.savefig("test.png")
    plt.show()
