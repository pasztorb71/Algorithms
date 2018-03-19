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

def sel_sort(l):
    """Az l egész értekeket tartalmazó listát növekvő sorrendbe rendezi"""
    for utolso_ind in range(len(l)-1,-1,-1):
        utolso = l[utolso_ind]
        max, max_ind = legnagyobb_megkeres(l, utolso_ind)
        if utolso < max:
            cserel(l, utolso_ind, max_ind)


l = [20,19,18,17,16,2,4,6,3,1]
print(l)
sel_sort(l)
print(l)

