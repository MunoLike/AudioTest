import numpy as np
import pyaudio
import pydub
from pydub import AudioSegment
import wave

sound = AudioSegment.from_mp3(r".\audrey_164.mp3")
#inp=sound.get_array_of_samples()
print(sound.array_type)
# p=pyaudio.PyAudio()
# stream = p.open(rate, channels, format)

