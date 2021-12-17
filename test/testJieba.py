# @Time : 2021/12/15 17:17
# @Author : klenq
# @File : testJieba.py
# @Software : PyCharm

import jieba                                # 分词
from matplotlib import pyplot as plt        # 数据可视化
from wordcloud import WordCloud             # 词云
from PIL import Image                       # 图片处理
import numpy as np                          # 矩阵运算
import sqlite3                              # 数据库
# wordcloud 无法安装, 去https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

con = sqlite3.connect('../movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
# print(text)
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
str = ' '.join(cut)
# print(str)

img = Image.open(r'../static/assets/img/tree.jpg')
img_array = np.array(img)       # 将u图片转换成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc"       # 字体所在位置: C:\Windows\Fonts

)
wc.generate_from_text(str)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
# plt.show()

# 输出词云文件到文件
plt.savefig(r'../static/assets/img/word.jpg', dpi=500)  # 需要注释掉 plt.show()
