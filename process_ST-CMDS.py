import os
from tqdm import tqdm
import json

def read_trn(file_path):
    with open(file_path,'r') as f:
        text=f.readline().strip()
    return text

def output_to_file(save_file_name,audio_files,list_trns):
    with open(save_file_name,'w') as f:
        for audio,trn in zip(audio_files,list_trns):
            f.write(audio+','+trn+'\n')

def output_word_json(json_path,list_trns):
    word_dict=['_']
    for trn in tqdm(list_trns):
        text_words=[item for item in trn if item!=' ']
        word_dict.extend(text_words)
    
    word_dict=list(set(word_dict))

    with open(json_path,"w") as f:
        json.dump(word_dict,f,ensure_ascii=False)

if __name__ == "__main__":
    root_path='/home/wugaosheng/data'
    ST_CMDS=os.path.join(root_path,'ST-CMDS-20170001_1-OS')
    audio_files=os.listdir(ST_CMDS)
    audio_files=[item for item in audio_files if item.split('.')[-1]=='wav']
    audio_files=[os.path.join(ST_CMDS,item) for item in audio_files]

    list_trns=[]
    for item in tqdm(audio_files):
        item=item.split('.')[0]+'.txt'
        file_path=os.path.join(ST_CMDS,item)
    #     print(file_path)
        text=read_trn(file_path)
        list_trns.append(text)
    
    output_to_file('data/train_ST_CMDS.index',audio_files,list_trns)

    json_path="./data/ST_CMDS_labels.json"
    output_word_json(json_path,list_trns)

    
