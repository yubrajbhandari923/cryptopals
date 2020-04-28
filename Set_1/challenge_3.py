given = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Turn the given strig into array of hex goruping 2 letters
given_arr = [given[i]+given[i+1] for i in range(0,68,2)]

# turn Hex Array into DECIMAL
dec_given = [int(val,16) for val in given_arr]

# Take the dec_given and XOR every thing with 0,1,2...255
ans_list_dec = [[ i^j for j in dec_given] for i in range(0,256)]

# Take the XOR'd data and turn that DECIMAL into ASCII
ans_list_en = ["".join([chr(j) for j in i]) for i in ans_list_dec]

# Print EVERY POSSIBLE OUTPUT AND CHECK MANULLAY to see which of them makes sense.
for i in ans_list_en:
    print("\n{} \n{}".format(i,"-"*50))
    if "LIKE" in i:
        print(ans_list_en.index(i))
        break 

#FOund "cOOKING mcS LIKE A POUND OF BACON" at index 120 