
import wave
import math
import numpy as np
import matplotlib.pyplot as plt



fname = "./data/Kalimba.wav"

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

#waveFile.readframes(1534900)
#waveFile.readframes(300)
buf = waveFile.readframes(N)
print(len(buf))
print(waveFile.tell())

waveFile.close()



