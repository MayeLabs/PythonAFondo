
# A diferencia de C, en Python todos los argumentos son pasados por referencia
# Referencia: Se copian los punteros de las variables y no el contenido en sí
# Debemos tener cuidado si el objeto es mutable, porque se modificará dentro y fuera de la función

# Ejemplo practico del libro

a = 'Hola'
b = " Mundo"

# Se define la función Suma, para comprobar lo mencionado
def suma(elem1, elem2):
    elem1 += elem2
    return elem1

# a, b y c al ser objetos no mutables no se modificarán
c = suma(a,b)
print(a)  # 'Hola'
print(b)  # ' Mundo'
print(c)  # 'Hola Mundo'

# Como se observa a se mantiene con su contenido original, pero ...
# Que ocurre en el contenido de una lista
a = [1,2,3]
b = [4, 5]
c = suma(a,b)
print(a)  # [1, 2, 3, 4, 5]  # El contenido de 'a' se ha modificado al ser un objeto mutable
