# Concepto de la programación funcional
# Funciones que pueden:
# 1. Aceptar otras funciones como parametros
# 2. Retornar funciones

# Ejemplo: Visualizar como una misma definicion de funciones puede
# hacer diferentes lógicas usando funciones externas como parametros
import math

def raiz_de_par(x):
    if not x % 2:
        return math.sqrt(x)
    return 0

def mul_de_par(x, multi=5):
    if not x % 2:
        return x * multi
    return 0

#func -> Es la f(x) como parametro
def aplicar_func(lst, func):
    return [func(x) for x in lst]

# Función externa mul_de_par
lst_mul_par = aplicar_func(range(20), mul_de_par)
print(lst_mul_par) # [0, 0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0]

# Función externa raiz_de_par
lst_raiz = aplicar_func(range(20), raiz_de_par)
print(lst_raiz) # [0.0, 0, 1.4142135623730951, 0, 2.0, 0, 2.449489742783178, 0, 2.8284271247461903, 0, 3.1622776601683795, 0, 3.4641016151377544, 0, 3.7416573867739413, 0, 4.0, 0, 4.242640687119285, 0]

# Usando una función lambda
mul_de_par_8 = lambda x:mul_de_par(x, multi=8)
lst_lamb = aplicar_func(range(20), mul_de_par_8)
print(lst_lamb) # [0, 0, 16, 0, 32, 0, 48, 0, 64, 0, 80, 0, 96, 0, 112, 0, 128, 0, 144, 0]

# Ejemplo 2: Funcion que retorna funciones
def op(a, b, func):
    return func(a,b)3510

print(op(45,78,int.__add__)) # 123
print(op(47, 78, int.__mul__)) # 3666 