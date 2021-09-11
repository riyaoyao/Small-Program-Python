# 程序说明： 生成200个激活码,数字夹杂数据
'''
# 方法一
import uuid
uuids = []
num = 10
for i in range(1, num):
    # 基于随机数生成 8-4-4-4-12固定格式
    code = uuid.uuid4()
    uuids.append(code)
print(uuids)
'''
# 方法二
import random
import string
import math
def create_code(i, len=10):
    chars = string.ascii_letters + string.digits
    code = ''
    for i in range(int(len/2)):
        code = code + random.choice(chars)
    code = code + '-'
    for i in range(len-int(len/2)):
        code = code + random.choice(chars)
    return code


num = 10
for i in range(num):
    codes = create_code(i)
    print(codes)