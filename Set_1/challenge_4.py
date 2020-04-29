def decodedcheck(text):
    probablity = 0
    common_words = ['the', 'at', 'there', 'some', 'my', 'of', 'be', 'use', 'her', 'than', 'and', 'this', 'an', 'would', 'first', ' a ', 'have', 'each', 'make', 'water', 'to', 'from', 'which', 'like', 'been', 'in', 'or', 'she', 'him', 'call', 'is', 'one', 'do', 'into', 'who', 'you', 'had', 'how', 'time', 'oil', 'that', 'by', 'their', 'has', 'its', 'it', 'word', 'if', 'look', 'now', 'he', 'but', 'will', 'two', 'find', 'was', 'not', 'up', 'more', 'long', 'for', 'what', 'other', 'write', 'down', 'on', 'all', 'about', 'go', 'day', 'are', 'were', 'out', 'see', 'did', 'as', 'we', 'many', 'number', 'get', 'with', 'when', 'then', 'no', 'come', 'his', 'your', 'them', 'way', 'made', 'they', 'can', 'these', 'could', 'may', ' I ', 'said', 'so', 'people', 'part']
    for i in common_words:
        a = text.lower().count(i)
        probablity += len(i) * a
    return probablity

# OPen the File
f = open("hex_4.txt","rt")
given_hex = f.read().split("\n")

for i in given_hex:
    # Turn the given strig into array of hex goruping 2 letters
    given_arr = [i[k]+i[k+1] for k in range(0,len(i),2)]
    
    # turn Hex Array into DECIMAL
    dec_given = [int(val,16) for val in given_arr]
    
    # Take the dec_given and XOR every thing with 0,1,2...255
    ans_list_dec = [[ k^j for j in dec_given] for k in range(0,256)]

    # Take the XOR'd data and turn that DECIMAL into ASCII
    ans_list_en = ["".join([chr(p) for p in l]) for l in ans_list_dec]

    # Print EVERY Probabale OUTPUT AND CHECK MANULLAY to see which of them makes sense.
    for q in ans_list_en:
        if decodedcheck(q)>10:
            print("\n{} \n{}".format(q,"-"*50))

    # exit()    
    #FOund "Now that the party is jumping"