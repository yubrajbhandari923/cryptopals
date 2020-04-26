given = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
# Turn the given strig into array of hex goruping 2 letters
given_arr = [given[i]+given[i+1] for i in range(0,68,2)]

# turn Hex Array into Binary of 8 digits i.e. Bytes
bin_given = [bin(int(val,16))[2:].zfill(8) for val in given_arr]

#generate all possible Bytes character that may have been used for XOR i.e. 00000000 =1 to 11111111 =255 
key_list = [bin(i)[2:].zfill(8) for i in range(0,255)]


print(bin_given)