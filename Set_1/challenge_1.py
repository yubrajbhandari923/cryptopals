from binascii import *
import base64 


# My Function
def Hex_To_base64(string):
    result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    hexVal = unhexlify(string)
    print(base64.b64encode(hexVal).decode() == result)


# Given str Hex
Hex_To_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')