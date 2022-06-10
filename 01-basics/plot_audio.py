import wave
import matplotlib.pyplot as plt
import numpy as np


# set up audio parameters
obj = wave.open("mojito.wav", "rb")

sample_freq = obj.getframerate()
num_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

time_audio = num_samples / sample_freq

print(time_audio)

# plot audio
signal_array = np.frombuffer(signal_wave, dtype = np.int16)

times = np.linspace(0, time_audio, num = num_samples)

plt.figure(figsize = (15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, time_audio)
plt.show()