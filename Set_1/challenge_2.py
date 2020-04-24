from binascii import *

string = '1c0111001f010100061a024b53535009181c'
key = '686974207468652062756c6c277320657965'
xor = int(string,16) ^ int(key,16)
result = '746865206b696420646f6e277420706c6179'
print(hex(xor) == hex(int(result,16)))
