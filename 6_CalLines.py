#程序说明： 统计共有写过多少行程序，并分别列出来空行和注释
# 注意：没有考虑到行后的注释
import re, os
import string

filename = './2_Gen_ActiveCode.py'
total_line = 0
blank_line = 0
note_line = 0
f = open(filename, 'r', encoding='utf-8')
lines = f.readlines()
f.close()
total_line = len(lines)
line_index = 0
while line_index < total_line:
    line = lines[line_index]
    if line.strip().startswith('#'):
            note_line += 1
            print(line)
    elif re.match("\s*'''", line) is not None:
        note_line += 1
        print(line)
        line_index += 1     # 记得要更新到下一行
        line = lines[line_index]
        while re.match(".*'''$", line) is None:
            print(line)
            note_line += 1
            line_index += 1
            line = lines[line_index]
    elif line.isspace():
        blank_line += 1
    line_index += 1
print('代码总行数为', total_line)
print('   空行数为', blank_line)
print('  注释行数为', note_line)


