# example.py
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)
'''
audio_url = (
    "https://storage.googleapis.com/eleven-public-cdn/audio/marketing/nicole.mp3"
)
response = requests.get(audio_url)
audio_data = BytesIO(response.content)
'''

file_path = "iusong.mp4"  # 같은 폴더에 있는 파일 이름
with open(file_path, "rb") as f:
    audio_data = BytesIO(f.read())




transcription = elevenlabs.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v1", # Model to use, for now only "scribe_v1" is supported
    tag_audio_events=True, # Tag audio events like laughter, applause, etc.
    language_code="kor", # Language of the audio file. If set to None, the model will detect the language automatically.
    diarize=True, # Whether to annotate who is speaking
)

# print(transcription)
print(transcription.text) 