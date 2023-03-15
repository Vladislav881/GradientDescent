import random

def function(n, k):
    if k == 0:
        print(0)
        exit()

    a = random.uniform(k + 1, 100)
    b = a / k

    mass = list()
    mass.append(a)
    mass.append(b)

    for i in range(2, n):
         mass.append(random.uniform(b + 1, a - 1))

    random.shuffle(mass)

    print(mass[0],'* (X 00)^2', end="")

    for i in range(1, n):
        print(' +', mass[i],"(X",i*11,")^2", end="")


if __name__ == '__main__':
    n, k = map(int, input().split())
    function(n, k)