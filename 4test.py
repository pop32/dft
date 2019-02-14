
import wave
import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk

#import matplotlib.pyplot as plt

# n0 = 0
# freq=42000
# N=256

# flist = np.fft.fftfreq(N, d=1.0/freq)
# print(flist[0:50])


root = Tk.Tk()
F = Figure(figsize=(6, 3), dpi=100)
re = F.add_subplot(1,1,1)
canvas = FigureCanvasTkAgg(F, master=root)
canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=0)
canvas._tkcanvas.pack(side=Tk.TOP, expand=0)

fname = "./data/Kalimba.wav"
N=2048

waveFile = wave.open(fname, 'r')
nchannles = waveFile.getnchannels()
samplewidth = waveFile.getsampwidth()
framerate = waveFile.getframerate()
nframes = waveFile.getnframes()
flist = np.fft.fftfreq(N, d=1.0/framerate)

print("Channel num : ", nchannles)
print("Sample width : ", samplewidth)
print("Sampling rate : ", framerate)
print("Frame num : ", nframes)


def Make_graphs():
    buf = waveFile.readframes(N)
    X = np.frombuffer(buf,dtype='int16')
    X2 = X.astype(np.int32)
    X2 = ((X2[0::2] + X2[1::2]))/32768
    c = np.fft.fft(X2)[0:int(N/2)]
    c = abs(c)

    re.cla()
    re.plot(flist[:len(c)], c, linestyle='-')
    re.set_ylim([0,1000])
    canvas.draw()
    if nframes > waveFile.tell():
        root.after(33, Make_graphs)
    else:
        waveFile.close()

Make_graphs()
root.mainloop()
