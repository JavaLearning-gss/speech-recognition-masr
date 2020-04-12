import os
from tqdm import tqdm
import json
import pandas as pd

def traverse_file_path(root_path):
    sub_dirs=os.listdir(root_path)
    sub_dirs=[item for item in sub_dirs if item.split('.')[-1]!='gz']
    list_paths=[]
    for sub_dir in tqdm(sub_dirs):
        sub_path=os.path.join(root_path,sub_dir)
        sub_path_files=os.listdir(sub_path)
        for sub_file in sub_path_files:
            file_path=os.path.join(sub_path,sub_file)
            list_paths.append(file_path)
    return list_paths

def get_file_map(file_path):
    dict_data={}
    with open(file_path) as f:
        data=f.readlines()
    for item in data:
        file,path=item.strip().split('\t')
        dict_data[file]=path
    return dict_data

def get_transcript(txt_paths):
    dict_trans={}
    data=pd.read_csv(txt_paths,sep='\t')
    list_keys=data['UtteranceID'].tolist()
    list_trans=data['Transcription'].tolist()
    for key,value in zip(list_keys,list_trans):
        dict_trans[key]=value
    return dict_trans

def output_to_file(save_file_name,dict_audio,dict_trans):
    with open(save_file_name,'w') as f:
        for key,value in dict_trans.items():
            audio=os.path.join(MAGICDATA_Mandarin_Chinese_Speech,dict_audio[key])
            trn=value
            f.write(audio+','+trn+'\n')

if __name__ == "__main__":
    root_path='/home/wugaosheng/data'
    MAGICDATA_Mandarin_Chinese_Speech=os.path.join(root_path,'MAGICDATA_Mandarin_Chinese_Speech')

    test_file=os.path.join(MAGICDATA_Mandarin_Chinese_Speech,'test.scp')
    test_dict_data=get_file_map(test_file)

    train_file=os.path.join(MAGICDATA_Mandarin_Chinese_Speech,'train.scp')
    train_dict_data=get_file_map(train_file)

    dev_file=os.path.join(MAGICDATA_Mandarin_Chinese_Speech,'dev.scp')
    dev_dict_data=get_file_map(dev_file)

    dict_merge={}
    dict_merge.update(test_dict_data)
    dict_merge.update(train_dict_data)
    dict_merge.update(dev_dict_data)
    print(len(train_dict_data))
    print(len(dev_dict_data))
    print(len(test_dict_data))
    sum_data=len(train_dict_data)+len(dev_dict_data)+len(test_dict_data)
    print(sum_data)
    print(len(dict_merge))

    trans_path=os.path.join(MAGICDATA_Mandarin_Chinese_Speech,'TRANS.txt')
    dict_trans=get_transcript(trans_path)
    print(len(dict_trans))

    output_to_file('data/train_MAGICDATA_Mandarin_Chinese_Speech.index',dict_merge,dict_trans)
    # print(test_dict_data['38_5716_20170914202341.wav'])

    word_dict=['_']
    for trn in tqdm(dict_trans.values()):
        text_words=[item for item in trn if item!=' ']
        word_dict.extend(text_words)

    with open("./data/MAGICDATA_labels.json","w") as f:
        json.dump(word_dict,f,ensure_ascii=False)


