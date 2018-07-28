from tkinter import *  # 导入 Tkinter 库
import sys
import csv
from random import *
import time
import pygame


# from tkinter.ttk import *

class App:
    def __init__(self, master):
        # frame = Frame(master) frame.pack()
        self.yyf = Button(root, text="背单词模式", font=('宋体', 30), width=20, foreground='BLUE', command=self.beidanci)
        self.yyf.pack(pady=40)
        Button(root, text="复习模式", width=20, font=('宋体', 30), bg='red', command=self.review).pack(pady=40)
        Button(root, text='退出', width=20, font=('宋体', 30), bg='blue', command=sys.exit).pack(pady=40)

    def get_pron(self, row):
        pass
        # print('this is pronunciation')

    def say_hi(self):
        print('hello world')

    def beidanci(self):
        newPage = Tk()
        newPage.title('背单词模式 author:杨宇锋')
        newPage.geometry('1150x600')

        records = {}

        try:
            record_file = open('records.csv', 'r', encoding='utf-8')
            csv_record_reader = csv.reader(record_file)
            for row in csv_record_reader:
                records[row[0]] = int(row[1])

        except BaseException as e:
            print(' You may be new to this software so you don\'t have records.  ')

        with open('words.csv', 'r', encoding='gbk') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = []
            for row in csv_reader:
                data.append(row)

        global var_list
        var_list = [str(m) for m in range(10)]
        meaning_list = [str(m) for m in range(10)]
        length_csv = 3071
        rd = [randint(0, length_csv) for m in range(10)]

        def check_whether_recite(old_rd):
            if 0 == len(records):
                return old_rd
            for i in range(10):
                if data[old_rd[i]][0] in records and records[data[old_rd[i]][0]] >= 2:
                    while data[old_rd[i]][0] in records and records[data[old_rd[i]][0]] >= 2:
                        old_rd[i] = randint(0, length_csv)
            return old_rd

        rd = check_whether_recite(rd)

        for m in range(10):
            var_list[m] = data[rd[m]][0]+' :    '
            meaning_list[m] = data[rd[m]][1]

        def get_sound():
            word_list = [var_list[i].split(' ')[0] for i in range(10)]
            file_list = [r'word_sound/' + word + '.mp3' for word in word_list]  # r'word_sound/abandon.mp3'
            pygame.mixer.init()

            for file in file_list:
                try:
                    track = pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    time.sleep(1.3)
                    pygame.mixer.music.stop()
                except BaseException as e:
                    time.sleep(1.3)

        var_text = '\n\n'.join(var_list)
        meaning_text = '\n\n'.join(meaning_list)

        word_box = Label(newPage, text=var_text, justify=LEFT)
        word_box.pack(side=LEFT, padx=25)

        meaning_box = Label(newPage, text=meaning_text, width=91, justify=LEFT)
        meaning_box.pack(side=LEFT)

        def get_new_page():
            global var_list
            for word in var_list:
                records[word.split(' ')[0]] = records.get(word.split(' ')[0], 0) + 1
            new_rd = [randint(0, length_csv) for m in range(10)]
            new_rd = check_whether_recite(new_rd)
            for m in range(10):
                var_list[m] = data[new_rd[m]][0] + ' :    '
                meaning_list[m] = data[new_rd[m]][1]
            _var_text = '\n\n'.join(var_list)
            _meaning_text = '\n\n'.join(meaning_list)

            word_box.config(text=_var_text)
            meaning_box.config(text=_meaning_text)

        def update_record():
            record_data = [[element, records[element]] for element in records]
            with open('records.csv', 'w', newline='') as record_file1:
                writer = csv.writer(record_file1)
                for row1 in record_data:
                    writer.writerow(row1)

        Button(newPage, text='退出', command=newPage.destroy).pack(side=BOTTOM, padx=30, pady=10)
        Button(newPage, text='保存记录', command=update_record).pack(side=BOTTOM, padx=30, pady=10)
        Button(newPage, text='看完这一页', command=get_new_page).pack(side=BOTTOM, padx=30, pady=10)
        sound_button = Button(newPage, text='sound', command=get_sound)
        sound_button.pack(side=BOTTOM, padx=30, pady=10)

        newPage.mainloop()

    def review(self):
        reviewPage = Tk()
        reviewPage.title('复习模式 author:杨宇锋')
        reviewPage.geometry('800x400')

        review_records = {}
        try:
            with open('records.csv', 'r', encoding='utf-8') as record_file2:
                csv_record_reader2 = csv.reader(record_file2)
                for row2 in csv_record_reader2:
                    review_records[row2[0]] = int(row2[1])
        except BaseException as e:
            errorPage = Tk()
            errorPage.title('报错啦，找不到文件')

            errorLabel = Label(errorPage, text='找不到你的records.csv文件, \n你是不是还没开始背单词啊')
            errorLabel.pack(padx=40, pady=40)
            errorButton = Button(errorPage, text='好吧', command=errorPage.destroy)
            errorButton.pack(padx=40)

            errorPage.mainloop()

        with open('words.csv', 'r', encoding='gbk') as csv_file:
            csv_reader = csv.reader(csv_file)
            data1 = {}
            for row in csv_reader:
                data1[row[0]] = row[1]

        global rd_word
        rd_word = choice([theWord for theWord in review_records])
        wordLabel = Label(reviewPage, text=rd_word, font=('宋体', 35))
        wordLabel.pack(padx=40, pady=20)
        meaning = '隐藏释义'
        meaningLabel = Label(reviewPage, text=meaning, font=('宋体', 17), justify=LEFT)
        meaningLabel.pack(padx=40, pady=20)

        review_records[rd_word] += 1

        def reduce_times():
            global rd_word
            if review_records[rd_word] >= 2:
                review_records[rd_word] -= 1

        respondButton = Button(reviewPage, text='不太熟悉', command=reduce_times, font=('宋体', 20))
        respondButton.pack(padx=40,pady=20)

        def show_low_level():
            global rd_word
            rd_word = choice([theWord for theWord in review_records
                              if review_records[theWord] == 1])
            wordLabel.config(text=rd_word)
            review_records[rd_word] += 1
            meaning = '隐藏释义'
            meaningLabel.config(text=meaning)

        def show_medium_level():
            global rd_word
            rd_word = choice([theWord for theWord in review_records
                              if 2 <= review_records[theWord] < 4])
            wordLabel.config(text=rd_word)
            review_records[rd_word] += 1
            meaning = '隐藏释义'
            meaningLabel.config(text=meaning)

        def show_medium_level2():
            global rd_word
            rd_word = choice([theWord for theWord in review_records
                              if 4 <= review_records[theWord] < 6])
            wordLabel.config(text=rd_word)
            review_records[rd_word] += 1
            meaning = '隐藏释义'
            meaningLabel.config(text=meaning)

        def show_high_level():
            global rd_word
            rd_word = choice([theWord for theWord in review_records
                              if 4 <= review_records[theWord]])
            wordLabel.config(text=rd_word)
            review_records[rd_word] += 1
            meaning = '隐藏释义'
            meaningLabel.config(text=meaning)

        def showMeaning():
            global rd_word
            meaning = data1[rd_word]
            meaningLabel.config(text=meaning)

        def save_review_records():
            record_data3 = [[element, review_records[element]] for element in review_records]
            with open('records.csv', 'w', newline='') as record_file3:
                writer3 = csv.writer(record_file3)
                for row3 in record_data3:
                    writer3.writerow(row3)

        def playSound():
            global rd_word
            file3 = r'word_sound/' + rd_word + '.mp3'
            pygame.mixer.init()
            try:
                track1 = pygame.mixer.music.load(file3)
                pygame.mixer.music.play()
                time.sleep(1.5)
                pygame.mixer.music.stop()
            except BaseException as e:
                time.sleep(1.5)
                print('No sound of this word')


        explaination = Button(reviewPage, text='查看释义', font=('宋体', 20), command=showMeaning)
        explaination.pack(padx=80, pady=20)

        low_level = Button(reviewPage, text='1', command=show_low_level)
        low_level.pack(padx=30, side=LEFT)

        medium_level = Button(reviewPage, text='2-3', command=show_medium_level)
        medium_level.pack(padx=30, side=LEFT)

        medium_level2 = Button(reviewPage, text='4-5', command=show_medium_level2)
        medium_level2.pack(padx=30, side=LEFT)

        high_level = Button(reviewPage, text='>5', command=show_high_level)
        high_level.pack(padx=30, side=LEFT)

        saveButton = Button(reviewPage, text='保存记录', command=save_review_records)
        saveButton.pack(padx=30, side=LEFT)

        soundButton = Button(reviewPage, text='sound', command=playSound)
        soundButton.pack(padx=30, side=LEFT)

        quitButton = Button(reviewPage, text='退出', command=reviewPage.destroy)
        quitButton.pack(padx=30, side=LEFT)

        reviewPage.mainloop()


root = Tk()
root.title('GREwords    author:杨宇锋')  # 主窗口标题
root.geometry('800x400')  # 主窗口大小，中间的为英文字母x
app = App(root)
root.mainloop()
