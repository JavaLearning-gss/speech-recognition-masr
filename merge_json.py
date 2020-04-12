import os
import json

def read_data(labels_path):
    with open(labels_path) as f:
       labels = json.load(f)
    return labels

def output_word_json(json_path,dict_word):
    word_dict=['_']
    word_dict.extend(dict_word)
    with open(json_path,"w") as f:
        json.dump(word_dict,f,ensure_ascii=False)

if __name__ == "__main__":
    root_path='./data'
    path_files=os.listdir(root_path)

    labels_path=[item for item in path_files if item.split('.')[-1]=='json']

    list_files=[]
    for item in labels_path:
        label_path=os.path.join(root_path,item)
        labels=read_data(label_path)
        # print(len(idx))
        list_files.extend(labels)

    list_files=list(set(list_files))
    print(len(list_files))
    print(list_files[:10])

    output_word_json('labels.json',list_files)