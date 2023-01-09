def produit(liste):
    prod=1
    for i in liste:
        if 25<i<90:
            prod=prod*i
    return prod

liste=[8,24,27,48,2,16,9,102,7,84,91]
print(produit(liste))