import matplotlib.pyplot as plt

def multigraf(x, *Y):
    for y in Y:
        plt.plot(x, y)
        plt.show()
