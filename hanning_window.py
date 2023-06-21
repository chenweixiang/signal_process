import matplotlib.pyplot as plt
import scipy.signal as sgn
import numpy as np

plt.rc('axes', unicode_minus=False)
plt.figure(num=3)
han = sgn.hann(41)
plt.plot(han)
plt.title('Hanning')
plt.show()