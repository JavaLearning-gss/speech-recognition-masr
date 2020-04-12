import requests
import _init_path
import feature
from record import record
import os
server = "http://localhost:6666/recognize"

# record("record.wav", time=5)  # modify time to how long you want
root_dir='audios'
audio_files=os.listdir(root_dir)
for audio in audio_files:
    audio_path=os.path.join(root_dir,audio)
    f = open(audio_path, "rb")

    files = {"file": f}

    r = requests.post(server, files=files)

    print("")
    print("识别结果:")
    print(r.text)
