
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

def Make_graphs():
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
    X = np.frombuffer(buf,dtype='int16')
    X2 = X.astype(np.int32)
    X2 = ((X2[0::2] + X2[1::2]))/32768
    c = np.fft.fft(X2)[0:int(N/2)]
    c = abs(c)
    flist = np.fft.fftfreq(N, d=1.0/framerate)

    re.cla()
    re.plot(flist[:len(c)], c, linestyle='-')
    canvas.draw()

Make_graphs()
root.mainloop()
