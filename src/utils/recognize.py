import io

import speech_recognition as sr
from pydub import AudioSegment


def recognize_audio(audio: bytes) -> str:
    audio_file = io.BytesIO(audio)
    audio_segment = AudioSegment.from_file(audio_file)
    wav_io = io.BytesIO()

    audio_segment.export(wav_io, format="wav")
    wav_io.seek(0)

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_io) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Failed to recognize audio"
    except sr.RequestError:
        return "Recognition service error"
