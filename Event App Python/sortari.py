def cmp(p1, p2, key=None):
    """
        Functie care compara doi parametri.
        p1 = primul parametru
        p2 = al doilea parametru
        key = cheia dupa care se compara
        Daca p1 > p2 returneaza true, false in caz contrar.
    """
    if (key(p1) if key else p1) > (key(p2) if key else p2):
        return True
    if (key(p1) if key else p1) == (key(p2) if key else p2):
        id_eveniment1 = p1.get_id()
        id_eveniment2 = p2.get_id()
        if id_eveniment1 > id_eveniment2:
            return True
    return False
    
def selection_sort(list, key=None, reverse=False):
    """
        Metoda de sortare selection sort.
        Sorteaza elementele unei liste.
        list = lista cu elemente
        key = cheia
        reverse = crescator/descrescator
    """
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if cmp(list[i], list[j], key):
                aux = list[i]
                list[i] = list[j]
                list[j] = aux
    if reverse==True:
        list.reverse()
    return list

def shaker_sort(list, key=None, reverse=False):
    """
        Metoda de sortare shaker sort.
        Sorteaza elementele unei liste.
        list = lista cu elemente
        key = cheia
        reverse = crescator/descrescator
    """
    sorted = False
    value = 0
    while sorted==False:
        sorted = True
        for i in range(value, len(list)-value-1):
            if cmp(list[i], list[i+1], key):
                sorted = False
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
        for i in range(len(list)-value-1, value, -1):
            if not cmp(list[i], list[i-1], key):
                sorted = False
                aux = list[i]
                list[i] = list[i-1]
                list[i-1] = aux
        value += 1
    if reverse==True:
        list.reverse()
    return list
            
        
    