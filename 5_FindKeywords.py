# 程序说明：找到多个日记txt中每篇认为最重要的词
import re, os
from collections import Counter

filepath = './File/'
filter_words = ['the', 'a', 'an', 'of', 'in', 'to', 'that', 'is', 'are', 'as', 'I', 'my', 'you', 'and', 'Whenever', 'me','be']

def GetCounter(file):
    wordlib = r"\w+"
    with open(file) as f:
        res = re.findall(wordlib, f.read())
        return Counter(res)

def FindKeyword(filename):
    for i in os.listdir(filename):
        cnts = Counter()
        if os.path.splitext(i)[1]=='.txt':
            cnts = cnts + GetCounter(os.path.join(filename, i))
            for j in filter_words:
                cnts[j] = 0
            print(cnts.most_common()[0][0])

FindKeyword(filepath)