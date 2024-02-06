import string

alphabet = string.ascii_uppercase

def generator(prefix, i, max, file):
    if i > max:
        return
    for n in range(26):
        if i > max:
            return
        s = prefix + alphabet[n] + "\n"
        i += 1
        file.write(s)
        generator(prefix + alphabet[n], i, max, file)

# -------------------

file = open("thingo.txt", "w")

generator("", 0, 702, file)

file.close()
