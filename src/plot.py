import matplotlib.pyplot as plt

def plot_result(t, x, Ef):
    plt.subplot(121)
    plt.semilogy(t, x[:, 0], label='Reflector')
    plt.semilogy(t, x[:, 1], label="Fluid")
    plt.legend()
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")
    plt.subplot(122)
    plt.semilogy(t, Ef, label='Reflector')
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Temperature (c) ")
    plt.legend()
    plt.tight_layout()
    plt.show()
