# Tipo de expresiones especiales
# Estas funciones pueden ser usadas dentro de otras funciones
# Al no poseer nombres no se pueden llamar mas adelante
# Pueden asignarse a una variable
# Usan la pa#labra reservada lambda y simples expresiones

# Una funcion normal seria:
def identidad(x):
    return x

# Pero como funcion anonima seria:
lambda x:x


f_x3 = lambda x: x * 3
print(f_x3(10)) # 30

suma = lambda x,y:x+y
print(suma(5,10)) # 15

# Las funciones anonimas se usan como funciones:
# De ordenación, manipulación, filtrado

lst = ['a1', 'a12', 'a100', 'a5']
print(sorted(lst)) # ['a1', 'a100', 'a12', 'a5'] Los resultados no se ordenaron por numero, sino por caracter
print(sorted(lst, key=lambda x: int(x[1:]))) # Lambda es usada para tomar en cuenta solos los numeros

lst = [1, 425, 3421, 34, 2]
lst.sort(key = lambda x:(x < 400, x)) # Ordena por tuplas de forma 
print(lst) # [425, 3421, 1, 2, 34]

# Me surgio la duda: Por que no muestra la lista con elementos de forma de tupla
# Respuesta: Porque key permite usar los elementos de forma interna, no se guardar en la lst, sino que se usan durante el proceso


