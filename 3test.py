
import wave
import math
import numpy as np
import matplotlib.pyplot as plt

n0 = 0
freq=42000
N=256

flist = np.fft.fftfreq(N, d=1.0/freq)
print(flist[0:50])
