from api_communication import *

filename = "../01-basics/output.wav"

audio_url = upload(filename)
save_transcript(audio_url)