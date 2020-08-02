import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import pandas as pd

y = pd.read_csv('feeds.csv', usecols=['field1'])
y = np.array(y[len(y)//2:], dtype=np.float)
# Number of sample points
N = len(y)

# sample spacing
T = 60
f = 1/T
x = np.linspace(0.0, N*T/60, N)

# FFT
yf = fft(y)
xf = np.linspace(0.0, f/2, N//2)

# Moving Average
alfa = np.array([0.4, 0.3, 0.3])
ym = np.empty([N,1])
ord = 2

for i in range(0,ord):
    ym[i] = y[i]

for i in range(2,N):
    y_ar = np.array([y[i], ym[i-1], ym[i-2]])
    ym[i] = alfa.dot(y_ar)

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




