import requests
import json
from api_secrets import API_KEY_ASSEMBLYAI
import time


upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY_ASSEMBLYAI}

# upload local file to assemblyAI
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url'] # extract url from response
    return audio_url

# transcribe
def transcribe(audio_url, sentiment_analysis):
    transcribe_request = {
        "audio_url": audio_url,
        "sentiment_analysis": sentiment_analysis
    }
    transcribe_response = requests.post(transcript_endpoint, json=transcribe_request, headers=headers)
    job_id = transcribe_response.json()['id']
    return job_id

# poll
def poll(transcribe_id):
    polling_endpoint = transcript_endpoint + '/' + transcribe_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcribe_result_url(audio_url, sentiment_analysis):
    transcribe_id = transcribe(audio_url, sentiment_analysis)
    while True:
        data = poll(transcribe_id)
        if data['status'] == "completed":
            return data, None
        elif data['status'] == "error":
            return data, data['error']
        
        print("waiting 30 seconds..")
        time.sleep(30)


# save transcript
def save_transcript(audio_url, title, sentiment_analysis=False):
    data, error = get_transcribe_result_url(audio_url, sentiment_analysis)

    if data:
        filename = title + ".txt"
        with open(filename, "w") as f:
            f.write(data['text'])
        
        if sentiment_analysis:   
            filename = title + '_sentiments.json'
            with open(filename, "w") as f:
                sentiments = data["sentiment_analysis_results"]
                json.dump(sentiments, f, indent=4)
        print("Transcript saved!!")
        return True
    elif error:
        print("Error!!", error)
        return False