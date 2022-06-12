# python-speech-recognition
Speech recognition course from freecodecamp

## Projects
1. Audio Process Basics
    * duplicate .wav file
    * plot .wav file using matplotlib and numpy
    * record .wav file with microphone using pyaudio
    <code>brew install portaudio</code>
    * edit .wav file and convert to .mp3 file
    <code>brew install ffmpeg</code>
2. Audio Recognition
    * signup on assemblyAI and get API key
    * developers > documentation
    * upload local file
    * get transcribe id
    * poll with transcribe id
    * return status
    * save transcript if process completed
3. Sentiment Analysis
    * api.py is basiclly the same as api_communication.py in previous project
    * api key is needed
    * import youtube_dl 
    <code>pip3 install youtube-dl</code>
    * with youtube_dl, we extract video info and retrieve audio url
    * save transcript using audio url and save sentiment analysis as .json file
    * count the number of "positive", "negative", and "neutral"
    * calculate positive ratio ignoring "neutral"