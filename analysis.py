import matplotlib.pyplot as plt


def show():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    frequency = range(len(alphabet))
    plt.plot(alphabet, frequency)
    plt.show()
