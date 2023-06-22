import numpy as np
from matplotlib import pyplot as plt
import scipy as sci
from scipy.fftpack import fft

nrows = 5  # number of rows
ncols = 1  # number of columns
index = 0  # index of row

x = np.linspace(0, 10 * np.pi, num=500)
#print(x)

y = []

a = 1

m = 1
y_tmp = a * np.power(np.sin(x), m)
y.append(y_tmp.tolist())
s_title =  "y = a * (sin(x) ^ m), where a={aVal}, m={mVal}".format(aVal=a, mVal=m)
#print(y[-1])

index += 1
plt.subplot(nrows,ncols,index)
plt.title(s_title)
plt.xlabel("x")
plt.plot(x, y[-1])

m = 2
y_tmp = a * np.power(np.sin(x), m)
y.append(y_tmp.tolist())
s_title =  "y = a * (sin(x) ^ m), where a={aVal}, m={mVal}".format(aVal=a, mVal=m)
#print(y[-1])

index += 1
plt.subplot(nrows,ncols,index)
plt.title(s_title)
plt.xlabel("x")
plt.plot(x, y[-1])

m = 3
y_tmp = a * np.power(np.sin(x), m)
y.append(y_tmp.tolist())
s_title =  "y = a * (sin(x) ^ m), where a={aVal}, m={mVal}".format(aVal=a, mVal=m)
#print(y[-1])

index += 1
plt.subplot(nrows,ncols,index)
plt.title(s_title)
plt.xlabel("x")
plt.plot(x, y[-1])

m = 4
y_tmp = a * np.power(np.sin(x), m)
y.append(y_tmp.tolist())
s_title =  "y = a * (sin(x) ^ m), where a={aVal}, m={mVal}".format(aVal=a, mVal=m)
#print(y[-1])

index += 1
plt.subplot(nrows,ncols,index)
plt.title(s_title)
plt.xlabel("x")
plt.plot(x, y[-1])

y_sum = np.sum(y, axis=0)
s_title =  "y_sum"

index += 1
plt.subplot(nrows,ncols,index)
plt.title(s_title)
plt.xlabel("x")
plt.plot(x, y_sum)

#print(y)

plt.tight_layout()  # automatically adjusts subplot params
plt.show()
