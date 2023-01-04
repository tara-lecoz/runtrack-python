for i in range(1000):
    div = 0
    for j in range(2,i):
        if i%j == 0:
            div = div + 1
    if div == 0:
        print(i)
