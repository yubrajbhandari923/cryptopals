from binascii import *
import base64, sys
#Given:
# hex = 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# My Function
def Hex_To_base64(string, result):
    hexVal = unhexlify(string)
    if result:
        print(base64.b64encode(hexVal).decode() == result)
    else:
        print(base64.b64encode(hexVal).decode())



if __name__ == "__main__":
    if not (len(sys.argv)==2 or len(sys.argv)==3) :
        print("\n\nUsuage : python {} 'Given Hex' 'Expected Result'\n #Expected result is Optional. If only hex is given then result will be returned ".format(sys.argv[0]))
        exit()
    if len(sys.argv)==3:
        Hex_To_base64(sys.argv[1], sys.argv[2])
    else:
        Hex_To_base64(sys.argv[1], False)