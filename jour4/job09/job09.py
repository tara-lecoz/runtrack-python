def maxi(liste):
    max=liste[0]
    for i in liste:
        if i>=max:
            max=i
    return max

def minimum(liste):
    min=liste[0]
    for i in liste:
        if i <= min:
            min=i
    return min

liste=[8,24,27,48,2,16,9,102,7,84,91]

print(maxi(liste))
print(minimum(liste))