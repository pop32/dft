import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40

p = pyaudio.PyAudio()

for i in range(0, p.get_device_count()):
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

data  = stream.read(CHUNK)
print(len(data))

data  = stream.read(CHUNK)
print(len(data))

p.terminate()

