# Funciones Recursivas:
# Funciones que se llaman asi mismas para completar su logica, en vez de llamar bucles
# Patron: Caso Base y llamadas recurrentes

# Entendiendo la funcion
def contar_rec(elem, acumulador=0):
    if elem == 0:
        return acumulador # Casos base, cuando se deje de llamar asi misma la funcion
    else:
        acumulador += elem
        # Se llama asi misma y elem-1 va disminuyendo hasta llegar al caso base
        return contar_rec(elem - 1, acumulador)

# La funcion hace una suma del acumulador + el elemento, mientras el elemento disminuye en 1 y cuando llega a 0, se finaliza la funcion 

# Corrida en frio:
# Inicializado: elem = 4 y acumulador = 0
# 1-> acumulador = 4 , elem = 3 
# 2-> acumulador = 7 , elem = 2
# 3-> acumuador = 9, elem = 1
# 4-> acumulador = 10, elem = 0
# 5-> Aca se llega al caso base

print(contar_rec(4))


