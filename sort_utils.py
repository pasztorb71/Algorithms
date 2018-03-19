def legnagyobb_megkeres(l, vege):
    """Az l egész értekeket tartalmazó listában megkeresi a legnagyobb értéket és annak sorszámát
       a 0. elemtől a vege-dik elemig
       Visszatér a maximum értékkel és a maximum sorszámával"""
    max = 0
    max_ind = 0
    for i in range(vege+1):
        if l[i] > max:
            max = l[i]
            max_ind = i
    return max, max_ind

def cserel(l, ind1, ind2):
    """Az l egész értekeket tartalmazó listában felcseréli az ind1-edik elemet az ind2-edik elemmel"""
    tmp = l[ind1]
    l[ind1] = l[ind2]
    l[ind2] = tmp
