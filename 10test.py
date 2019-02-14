import pyaudio
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40

p = pyaudio.PyAudio()

for i in range(0, p.get_device_count()):
    #print(i, p.get_device_info_by_index(i)['name'])
    if type(p.get_device_info_by_index(i)['name']) == bytes:
        print(i, p.get_device_info_by_index(i)['name'].decode('sjis'))
    elif type(p.get_device_info_by_index(i)['name']) == str:
        print(i, p.get_device_info_by_index(i)['name'])

device_index = int(input('Device index: '))
if device_index is None:
    exit()

print(device_index)

recording = True

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=device_index)

print("*recording")

root = Tk.Tk()
F = Figure(figsize=(13, 3), dpi=100)
re = F.add_subplot(1,1,1)
canvas = FigureCanvasTkAgg(F, master=root)
canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=0)
canvas._tkcanvas.pack(side=Tk.TOP, expand=0)
flist = np.fft.fftfreq(CHUNK, d=1.0/RATE)

call_t = time.time()
def Make_graphs():
    global call_t

    #print("call_t:{}".format(time.time() - call_t))
    #proc_t1 = proc_t2 = proc_t3 = call_t = time.time()

    data  = stream.read(CHUNK)
    X = np.frombuffer(data,dtype='int16')/32768.0
    #print(len(X))
    c = np.fft.fft(X)[:int(CHUNK/2)]
    c = abs(c)
    #print("proc_t3:{}".format(time.time() - proc_t3))

    re.cla()
    re.plot(flist[:100], c[:100], linestyle='-')
    re.set_ylim([0,50])
    #print("proc_t2:{}".format(time.time() - proc_t2))

    canvas.draw()

    #print("proc_t1:{}".format(time.time() - proc_t1))
    root.after(1, Make_graphs)

Make_graphs()
root.mainloop()

p.terminate()

