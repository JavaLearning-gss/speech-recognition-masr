
import os
from tqdm import tqdm
import json


def traverse_file_path(root_path):
    sub_dirs=os.listdir(root_path)
    list_paths=[]
    for sub_dir in tqdm(sub_dirs):
        sub_path=os.path.join(root_path,sub_dir)
        sub_path_files=os.listdir(sub_path)
        for sub_file in sub_path_files:
            file_path=os.path.join(sub_path,sub_file)
            list_paths.append(file_path)
    return list_paths

def path_to_dict(list_paths):
    dict_paths={}
    for path in tqdm(list_paths):
        key=path.split('/')[-1]
        value=path
        dict_paths[key]=value
    return dict_paths

def get_transcript(transcript):
    transcript_path=os.path.join(transcript,'aishell_transcript_v0.8.txt')
    with open(transcript_path) as f:
        list_data=f.readlines()

    return list_data

def output_to_file(save_file_name,audio_files,list_trns):
    with open(save_file_name,'w') as f:
        for audio,trn in zip(audio_files,list_trns):
            f.write(audio+','+trn+'\n')

if __name__ == "__main__":
    root_path='/Users/admin/Documents/data'
    data_aishell=os.path.join(root_path,'data_aishell')
    
    train_path=os.path.join(data_aishell,'wav/train/')
    dev_path=os.path.join(data_aishell,'wav/dev/')
    test_path=os.path.join(data_aishell,'wav/test/')

    list_train_paths=traverse_file_path(train_path)
    list_dev_paths=traverse_file_path(dev_path)
    list_test_paths=traverse_file_path(test_path)

    list_paths=list_train_paths+list_dev_paths+list_test_paths

    dict_paths=path_to_dict(list_paths)
    transcript=os.path.join(data_aishell,'transcript')
    list_data=get_transcript(transcript)

    audio_files=[]
    list_trns=[]
    for item in tqdm(list_data):
        audio_file,trn=item.strip().split(" ", 1)
        key_path=audio_file+'.wav'
        audio_files.append(dict_paths[key_path])
        list_trns.append(trn)
    


    output_to_file('data/train_data_aishell.index',audio_files,list_trns)

    word_dict=['_']
    for trn in tqdm(list_trns):
        text_words=[item for item in trn if item!=' ']
        word_dict.extend(text_words)
    
    word_dict=list(set(word_dict))

    with open("./data/labels.json","w") as f:
        json.dump(word_dict,f,ensure_ascii=False)

    