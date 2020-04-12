import _init_path
from models.conv import GatedConv

# model = GatedConv.load("pretrained/gated-conv.pth")
model = GatedConv.load("pretrained/model_3.pth")

text = model.predict("./sample_audio/test.wav")

print("")
print("识别结果:")
print(text)
