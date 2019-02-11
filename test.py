
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

fname = "./data/test.wav"

n0 = 52188
N=256

waveFile = wave.open(fname, 'r')
nchannles = waveFile.getnchannels()
samplewidth = waveFile.getsampwidth()
framerate = waveFile.getframerate()
nframes = waveFile.getnframes()

print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)

buf = waveFile.readframes(n0)
buf = waveFile.readframes(N)
# #print(buf)
#X = np.frombuffer(buf,dtype='int16')/32768.0
X = np.frombuffer(buf,dtype='int16')
print(np.get_printoptions())
X2=X[0]/32768.0
print(X[0])
print(X2)
print(X[0].tobytes().hex())
print(X2.tobytes().hex())
print(buf[0:2].hex())
print(type(X[0]))
# left = X[0::2]
# print(left)
# c = np.fft.fft(left)
# c = abs(c)
# print(c)
waveFile.close()

#flist = np.fft.fftfreq(N, d=1.0/framerate)
#print(flist)

# plt.subplot(2,1,1)
# plt.title('data')
# plt.plot(range(n0, n0+N), left)
# plt.axis()

# plt.subplot(2,1,2)
# plt.title('frequency spectrum')
# plt.plot(flist, c, marker='o', linestyle='-')
# plt.tight_layout()
# plt.show()

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

