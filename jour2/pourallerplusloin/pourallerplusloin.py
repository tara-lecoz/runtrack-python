def triangleoupas(a,b,c):
    if a + b >= c:
        result=print("C'est un triangle existant")
        if a == b == c:
            result=print("Il est équilatéral")
        elif a == b or b == c or c == a:
            result=print("Il est isocèle")
        elif a^2+b^2 == c^2:
            result=print("Il est rectangle")
    else:
        result=print("Ce n'est pas un triangle")
    return result

print("---------------------")
triangleoupas(2,3,4)
print("---------------------")
triangleoupas(3,4,5)
print("---------------------")
triangleoupas(3,3,5)
print("---------------------")
triangleoupas(3,3,3)
print("---------------------")
triangleoupas(1,1,12)
print("---------------------")
