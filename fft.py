import numpy as np
from matplotlib import pyplot as plt
import scipy as sci
from scipy.fftpack import fft

fs = 100 # 采样率
N = 256 # 数据点数
n = np.linspace(0, N-1, N)
print(n)

t = n / fs #时间序列
print(t)

x = 0.5 * np.sin(2 * np.pi * 15 * t) + 2 * np.sin(2 * np.pi * 40 * t) #实信号

y1 = sci.fft.fft(x, N) #信号傅立叶变换
y2 = sci.fft.fftshift(y1)

mag1 = abs(y1) #对信号取模求振幅
mag2 = abs(y2)

f1 = n * fs / N #频率序列
f2 = n * fs / N - fs/2

nrows = 3
ncols = 1
index = 0

index += 1
plt.subplot(nrows,ncols,index)
plt.title("Usual FFT")
plt.xlabel("Freq/Hz")
plt.ylabel("Amp")
plt.plot(f1, mag1) #随频率变化的振幅

index += 1
plt.subplot(nrows,ncols,index)
plt.title("FFT without fftshift")
plt.xlabel("Freq/Hz")
plt.ylabel("Amp")
plt.plot(f2, mag1) #随频率变化的振幅

index += 1
plt.subplot(nrows,ncols,index)
plt.title("FFT after fftshift")
plt.xlabel("Freq/Hz")
plt.ylabel("Amp")
plt.plot(f2, mag2) #随频率变化的振幅

plt.tight_layout() #自动调整子图间距
plt.show()
