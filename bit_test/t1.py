# parse string to binary

x = int('0010', 2)
print(x)

x = chr(int('01011110',2))

'''
下面是关于binary 类型，形成binary有两种方法：
    1. b'0101'
    2. bitarray.tobytes

# https://pypi.python.org/pypi/bitarray/
'''



from bitarray import bitarray
# from hex

a = bitarray()
a.append(True)
b = a.tobytes()
print(b)

# 自定义某字符及其表示
d = {'H':bitarray('111'), 'e':bitarray('0'),
    'l':bitarray('110'), 'o':bitarray('10')}
a = bitarray()
# 将a当中的内容按d的格式定义进行encode
a.encode(d, "Hello")
print(a)

# 将a当中的内容按d的格式进行decode, 返回tuple
y = a.decode(d)

# 将y 列表当中的元素join到空字符中
print(''.join(y))
a.decode(d)