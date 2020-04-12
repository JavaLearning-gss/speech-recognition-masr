# import _init_path
from models.conv import GatedConv

# model = GatedConv.load("pretrained/gated-conv.pth")
# model = GatedConv.load("pretrained/model_62.pth")
model = GatedConv.load("pretrained2/model_81.pth")

text = model.predict("./sample_audio/8_16.wav")

print("")
print("识别结果:")
print(text)
