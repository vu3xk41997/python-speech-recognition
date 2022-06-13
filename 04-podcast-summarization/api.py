import requests
import json
from api_secrets import API_KEY_ASSEMBLYAI, API_KEY_LISTENNOTES
import time
import pprint


transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
assemblyai_headers = {'authorization': API_KEY_ASSEMBLYAI}

listennotes_episode_endpoint = "https://listen-api.listennotes.com/api/v2/episodes"
listennotes_headers = {'X-ListenAPI-Key': API_KEY_LISTENNOTES}

# get episode information
def get_episode_audio_url(episode_id):
    url = listennotes_episode_endpoint + '/' + episode_id
    response = requests.request('GET', url, headers=listennotes_headers)

    data = response.json()
    # pprint.pprint(data)

    audio_url = data['audio']
    episode_thumbnail = data['thumbnail']
    podcast_title = data['podcast']['title']
    episode_title = data['title']

    return audio_url, episode_thumbnail, episode_title, podcast_title

# transcribe
def transcribe(audio_url, auto_chapters):
    transcribe_request = {
        "audio_url": audio_url,
        "auto_chapters": auto_chapters
    }
    transcribe_response = requests.post(transcript_endpoint, json=transcribe_request, headers=assemblyai_headers)
    job_id = transcribe_response.json()['id']
    return job_id

# poll
def poll(transcribe_id):
    polling_endpoint = transcript_endpoint + '/' + transcribe_id
    polling_response = requests.get(polling_endpoint, headers=assemblyai_headers)
    return polling_response.json()

def get_transcribe_result_url(audio_url, auto_chapters):
    transcribe_id = transcribe(audio_url, auto_chapters)
    while True:
        data = poll(transcribe_id)
        if data['status'] == "completed":
            return data, None
        elif data['status'] == "error":
            return data, data['error']
        
        print("waiting 60 seconds..")
        time.sleep(60)


# save transcript
def save_transcript(episode_id):
    audio_url, episode_thumbnail, episode_title, podcast_title = get_episode_audio_url(episode_id)
    data, error = get_transcribe_result_url(audio_url, auto_chapters = True)

    pprint.pprint(data)

    if data:
        filename = episode_id + ".txt"
        with open(filename, "w") as f:
            f.write(data['text'])

        chapters_filename = episode_id + '_chapters.json'
        with open(chapters_filename, "w") as f:
            chapters = data['chapters']

            episode_data = {'chapters': chapters}
            episode_data['episode_thumbnail'] = episode_thumbnail
            episode_data['episode_title'] = episode_title
            episode_data['podcast_title'] = podcast_title

            json.dump(episode_data, f)
            print("Transcript saved!!")
        return True
    elif error:
        print("Error!!", error)
        return False