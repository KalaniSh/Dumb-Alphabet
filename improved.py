import string

def numerator(num, alph = string.ascii_uppercase):
    mod = len(alph) # = 26 for string.ascii_uppercase
    currNumer = [0]

    for i in range(num):
        
        # Print the current alphabetisized num
        s=""
        for i in currNumer:
            s+=alph[i]
        print(s)

        currNumer[-1]+=1

        if currNumer[-1]>=mod:
            for i in range(len(currNumer)-1, -1, -1):
                if currNumer[i] >= mod:
                    currNumer[i]=0
                    if i==0:
                        currNumer.append(0)
                    else: 
                        currNumer[i-1]+=1

numerator(200)