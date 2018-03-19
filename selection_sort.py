from sort_utils import legnagyobb_megkeres, cserel


def rendezes_legnagyobb_kivalasztassal(l):
    """Az l egész értekeket tartalmazó listát növekvő sorrendbe rendezi"""
    for utolso_ind in range(len(l)-1,-1,-1):
        utolso = l[utolso_ind]
        max, max_ind = legnagyobb_megkeres(l, utolso_ind)
        if utolso < max:
            cserel(l, utolso_ind, max_ind)


l = [20,19,18,17,16,2,4,6,3,1]
print(l)
rendezes_legnagyobb_kivalasztassal(l)
print(l)

