"""
    字符的编码和解码
    1 byte = 8 bit
    1 kb = 1024 byte
    1 mb = 1024 kb
"""

str = "你好中国"
print(type(str))
byte1 = str.encode(encoding="utf-8")

str2 = byte1.decode(encoding="gbk")
print(str2)

