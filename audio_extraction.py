from moviepy.editor import VideoFileClip

mp4_file = "temp_video.mp4"
mp3_file = "temp_audio.mp3"


def extract_audio(mp4_file, mp3_file):
    video_clip = VideoFileClip(mp4_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    video_clip.close()
    print("Audio extraction successful!")
