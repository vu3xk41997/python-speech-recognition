import wave

# set up audio parameters
obj = wave.open("mojito.wav", "rb")

print("Number of channels", obj.getnchannels()) # if channel > 1 audio comes from multiple directions
print("Sample width", obj.getsampwidth()) # number of bytes for each sample
print("Frame rate", obj.getframerate()) # sample frequency: sample values for each second
print("Number of frames", obj.getnframes()) # 
print("Parameters", obj.getparams())


time_audio = obj.getnframes() / obj.getframerate()
print(time_audio)

frames = obj.readframes(-1) # read all frames
print(type(frames), type(frames[0]))
print(len(frames)) # number of frames * number of channels * sample width

obj.close()

# duplicate audio file
obj_new = wave.open("mojito_new.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)

obj_new.writeframes(frames)

obj_new.close()