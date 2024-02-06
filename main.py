import string

def generator(max:int, file, prefix:str="", pi:int=0, i:int=0):
    realMax = 26**2 + 26 # This is not ideal, I want to go forever!

    alphabet = string.ascii_uppercase

    for n in range(26):
        if i >= max or i >= realMax:
            return
        s = prefix + alphabet[n] + "\n"
        i += 1
        file.write(s)

    generator(max, file, alphabet[pi], (pi+1)%26, i)

# -------------------

file = open("thingo.txt", "w")

generator(71000, file)

file.close()
