from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
text = ""
with open('ctf.txt', 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        line = line.strip('\n')

text += ' '.join(jieba.cut(line))
backgroud_Image = plt.imread('background.jpg')
wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    stopwords=STOPWORDS,
    max_font_size=150,
    random_state=30
    )
wc.generate_from_text(text)
plt.imshow(wc)
d = path.dirname(__file__)
wc.to_file(path.join(d, "wc.jpg"))
