import time
import pygame

word_list = ['abandon', 'abase', 'abash', 'asjhd', 'abbreviate', 'abdicate', 'aberrant', 'abet', 'abeyance', 'abandon']

file_list = [r'word_sound/' + word + '.mp3' for word in word_list]    # r'word_sound/abandon.mp3'
pygame.mixer.init()

for file in file_list:
    try:
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(1.3)
        pygame.mixer.music.stop()
    except BaseException as e:
        time.sleep(1.3)

#播放音乐10秒后停止
