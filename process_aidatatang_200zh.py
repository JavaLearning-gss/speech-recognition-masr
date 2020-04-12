import os
from tqdm import tqdm
import json

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

def get_transcript(txt_paths):
    list_trns=[]
    for item in tqdm(txt_paths):
        with open(item) as f:
            text=f.readline().strip()
            list_trns.append(text)
    return list_trns

def output_to_file(save_file_name,audio_files,list_trns):
    with open(save_file_name,'w') as f:
        for audio,trn in zip(audio_files,list_trns):
            f.write(audio+','+trn+'\n')

if __name__ == "__main__":
    root_path='/home/wugaosheng/data'
    aidatatang_200zh=os.path.join(root_path,'aidatatang_200zh')

    train_path=os.path.join(aidatatang_200zh,'corpus/train')
    dev_path=os.path.join(aidatatang_200zh,'corpus/dev/')
    test_path=os.path.join(aidatatang_200zh,'corpus/test/')

    list_train_paths=traverse_file_path(train_path)
    list_dev_paths=traverse_file_path(dev_path)
    list_test_paths=traverse_file_path(test_path)

    list_paths=list_train_paths+list_dev_paths+list_test_paths

    # print(len(list_dev_paths))
    # print(list_dev_paths[:5])

    wav_paths=[path for path in list_paths if path.split('.')[-1]=='wav']
    txt_paths=[path for path in list_paths if path.split('.')[-1]=='txt']
    print(len(wav_paths))
    print(len(txt_paths))
    list_trns=get_transcript(txt_paths)
    print(len(list_trns))

    output_to_file('data/train_aidatatang_200zh.index',wav_paths,list_trns)

    word_dict=['_']
    for trn in tqdm(list_trns):
        text_words=[item for item in trn if item!=' ']
        word_dict.extend(text_words)
    
    word_dict=list(set(word_dict))

    with open("./data/aidatatang_labels.json","w") as f:
        json.dump(word_dict,f,ensure_ascii=False)


