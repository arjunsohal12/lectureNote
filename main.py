import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import os


def get_text(video_file_name):
    # Get the mp4 file, and set the name for transcribed speech
    transcribed_audio_file_name = "transcribed_speech.wav"

    # Transcribe the speech, and write to the name we want
    audioclip = AudioFileClip(video_file_name)
    audioclip.write_audiofile(transcribed_audio_file_name)

    with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    total_duration = math.ceil(duration / 60)

    r = sr.Recognizer()

    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i * 60, duration=60)
        f = open("transcription.txt", "a")
        transcription = r.recognize_google(audio)
        print(transcription)
        f.write(transcription)
        f.write(" ")
    f.close()

get_text("psychLec02.mp4")
