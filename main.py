import string

def generator(max:int, file, alphabet = string.ascii_uppercase):
    mod = len(alphabet)
    piList = [0]



    for i in range(max):
        print(piList)

        piList[-1] += 1

        if len(piList) > 1:
            for j in range(len(piList)-1, 1, -1):
                if j == mod:
                    piList[j] = 0
                    piList[j-1] += 1

        if piList[0] == mod:
            for n in range(len(piList)):
                piList[n] = 0
            piList.append(0)

# -------------------

file = open("thingo.txt", "w")

generator(1000, file)

file.close()
