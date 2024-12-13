# Ejercicio:
# Dada una lista de niveles, se debe unificar la lista
# Entrada [1,20,[2,[3,4,[5]]]] Salida = [,20,2,3,4,5]
def aplanar_lista(lst, lst_new):

    elem = lst.pop(0)
    print(elem)

    if isinstance(elem, int):
        lst_new.append(elem)
    else:
        aplanar_lista(elem, lst_new)
        
    if len(lst) > 0:
        aplanar_lista(lst, lst_new)

if __name__ == '__main__':
    lst = [1,20,[2,[3,4,[5]]]]
    lst_new = []
    print(lst)
    lst_r = aplanar_lista(lst, lst_new)
    print(lst_new)
