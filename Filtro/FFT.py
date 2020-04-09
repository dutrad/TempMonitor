import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
import csv

with open('feeds.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# Number of sample points
N = len(data)
# sample spacing
T = 30
x = np.linspace(0.0, N * T, N)
y = data
yf = fft(y)

xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)

# Plot
plt.figure(1)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.grid()

plt.figure(2)
plt.plot(np.array(y, dtype=np.float))
plt.grid()
plt.show()
