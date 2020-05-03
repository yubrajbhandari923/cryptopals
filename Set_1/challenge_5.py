import sys


# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
# Key : ICE

def main(given, key):
    given_bytes = given.encode('utf-8')
    key_bytes = key.encode('utf-8')
    output = ""
    for i, item in enumerate(given_bytes):
        output += ('0'+hex(item ^ key_bytes[i%3])[2:])[-2:]
    print(output)


if __name__ == "__main__":
    if not (len(sys.argv)==3) :
        print("\n\nUsuage : python {} 'Given Text' 'KEY' ".format(sys.argv[0]))
        exit()
    main(sys.argv[1], sys.argv[2])