def inverser(mot):
    ch=""
    for i in range((len(mot)) -1, -1, -1):
        ch = ch+ mot[i]
    return ch

print(inverser("nikana"))