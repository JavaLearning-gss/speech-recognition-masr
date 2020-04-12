from web_vad import read_wave,frame_generator,vad_collector,write_wave
import webrtcvad
import os
from models.conv import GatedConv
import beamdecode

def clear_output_dir(path):
    """
     clear files in a path
    """
    print('clear exist files')
    for i in os.listdir(path):
        path_file=os.path.join(path,i)
        if(os.path.isfile(path_file)):
            os.remove(path_file)

def vad_split(audio_file,output_dir):
    audio, sample_rate = read_wave(audio_file)
    vad = webrtcvad.Vad(2)
    frames = frame_generator(30, audio, sample_rate)
    frames = list(frames)
    segments = vad_collector(sample_rate, 30, 300, vad, frames)
    for i, segment in enumerate(segments):
        path=os.path.join(output_dir,'chunk-%003d.wav')
        path = path % (i,)
        print(' Writing %s' % (path,))
        write_wave(path, segment, sample_rate)

def masr_recognize(audio_path):
    audio_files=os.listdir(audio_path)
    list_texts={}
    for path in audio_files:
        audio_file=os.path.join(audio_path,path)
        # text = model.predict(audio_file)
        text=beamdecode.predict(audio_file)
        list_texts[path]=text

    return list_texts

if __name__ == "__main__":
    audio_file='./sample_audio/duihua_sample.wav'
    output_dir='data_vad'
    clear_output_dir(output_dir)
    vad_split(audio_file,output_dir)

    # model = GatedConv.load("pretrained/gated-conv.pth")
    dict_texts=masr_recognize(output_dir)
    print(dict_texts)
