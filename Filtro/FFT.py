import numpy as np
from scipy.fft import fft, ifft
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd

y = pd.read_csv('feeds.csv', usecols=['field1'])
y = np.array(y[100:len(y)], dtype=np.float)
# Number of sample points
N = len(y)

# sample spacing
T = 30
x = np.linspace(0.0, N * T, N)
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N)

# Filter
#b, a = signal.butter(8, 0.01)
#y_filter = signal.filtfilt(b, a, y, padlen=0)
#yf_filter = fft(y_filter)

y_filter = yf
y_filter[N // 2: N] = 0
yf_filter = ifft(y_filter)

# Plot
plt.figure(1)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N]), 'k-', label='Signal')
plt.plot(xf, 2.0 / N * np.abs(yf_filter[0:N]), 'b-', label='Filtered')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Hz')
plt.ylabel('|Y|')

plt.figure(2)
plt.plot(np.array(y, dtype=np.float), 'k-', label='Signal')
plt.plot(y_filter, 'b-', label='Filtered')
plt.legend(loc='best')
plt.grid()
plt.ylabel('Temperature (ºC)')

plt.show()
