L=[1,2,3,4,5]
print(L[1])
def replace():
    L.insert(3, L[2]+L[4])
    L.remove(4)
    print(L)
    print(L[4])

replace()
