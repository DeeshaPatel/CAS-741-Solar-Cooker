import matplotlib.pyplot as plt


def plot_result(t, temp, ef):

    # plot the result of temperature reflector and fluid
    plt.subplot(121)
    plt.semilogy(t, temp[:, 0], label='Reflector')
    plt.semilogy(t, temp[:, 1], label="Fluid")
    plt.legend()
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")

    # plot the result for energy of fluid
    plt.subplot(122)
    plt.semilogy(t, ef, label='Fluid')
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")
    plt.legend()
    plt.tight_layout()
    plt.savefig("test.png")
    plt.show()
