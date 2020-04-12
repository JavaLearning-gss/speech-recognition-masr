
import os
from sklearn.model_selection import train_test_split

def read_data(index_path):
    with open(index_path) as f:
        idx = f.readlines()
    # idx = [x.strip().split(",", 1) for x in idx]
    return idx

def split_data(list_files,test_size=0.3):
    X_train, X_test= train_test_split(list_files, test_size=test_size, random_state=42)
    return X_train,X_test

def output_to_file(save_file_name,list_files):
    with open(save_file_name,'w') as f:
        for item in list_files:
            f.write(item)

if __name__ == "__main__":
    root_path='./data'
    path_files=os.listdir(root_path)

    index_paths=[item for item in path_files if item.split('.')[-1]=='index']
    list_files=[]
    for item in index_paths:
        index_path=os.path.join(root_path,item)
        idx=read_data(index_path)
        # print(len(idx))
        list_files.extend(idx)
    print(len(list_files))
    train,test=split_data(list_files)
    print(len(train))
    print(len(test))
    output_to_file('train.index',train)
    output_to_file('dev.index',test)
