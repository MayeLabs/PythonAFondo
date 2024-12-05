
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


# Cuando se usan valores por defecto en parametros hay que tener precaucion de que no sean mutables
# Lo ideal en caso de usarlas es colocar None como valor por defecto y comprobar si es none para inicializar

# Ejemplo Practico del libro

# Se define la f(x) anadir_valor para comprobarlo
# Usando la funcion con un parametro mutable, con el valor vacio por defecto
def anadir_valor(elem, lst=[]):
    lst.append(elem)
    return lst

# En la primera llamada se usa la lista por defecto []
print(anadir_valor(1)) # [1]

# En las siguientes llamadas reutiliza las mismas lista definida por defecto
print(anadir_valor(5)) # [1, 5]
print(anadir_valor(2)) # [1, 5, 2]

# Si se quiere crear listas "diferentes", veremos que todas son en realidad la misma
lst1 = anadir_valor(10) 
lst2 = anadir_valor(50)
print(lst1) # [1, 5, 2, 10, 50]
print(lst2) # [1, 5, 2, 10, 50]


# Para evitar compartir accidentalmente el mismo objeto mutable entre llamadas
# Se coloca por defecto None y una validación 
def anadir_valor_seguro(elem, lst=None):
    if lst is None:
        lst = []
    lst.append(elem)
    return lst

# Al realizar varias llamadas se creara una lista correspondiente a cada inserción 
print(anadir_valor_seguro(1)) # [1]
print(anadir_valor_seguro(5)) # [5]

# Y en el caso de crear listas, entonces no se comparte el mismo objeto
lst3 = anadir_valor_seguro(10) 
lst4 = anadir_valor_seguro(50)
print(lst3) # [10]
print(lst4) # [50]
