import random

def _select():
    A = set([])
    while len(A)<6:
        A.add(random.randint(1,45))
    return A

if __name__ == '__main__':
    t = int(input('Enter num(1-100): '))
    for _ in range(t):
        print(_select())

