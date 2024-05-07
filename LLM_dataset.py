import os
from PIL import Image
import matplotlib.pyplot as plt


def create_train_json(path):
    with open(path, "a") as f:
        f.write('[\n')

    for item in os.listdir('./dataset/train/GALAXY'): 
        with open(path, "a") as f:
            f.write('\t {"conversations": [\n')
            f.write('\t\t{"from": "user", "value": "<img>/data/smf/LAMO_swin_transformer/dataset/train/GALAXY/'+ str(item) + '</img>Given a spectral images, promptly identify and issue a warning regarding the image into one of the folling types: galaxy, qso, or star. Return the answer in an Assignment Statement, containing ONE variable: WARNING. Only return the WARNING, not the Description"},\n')
            f.write('\t\t{"from": "assistant", "value": "WARNING = \'0\'"}\n')
            f.write('\t]},\n')
    for item in os.listdir('./dataset/train/QSO'):
        with open(path, "a") as f:
            f.write('\t {"conversations": [\n')
            f.write('\t\t{"from": "user", "value": "<img>/data/smf/LAMO_swin_transformer/dataset/train/QSO/'+ str(item) + '</img>Given a spectral images, promptly identify and issue a warning regarding the image into one of the folling types: galaxy, qso, or star. Return the answer in an Assignment Statement, containing ONE variable: WARNING. Only return the WARNING, not the Description"},\n')
            f.write('\t\t{"from": "assistant", "value": "WARNING = \'1\'"}\n')
            f.write('\t]},\n')
    for item in os.listdir('./dataset/train/STAR'):
        with open(path, "a") as f:
            f.write('\t {"conversations": [\n')
            f.write('\t\t{"from": "user", "value": "<img>/data/smf/LAMO_swin_transformer/dataset/train/STAR/'+ str(item) + '</img>Given a spectral images, promptly identify and issue a warning regarding the image into one of the folling types: galaxy, qso, or star. Return the answer in an Assignment Statement, containing ONE variable: WARNING. Only return the WARNING, not the Description"},\n')
            f.write('\t\t{"from": "assistant", "value": "WARNING = \'2\'"}\n')
            f.write('\t]},\n')

    with open(path, "a") as f:
        f.write(']\n')


def create_test_json(path):
    with open(path, "a") as f:
        f.write('[\n')

    for item in os.listdir('./dataset/test'): 
        with open(path, "a") as f:
            f.write('\t {"conversations": [\n')
            f.write('\t\t{"from": "user", "value": "<img>/data/smf/LAMO_swin_transformer/dataset/test/'+ str(item) + '</img>Given a spectral images, promptly identify and issue a warning regarding the image into one of the folling types: galaxy, qso, or star. Return the answer in an Assignment Statement, containing ONE variable: WARNING. Only return the WARNING, not the Description"},\n')
            f.write('\t\t{"from": "assistant", "value": "WARNING = \'None\'"}\n')
            f.write('\t]},\n')

    with open(path, "a") as f:
        f.write(']\n')




train_path = "./dataset/train.json"
test_path = "./dataset/test.json"
create_train_json(train_path)
create_test_json(test_path)