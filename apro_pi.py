def calculate_pi1() -> None: #I created this
    pi = 4
    i = 0
    coff = -1

    while True:
        n = 3 + i * 2
        i += 1
        pi += coff*(4 / n)

        coff = -coff
        print(pi)


def calculate_pi2(n) -> float:# from internet
    pi = 0
    demon = 1

    for j in range(2):
        for i in range(n):
            if i % 2 == 0:
                pi += 4/demon
            else:
                pi -= 4/demon

            demon += 2
    return pi

#print(calculate_pi2(100000))
#calculate_pi1()