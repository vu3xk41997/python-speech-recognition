from api import *
# pip3 install streamlit
import streamlit as st

# create frontend with streamlit
st.title("Welcome to my podcast summaries creating application")
episode_id = st.sidebar.text_input("Please enter an episode id:")
button = st.sidebar.button("Get podcast summary!", on_click=save_transcript, args={episode_id,})

def get_clean_time(start_ms):
    seconds = int((start_ms/1000) % 60)
    minutes = int((start_ms/(1000 * 60)) % 60)
    hours = int((start_ms/(1000 * 60 * 60)) % 24)
    if hours > 0:
        start_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        start_time = f'{minutes:02d}:{seconds:02d}'

    return start_time


if button:
    filename = episode_id + '_chapters.json'
    with open(filename, 'r') as f:
        data = json.load(f)

        chapters = data['chapters']
        podcast_title = data['podcast_title']
        episode_title = data['episode_title']
        thumbnail = data['episode_thumbnail']


    st.header(f'{podcast_title} - {episode_title}')
    st.image(thumbnail)
    for chp in chapters:
        with st.expander(chp['gist'] + '-' + get_clean_time(chp['start'])):
            chp['summary']


# save_transcript('71de733737a74d4994b0d4d58ebbeafe')
