def decodedcheck(text):
    probablity = 0
    common_words = ['the', 'at', 'there', 'some', 'my', 'of', 'be', 'use', 'her', 'than', 'and', 'this', 'an', 'would', 'first', ' a ', 'have', 'each', 'make', 'water', 'to', 'from', 'which', 'like', 'been', 'in', 'or', 'she', 'him', 'call', 'is', 'one', 'do', 'into', 'who', 'you', 'had', 'how', 'time', 'oil', 'that', 'by', 'their', 'has', 'its', 'it', 'word', 'if', 'look', 'now', 'he', 'but', 'will', 'two', 'find', 'was', 'not', 'up', 'more', 'long', 'for', 'what', 'other', 'write', 'down', 'on', 'all', 'about', 'go', 'day', 'are', 'were', 'out', 'see', 'did', 'as', 'we', 'many', 'number', 'get', 'with', 'when', 'then', 'no', 'come', 'his', 'your', 'them', 'way', 'made', 'they', 'can', 'these', 'could', 'may', ' I ', 'said', 'so', 'people', 'part']
    for i in common_words:
        a = text.lower().count(i)
        probablity += len(i) * a
    return probablity

given = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Turn the given strig into array of hex goruping 2 letters
given_arr = [given[i]+given[i+1] for i in range(0,68,2)]

# turn Hex Array into DECIMAL
dec_given = [int(val,16) for val in given_arr]

# Take the dec_given and XOR every thing with 0,1,2...255
ans_list_dec = [[ i^j for j in dec_given] for i in range(0,256)]

# Take the XOR'd data and turn that DECIMAL into ASCII
ans_list_en = ["".join([chr(j) for j in i]) for i in ans_list_dec]

# Print EVERY Probabale OUTPUT AND CHECK MANULLAY to see which of them makes sense.
for i in ans_list_en:
    if decodedcheck(i)>2:
        print("\n{} \n{}".format(i,"-"*50))

#FOund "cOOKING mcS LIKE A POUND OF BACON" at index 120 