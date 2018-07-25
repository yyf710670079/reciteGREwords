## 背诵GRE单词软件 RECITE GRE WORDS
![Aaron Swartz](https://github.com/yyf710670079/reciteGREwords/blob/master/word1.jpeg)
### 使用说明
#### 1.下载并安装所需的扩展库
    git clone git@github.com:yyf710670079/reciteGREwords.git
    pip3 install pygame
    pip3 install tkinter

#### 2.解压缩word_sound压缩包并放在同一文件夹下

#### 3.在终端输入
	python3 main.py

#### 4.两种模式：背单词模式和复习模式

##### 背单词模式
![Aaron Swartz](https://github.com/yyf710670079/reciteGREwords/blob/master/word2.jpeg)

- 每显示一页，后台会记录这10个单词

- 按下sound按钮，系统会连续地播放出10个单词的音频，如果音频缺失则会空缺1.3秒左右的时间

- 在每次退出前记得按下保存记录，这样复习模式即可知道这10个单词已经背过

##### 复习模式
![Aaron Swartz](https://github.com/yyf710670079/reciteGREwords/blob/master/word3.jpeg)

- 按下“1-2”按钮会显示一个新的词汇，且该词汇只重复了0次或1次

- 按下“3-5”按钮会显示一个新的词汇，且该词汇只重复了2次到4次

- 按下“>6”按钮会显示一个新的词汇，且该词汇重复了超过4次

- 每按一次不太熟悉，该词汇重复时减少一次，直到0位置

- 每次退出前记得保存记录