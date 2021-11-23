import numpy as np
import pyaudio
import pydub

SAMPLING_RATE=44100

def play(s: pyaudio.Stream, freq:float,duration:float):
    samples=np.sin(np.arange(int(duration*SAMPLING_RATE))*freq*np.pi*2/SAMPLING_RATE)
    s.write(samples.astype(np.float32).tostring())
    
    
p=pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1,rate=SAMPLING_RATE,frames_per_buffer=1024,output=True)
play(stream,261.626,0.3)
play(stream,329.628,0.3)
play(stream,391.995,0.3)
play(stream,523.251,0.6)

stream.close()
p.terminate()

