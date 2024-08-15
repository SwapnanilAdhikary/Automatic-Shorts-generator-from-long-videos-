import whisper


def transcribe_audio(audio_file, transcription_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    with open(transcription_file,"w") as f:
        f.write(result["text"])








