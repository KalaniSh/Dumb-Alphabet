import string

def generator(max:int, file, alphabet = string.ascii_uppercase):
    mod = len(alphabet)
    iList = [0]

    for n in range(max):
        s = ""
        for i in iList:
            s += alphabet[i]
        s += "\n"

        file.write(s)

        iList[-1] += 1

        for j in range(len(iList)-1, 0, -1):
            if iList[j] == mod:
                iList[j] = 0
                iList[j-1] += 1

        if iList[0] == mod:
            for n in range(len(iList)):
                iList[n] = 0
            iList.append(0)

# -------------------

file = open("thingo.txt", "w")

generator(6969, file)

file.close()
