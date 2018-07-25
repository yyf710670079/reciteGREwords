import requests
import urllib
import csv


# word = 'distinct'
# src = 'http://dict.youdao.com/dictvoice?audio=distinct&type=2'
# urllib.request.urlretrieve(src, 'word_sound/' + word + '.mp3')

with open('words.csv', 'r', encoding='gbk') as csv_file:
    csv_reader = csv.reader(csv_file)
    data_word = []
    for row in csv_reader:
        data_word.append(row[0])


for word in data_word:
    try:
        src = 'http://dict.youdao.com/dictvoice?audio='+ word + '&type=2'
        urllib.request.urlretrieve(src, 'word_sound/' + word + '.mp3')
        print('================' + word + '这个单词正在下载' + '====================')
    except BaseException as e:
        print('下载出错啦,' + word + '这个单词跳过!')