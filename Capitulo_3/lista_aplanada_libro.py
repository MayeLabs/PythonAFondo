# Esta es la solución del libro
# Obj: Entender y verificar que puedo mejorar
# Entrada [1,20,[2,[3,4,[5]]]] Salida = [1,20,2,3,4,5]

def aplanador(llst):
    lista_plana = []
    for elem in llst:
        if isinstance(elem, list):
            lista_plana.extend(aplanador(elem))
        else:
            lista_plana.append(elem)
    return lista_plana

if __name__ == '__main__':
 
    lst = [1,20,[2,[3,4,[5]]]]
    print(aplanador(lst))


    caso_2 = [1,[2,3,4,5],[1,[23,[34]],[62]]]
    print(aplanador(caso_2))

# Conclusiones, tomando en cuenta lo que realice:
# - El bucle for, mejora la necesidad de modificar la lista original
# - Devuelve una lista en vez de modificar una externa
# - extend, es mas adecuado ya que se esta anhandiendo elementos de una lista a otra
# - El uso de pop es ineficiente porque implica un cambio en todos los indices de la lista
#   porque requiere mover todos los indices a la izquierda