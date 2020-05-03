import sys
# given 
# string = '1c0111001f010100061a024b53535009181c'
# key = '686974207468652062756c6c277320657965'
# result = '746865206b696420646f6e277420706c6179'
def main(string, key, result):
    xor = int(string,16) ^ int(key,16)
    if result:
        print(hex(xor) == result)
    else:
        print(hex(xor))

if __name__ == "__main__":
    if not (len(sys.argv)==3 or len(sys.argv)==4) :
        print("\n\nUsuage : python {} 'Given Hex' 'KEY' 'Expected Result'\n #Expected result is Optional. If only hex & Key is given then result will be returned ".format(sys.argv[0]))
        exit()
    if len(sys.argv)==4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        main(sys.argv[1], sys.argv[2], False)