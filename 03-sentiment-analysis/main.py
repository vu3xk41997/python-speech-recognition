import json
from yt_extractor import get_audio_url, get_video_infos
from api import save_transcript

def save_vedio_sentiments(url):
    video_infos = get_video_infos(url)
    audio_url = get_audio_url(video_infos)
    title = video_infos["title"]
    title = title.strip().replace(" ", "_")
    title = "data/" + title
    save_transcript(audio_url, title, sentiment_analysis=True)

if __name__ == "__main__":
    # save_vedio_sentiments("https://www.youtube.com/watch?v=e-kSGNzu0hM")

    with open("data/iPhone_13_Review:_Pros_and_Cons_sentiments.json", "r") as f:
        data = json.load(f)

    positives = []
    negatives = []
    neutrals = []

    # categorizing texts
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)

    n_pos = len(positives)
    n_neg = len(negatives)
    n_neut = len(neutrals)

    print("Number of positives:", n_pos)
    print("Number of negatives:", n_neg)
    print("Number of neutrals:", n_neut)

    # ignore neutrals here
    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:.3f}")