def mylen(L):
    count=0
    for i in L:
        count=count+1
    return count

L=[8,24,27,48,2,16,9,102,7,84,91]
def inverserordre(L):
    i=0
    for i in range(mylen(L)):
        for j in range(i+1,mylen(L)):
            if L[i] > L[j]:
                L[i],L[j]=L[j],L[i]
    return L

print(inverserordre(L))