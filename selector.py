import random

def _select():
    A = set([])
    while len(A)<6:
        A.add(random.randint(1,45))
    return A

if __name__ == '__main__':
    print(_select())
