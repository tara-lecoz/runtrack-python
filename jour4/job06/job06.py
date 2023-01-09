L=[1,2,3,4,5]
for i,j in [(0,4)]:
    L[i],L[j] = L[j],L[i]
print(L)