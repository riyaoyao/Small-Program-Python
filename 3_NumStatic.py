# 程序说明：统计文件中的制定单词出现次数
fp = './File/words.txt'
# 打开文件，如果打开成功，用read读取文件的全部内容
file = open(fp)
text = file.read()
word = 'love'
num = 0
while text.find(word)!=-1:
    num = num + 1
    # split(str,num)第二个参数为分割次数
    text = text.split(word, 1)[1]
print(num)
file.close()