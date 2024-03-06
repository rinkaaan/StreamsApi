import whisper
from whisper.utils import WriteSRT

modelSize = "large"
mp3 = "tbs mar 05 14 59 58.mp3"

print("Loading Whisper model: " + modelSize + " ...")
model = whisper.load_model(modelSize)

print("Transcribing...")
result = model.transcribe(mp3)

print(f"Saving srt ...")
writer = WriteSRT(".")
writer(result, mp3)
