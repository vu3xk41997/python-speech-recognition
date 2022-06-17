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
4. Podcast Summarization
    * similar api as previous project
    * signup on Listennotes and get API key
    * search for certain episode and fetch api of that episode (right side of the screen after scrolling down)
    * get episode information and save transcription
    * import streamlit to build frontend UI
    <code>pip3 install streamlit</code>
    * create frontend UI with streamlit
    * calculate start time of each chapter
    * run streamlit in terminal
    <code>streamlit run main.py</code>
    * search with episode id
    * it might take a while to retrieve information
5. Real-time Recognition with OpenAi
    * upgrade assemblyAi to paid account
    * same api_secrets as previous project
    * signup on openAi and get api key
    * import websockets
    <code>pip3 install websockets</code>
    * import openai
    <code>pip3 install openai</code>
    * setup microphone using source code from project one
    * get url from assemblyAi real-time speech recognition blog
    * sending and receiving data with async
    * get ask_computer source code from openAi exemples > Q&A