# from audio_extraction import extract_audio
# extract_audio("clip_3.mp4","test_audio.mp3")
# from audio import transcribe_audio
# #
# transcribe_audio("test_audio.mp3","test.txt")
from summary import generate_summary
from reader import read_text_file
test = read_text_file("test.txt")
generate_summary(test)
