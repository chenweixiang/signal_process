import argparse

import numpy as np
from matplotlib import pyplot as plt
import scipy as sci
from scipy.fftpack import fft

max_loop = 1

# Parse input arguments
def parse_arguments():
    # Parse arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-m", "--max", help="Maximum loop")
    args = parser.parse_args()
    
    # -m, --max
    global max_loop
    if args.max:
        max_loop = int(args.max)

# max = 1, 2, ..
def loop_sin(max):
    w = 0.5
    x = np.linspace(0, 10 * np.pi, num=500)
    y = []
    for m in range(0, max):
        one_sin = 4 / np.pi / (2 * m + 1) * np.sin((2 * m + 1) * w * x)
        y.append(one_sin.tolist())
        sum = np.sum(y, axis=0)
        y = [sum.tolist()]

    plt.title("square signal")
    plt.xlabel("x")
    plt.plot(x, y[-1])

    plt.tight_layout()  # automatically adjusts subplot params
    plt.show()

# Entry point
if __name__ == "__main__":
    parse_arguments()
    loop_sin(max_loop)

