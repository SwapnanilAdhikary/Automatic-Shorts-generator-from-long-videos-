from summary import generate_summary
from reader import read_text_file

sum = read_text_file("transcription.txt")

generate_summary(sum)