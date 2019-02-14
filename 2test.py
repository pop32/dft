
import wave
import math
import numpy as np
import matplotlib.pyplot as plt



fname = "./data/1khz-6db-20sec.dat"

n0 = 0
N=2048

waveFile = wave.open(fname, 'r')
nchannles = waveFile.getnchannels()
samplewidth = waveFile.getsampwidth()
framerate = waveFile.getframerate()
nframes = waveFile.getnframes()

print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)

buf = waveFile.readframes(N)
waveFile.close()

# #print(buf)
X = np.frombuffer(buf,dtype='int16')
#print(X)
#print(len(X))
X2 = X.astype(np.int32)
X2 = ((X2[0::2] + X2[1::2]))/32768
#X2 = (X[0::2])/32768
#print(X2)
# print(X2[0::2])
# print(X2.dtype)
# left = X[0::2]
# print(left)
c = np.fft.fft(X2)[0:int(N/2)]
c = abs(c)
# # print(c)
# # print(len(c))

flist = np.fft.fftfreq(N, d=1.0/framerate)
print(flist[0:500])
# print(len(flist))

plt.subplot(2,1,1)
plt.title('data')
plt.plot(range(n0, n0+N), X2)
plt.axis()

plt.subplot(2,1,2)
plt.title('fft')
plt.plot(flist[:len(c)], c, linestyle='-')
plt.tight_layout()
plt.show()

#print(left[0])
#print(X)
#print(left)

# #print(sd)
# #ret = dft(sd)
# #for t in ret['re']:
# #    print(t)

# F = np.fft.fft(sd)

# print(F)

# waveFile.close()

