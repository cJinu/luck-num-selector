import random

def _select():
    A = set([])
    while len(A)<6:
        A.add(random.randint(1,45))
    return A

print(_select())
