import math

def isPrim(x):
    if x == 0 or x == 1: return False
    if x < 0:
        print("A szám nem lehet negatív")
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0: return False
    return True
