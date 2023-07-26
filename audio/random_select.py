import os
import numpy as np

def read_list(fname):
    result = []
    with open(fname, "r") as f:
        for each in f.readlines():
            each = each.strip('\n')
            result.append(each)
    return result

def write_list(list, fname):
    with open(fname,'w') as f:
        for word in list:
            f.write(word)
            f.write('\n')

audio_folder = "/mnt/bn/lqhaoheliu/hhl_script2/2023/make_an_audio_2/model_output"
filelist = os.listdir(audio_folder)
np.random.shuffle(filelist)
write_list(filelist[:50], "filename.lst")