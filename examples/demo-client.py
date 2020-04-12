import requests
import _init_path
import feature
from record import record

server = "http://localhost:6666/recognize"

# record("record.wav", time=5)  # modify time to how long you want

f = open("4_16.wav", "rb")

files = {"file": f}

r = requests.post(server, files=files)

print("")
print("识别结果:")
print(r.text)
