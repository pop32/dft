
import wave
import math
import numpy as np
import matplotlib.pyplot as plt

fname = "./data/Kalimba.wav"
N=2048
OVERLAP=int(N/2)
window = np.hamming(N)
print("---- fft info ----")
print("N :", N)
print("OVERLAP :", OVERLAP)
print("window :", window)

waveFile = wave.open(fname, 'r')
nchannles = waveFile.getnchannels()
samplewidth = waveFile.getsampwidth()
framerate = waveFile.getframerate()
nframes = waveFile.getnframes()
flist = np.fft.fftfreq(N, d=1.0/framerate)

print("---- wave info ----")
print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)

# test --------------------------------------- 
print(flist[:467])
# buf = waveFile.readframes(OVERLAP)
# X = np.frombuffer(buf,dtype='int16')
# #print(X[0:100])

# buf = waveFile.readframes(OVERLAP)
# X = np.frombuffer(buf,dtype='int16')
# X = ((X[0::2]*0.5)+(X[1::2]*0.5))/32768.0
# print(X[0:5])

# windowbuf = np.zeros(N)

# windowbuf = np.roll(windowbuf, -OVERLAP)
# windowbuf[OVERLAP:] = X
# windowedbuf = windowbuf * window
# #print(windowbuf[0:100])
# print(windowedbuf[0:10])

# buf = waveFile.readframes(OVERLAP)
# X = np.frombuffer(buf,dtype='int16')
# X = ((X[0::2]*0.5)+(X[1::2]*0.5))/32768.0
# print(X[0:5])

# windowbuf = np.roll(windowbuf, -OVERLAP)
# windowbuf[OVERLAP:] = X
# windowedbuf = windowbuf * window
# #print(windowedbuf[0:100])
# print(windowedbuf[0:10])

windowX=np.zeros(N)
buf = waveFile.readframes(OVERLAP)
X = np.frombuffer(buf,dtype='int16')
X = ((X[0::2]*0.5)+(X[1::2]*0.5))/32768.0
windowX = np.roll(windowX, -OVERLAP)
windowX[OVERLAP:] = X
windowd_X = windowX * window

c = np.fft.fft(windowd_X)[0:int(N/2)]
c = abs(c)

waveFile.close()

plt.figure(figsize=(13, 3))
plt.subplot(1,1,1)
plt.title('fft')
plt.tight_layout()
plt.plot(flist[:500], c[:500], linestyle='-')
plt.ylim(0,1)
plt.show()

exit()


# test --------------------------------------- 

plt.subplot(2,1,2)
plt.title('fft')
plt.tight_layout()

readend=False
readlen=0
pos=0
windowX=np.zeros(N)
while not readend:
    buf = waveFile.readframes(OVERLAP)
    X = np.frombuffer(buf,dtype='int16')
    X = ((X[0::2]*0.5)+(X[1::2]*0.5))/32768.0
    windowX = np.roll(windowX, -OVERLAP)
    windowX[OVERLAP:] = X
    windowd_X = windowX * window

    c = np.fft.fft(windowd_X)[0:int(N/2)]
    c = abs(c)

    plt.plot(flist[:len(c)], c, linestyle='-')
    if nframes <= waveFile.tell():
        readend=True
    else:
        readlen = waveFile.tell()-pos
        pos = pos + readlen

waveFile.close()