import csv
import json
import os

import os
import numpy as np

def read_list(fname):
    result = []
    with open(fname, "r") as f:
        for each in f.readlines():
            each = each.strip('\n')
            result.append(each)
    return result

def load_json(fname):
    with open(fname,'r') as f:
        data = json.load(f)
        return data

csv_save_path = "/mnt/bn/lqhaoheliu/audio_samples_mos/audio/input.csv"

testfilelist = read_list("/mnt/bn/lqhaoheliu/audio_samples_mos/audio/filename.lst")
# Create a list with the header row

metadata = load_json("/mnt/bn/lqhaoheliu/metadata/processed/general_audio/audiocaps/datafiles/audiocaps_test_label.json")
fname_to_transcription = {}

for item in metadata["data"]:
    fname_to_transcription[os.path.basename(item["wav"])] = item["caption"]

#################################################################################
head_row = [["audio_url", "description","model_id"]]
rows = []
root_path = "/mnt/bn/lqhaoheliu/audio_samples_mos/audio"
for folder in os.listdir(root_path):
    if(not os.path.isdir(os.path.join(root_path, folder))): 
        continue

    remote_url = os.path.join("https://github.com/haoheliu/audio_samples_mos/raw/master/","audio", folder)

    for each in testfilelist:
        rows.append([os.path.join(remote_url, each), fname_to_transcription[each], folder])

np.random.shuffle(rows)
rows = head_row+rows
#################################################################################

# Open a new CSV file and write the rows to it
with open(csv_save_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)