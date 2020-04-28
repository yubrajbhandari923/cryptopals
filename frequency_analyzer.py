import sys, json
from collections import OrderedDict


class master:
    def __init__(self, text):
        self.frequency_table = dict()
        self.bigram_table = dict()
        self.trigram_table = dict()
        self.edited = ""
        self.original = text 
        self.escape_chars = [" ",",",".","{","}",":",";"]
        self.compute_frequencies()
        self.letters_replace({"--" : "--"})
    
    def compute_frequencies(self):
        sanitized_text = "".join([ i for i in self.original if not (i in self.escape_chars)]) 
        #run Through every letter to count them a create a dict.
        for letter in sanitized_text:
            if letter in self.frequency_table:
                self.frequency_table[letter] += 1
            else:
                self.frequency_table[letter] = 1

        #make the dict having count in Desending order.
        self.frequency_table = dict(OrderedDict(sorted(self.frequency_table.items(), key= lambda t:t[1], reverse=True)))

        # print('\n\n\nLetter Frequency Computed: \n '+ json.dumps(self.frequency_table))#.replace(",", ",\n"))
        
        # COmpute Bigram
        for i in range(0,len(sanitized_text)-1,2):
            bigram = sanitized_text[i] + sanitized_text[i+1]
            if bigram in self.bigram_table:
                self.bigram_table[bigram] += 1
            else:
                self.bigram_table[bigram] = 1

        self.bigram_table = dict(OrderedDict(sorted(self.bigram_table.items(), key= lambda t:t[1], reverse=True)))
        # print('\n\n\nBigram Frequency Computed: \n '+ json.dumps(bigram_table))#.replace(",", ",\n"))

            # Trigram Compute 
        for i in range(0,len(sanitized_text)-2,3):
            trigram = sanitized_text[i] + sanitized_text[i+1] + sanitized_text[i+2]
            if trigram in self.trigram_table:
                self.trigram_table[trigram] += 1
            else:
                self.trigram_table[trigram] = 1

        self.trigram_table = dict(OrderedDict(sorted(self.trigram_table.items(), key= lambda t:t[1], reverse=True)))
        return True
        # print('\n\n\nTrigram Frequency Computed: \n '+ json.dumps(trigram_table))#.replace(",", ",\n"))


    def letters_replace(self, replacer):
        print("IN CLASS{}".format( replacer))
        self.edited = ""
        for i in self.original:
            if i in replacer:
                self.edited += replacer[i]
            elif i in self.escape_chars:
                self.edited += i
            else:
                self.edited += "*"
        self.print_replaced()
        return True

    def print_replaced(self):
        ori_buff = ""
        edi_buff = ""
        for i in range(0,len(self.original)):
            ori_buff += self.original[i]
            edi_buff += self.edited[i]
            if self.original[i] == ".":
                print("\n\n"+ori_buff)
                ori_buff = ""
                print(edi_buff)
                edi_buff = ""
                print("-"*50)
        return True


    def interaction(self):
        print("\n\n\n Choose an Option.")
        print("\n 1. View Frequency of Monograms")
        print("\n 2. View Frequency of Bigrams")
        print("\n 3. View Frequency of Trigrams")
        print("\n 4. Replace letters (EnCrYpted : replace)[such that E=r, n=e]")
        print("\n 5. Exit")
        opt = int(input())
        if  opt ==5:
            exit()
        elif opt == 1:
            print("\n\n MonoGram Frequency :\n"+json.dumps(self.frequency_table))
        elif opt == 2:
            print("\n\n BiGram Frequency :\n"+json.dumps(self.bigram_table))
        elif opt == 3:
            print("\n\n TriGram Frequency :\n"+json.dumps(self.trigram_table))
        elif opt == 4:
            print("\n\n Enter word/char to replace : Correct Chars/word")
            word = input()
            arr = word.split(":")
            print(arr)
        else:
            print("\n\n Invalid Choice!")
        

        self.interaction()



def main(encrypted):
    process = master(encrypted)

    print("\n\n\n\nCompleted Processing.\n\nTrying Default variation ....\n\n")
        
    guess_replacer = dict()
    monlist = list(process.frequency_table.keys())[:4] # [e, t, a, i]
    bilist = list(process.bigram_table.keys())[:2] # [th, he, in]
    trilist = list(process.trigram_table.keys())[:2] #[the, and]
    #Add Rules here
    print(guess_replacer)
    if not len(guess_replacer) == 0:
        process.letters_replace(guess_replacer)
    process.interaction()



    


if __name__ == "__main__":
    if len(sys.argv)>2:
        print("Usuage : python frequency_analyazer.py 'Text to analyze' ")
        exit()
    main(sys.argv[1])