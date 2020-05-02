import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import pandas as pd

y = pd.read_csv('feeds.csv', usecols=['field1'])
y = np.array(y[len(y)//2:], dtype=np.float)
# Number of sample points
N = len(y)

# sample spacing
T = 30
f = 1/T
x = np.linspace(0.0, N*T/60, N)

# FFT
yf = fft(y)
xf = np.linspace(0.0, f/2, N//2)

# Moving Average
alfa = 0.9
ym = np.empty([N,1])
ym[0] = y[0]
ym[1] = y[1]
for i in range(2,N):
    ym[i] = (y[i] + y[i-1] + y[i-2])/3

ymf = fft(ym)


fig1 = plt.figure()

plt.subplot(2, 2, 1)
plt.title('Temperatura')
plt.plot(x,y)
plt.xlabel('Tempo (min)')
plt.ylabel('T (ºC)')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(xf, 1.0/N * np.abs(yf[:N//2]))
plt.title('FFT')
plt.xlabel('Freq (Hz)')
plt.ylabel('|T|')
plt.grid()

plt.subplot(2, 2, 3)
plt.title('Temperatura -  MV')
plt.plot(x,ym)
plt.xlabel('Tempo (min)')
plt.ylabel('T (ºC)')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(xf, 1.0/N * np.abs(ymf[:N//2]))
plt.title('FFT - MV')
plt.xlabel('Freq (Hz)')
plt.ylabel('|T|')
plt.grid()

plt.show()




