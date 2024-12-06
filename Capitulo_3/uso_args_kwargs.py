# Uso de args y kwargs
# Los clave-valor se almacenan en kwargs y los que no como args (argumentos posicionales)
# Se usa para extender y usar número indefinido de argumentos 


# Esta f(x) es copiada del libro, para observar como se almacenan segun la llamada
# Los '*' indican si se pasara un argumento Clave valor o posicionlaes, permiten identificar y descomponer
def mi_funcion(*args, **kwargs):
    print(f"args: {args}, kwargs: {kwargs}")


# Casos válidos con mi_funcion
mi_funcion() # args: (), kwargs: {}
# Al pasar un solo arg, python lo empaqueta como tupla
mi_funcion(42) # args: (42,), kwargs: {}
mi_funcion(vehiculo='coche') # args: (), kwargs: {'vehiculo': 'coche'}

# Se prueba que al pasar argumentos posicionales y clave valor python diferencia
mi_funcion(345, 'Juan', modo='Vuelo', flag='Activado') # args: (345, 'Juan'), kwargs: {'modo': 'Vuelo', 'flag': 'Activado'}
mi_funcion(345, 'Juan', 'Maye', 'Lab', modo='Vuelo', flag='Activado')

# Extendiendo
def calculo_general(**kwargs):
    ret_s = suma(**kwargs)
    ret_d = division(**kwargs)
    return ret_s * ret_d

def suma(op1, op2, **kwargs):
    return op1 + op2

def division(num, deno, **kwargs):
    return num / deno


# Casos validos
res = calculo_general(op1=5, op2=9, num=8, deno=2)
print(res) # 6
res_f = calculo_general(op1=5, op2=5, op3=5, num=8, deno=4)
print(res_f) # 20

# Casos Invalidos
"""
res_t = calculo_general(2, 2, num=8, deno=4)
print(res_t) 

res_t = calculo_general(op4=2, op5=2, num=8, deno=4)
print(res_t) 
"""

# Conclusion: '**kwars' permiten manejar argumentos clave valor-ilimitados, pero las claves (actuan como identificadores explicitos) deben coincidir con
# los identificadores correspondiente, sino python no sabra asociar a cual corresponde y debe usar

# Ejemplo con parametros posicionales
def calculo_posicional(*args):
    rest_s = suma(*args)
    res_d = division(*args)

def suma(op1, op2, *args):
    return op1 + op2

def division(a1, a2, num, deno):
    return num / deno

print(res)
res = calculo_posicional(5,9,8,2) # 56