
import wave
import math
import numpy as np
import matplotlib.pyplot as plt

def dft(rd):
    ret={}
    ret_re=[]
    ret_im=[]
    n = len(rd)
    for i in range(n):
        re = 0.0
        im = 0.0
        for j in range(n):
            re = re + (rd[j] * math.cos(2*math.pi*j*i/n))
            im = im + (-rd[j] * math.cos(2*math.pi*j*i/n))
        ret_re.append(re)
        ret_im.append(im)

    ret['re'] = ret_re
    ret['im'] = ret_im
    return ret

fname = "./data/test_10kHz.wav"

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
# #print(buf)
X = np.frombuffer(buf,dtype='int16')/32768.0
#print(X)
# left = X[0::2]
# print(left)
c = np.fft.fft(X)[0:int(N/2)]
c = abs(c)
print(c)
print(len(c))
waveFile.close()

flist = np.fft.fftfreq(N, d=1.0/framerate)
print(flist)
print(len(flist))

plt.subplot(2,1,1)
plt.title('data')
plt.plot(range(n0, n0+N), X)
#plt.axis()

plt.subplot(2,1,2)
plt.title('fft')
#plt.set_xlim(0, flist[:len(c)])
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

