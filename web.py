import streamlit as st
from audio_extraction import extract_audio
from edit import extract_random_clips
from audio import transcribe_audio
from reader import read_text_file
from summary import generate_summary



st.title('Automatic shorts and content producer')
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
if uploaded_file is not None:
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
st.video("temp_video.mp4")

if st.button('Extract Clips'):
    with st.spinner('Extracting clips...'):
        clips = extract_random_clips("temp_video.mp4", num_clips=3, clip_duration=60)
        st.success('Clips extracted successfully!')
        extract_audio("clip_1.mp4","clip_1.mp3")
        extract_audio("clip_2.mp4","clip_2.mp3")
        extract_audio("clip_3.mp4","clip_3.mp3")
        transcribe_audio("clip_1.mp3","content1.txt")
        transcribe_audio("clip_2.mp3","content2.txt")
        transcribe_audio("clip_3.mp3","content3.txt")
        clip1 = read_text_file("content1.txt")
        clip2 = read_text_file("content2.txt")
        clip3 = read_text_file("content3.txt")
        st.video("clip_1.mp4")
        st.text(clip1)
        st.video("clip_2.mp4")
        st.text(clip2)
        st.video("clip_3.mp4")
        st.text(clip3)
