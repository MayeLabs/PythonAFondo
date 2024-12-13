# Ejercicio:
# Dada una lista de niveles, se debe unificar la lista
# Entrada [1,20,[2,[3,4,[5]]]] Salida = [1,20,2,3,4,5]
def aplanar_lista(lst, lst_new):

    elem = lst.pop(0)
  
    if isinstance(elem, int):
        lst_new.append(elem)
    else:
        aplanar_lista(elem, lst_new)
        
    if len(lst) > 0:
        aplanar_lista(lst, lst_new)

if __name__ == '__main__':
    lst = [1,20,[2,[3,4,[5]]]]
    lst_new = []
    aplanar_lista(lst, lst_new)
    print(lst_new)

    case_2 = [1,[2,3,4,5],[1,[23,[34]],[62]]]
    lst_c2 = []
    aplanar_lista(case_2, lst_c2)
    print(lst_c2)