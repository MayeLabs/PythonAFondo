# Decoradores:
# Se usa para extender o modificar una funcion
# Los decoradores usan min 3 funciones:
# La que recibe, la que envuelve y la que retorna , veamos:
import time

def temporiza(func):  # Función que recibe o decorador
    def funcion_interna(*args, **kwargs): #Función principal -> envoltura
        inicio = time.time()
        resultado = func(*args, **kwargs)
        tiempo = time.time() - inicio
        print(f'La Función {func.__name__} tardo {tiempo}s usando {args} {kwargs}')
        return resultado # Retorna la función original 
    return funcion_interna

@temporiza # Indica que esta suma_elems esta decorada
def suma_elems(elems):
    acc = 0
    for x in elems:
        acc += x
    return acc

suma_elems(range(1000))


