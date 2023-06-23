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
from scipy import signal
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
def loop_sig(n):
    nrows = 3  # number of rows
    ncols = 1  # number of columns
    index = 0  # index of row

    a = 1
    w = 0.5

    x = np.linspace(0, 5 * (2 * np.pi), num=1000)

    sin_signal = a * np.sin(x)

    index += 1
    plt.subplot(nrows,ncols,index)
    plt.title("sin signal")
    plt.plot(x, sin_signal)

    square_signal = a * signal.square(sin_signal, w)

    index += 1
    plt.subplot(nrows,ncols,index)
    plt.title("square signal")
    plt.plot(x, square_signal)

    square_signal_fourier_series = []
    for m in range(0, n):
        one_element = 4 * a / ((2 * m + 1) * np.pi) * np.sin((2 * m + 1) * 2 * w * x)
        square_signal_fourier_series.append(one_element.tolist())
        sum = np.sum(square_signal_fourier_series, axis=0)
        square_signal_fourier_series = [sum.tolist()]

    index += 1
    s_title = "square signal composed by fourier series (n={n_val})".format(n_val=n)
    plt.subplot(nrows,ncols,index)
    plt.title(s_title)
    plt.plot(x, square_signal_fourier_series[-1])

    plt.tight_layout()  # automatically adjusts subplot params
    plt.show()

# Entry point
if __name__ == "__main__":
    parse_arguments()
    loop_sig(num_loop)
