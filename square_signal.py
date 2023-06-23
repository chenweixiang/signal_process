#
# square signal
#
# python3 square_signal.py -n [<num_loop>]
# where, <num_loop> = 1, 2, ..,
# <num_loop> = 1 by default.
#

import argparse

import numpy as np
from matplotlib import pyplot as plt
import scipy as sci
from scipy.fftpack import fft

num_loop = 1

# Parse input arguments
def parse_arguments():
    # Parse arguments
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-n", "--num_loop", help="Number of loops")
    args = parser.parse_args()
    
    # -n, --num_loop
    global num_loop
    if args.num_loop:
        num_loop = int(args.num_loop)

# max = 1, 2, ..
def loop_sin(n):
    a = 1
    w = 0.5
    x = np.linspace(0, 10 * np.pi, num=1000)
    y = []
    for m in range(0, n):
        one_sin = 4 * a / np.pi / (2 * m + 1) * np.sin((2 * m + 1) * w * x)
        y.append(one_sin.tolist())
        sum = np.sum(y, axis=0)
        y = [sum.tolist()]

    s_title = "square signal, n={n_val}".format(n_val=n)
    plt.title(s_title)
    plt.xlabel("x")
    plt.plot(x, y[-1])

    plt.tight_layout()  # automatically adjusts subplot params
    plt.show()

# Entry point
if __name__ == "__main__":
    parse_arguments()
    loop_sin(num_loop)

