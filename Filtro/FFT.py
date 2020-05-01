import numpy as np
from scipy.fft import fft, ifft
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd

y = pd.read_csv('feeds.csv', usecols=['field1'])
y = np.array(y, dtype=np.float)
# Number of sample points
N = len(y)

# sample spacing
T = 30
x = np.linspace(0.0, N * T, N)
yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N)


