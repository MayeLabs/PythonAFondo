# Memoización: 
# Conciste en crear una memoria cache interna para calculos posteriores
# Uso de memoria de la funcion principal 
# La memoria almacena resultados anteriores

import timeit

# Funcion recursiva del fibonacci
def fibo_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibo_recursivo(n-1) + fibo_recursivo(n-2)

# Funcion para raalizar memoización
def memoize(f):
    mem = {} # Variable con el papel de memoria
    def mem_func(n):
        if n not in mem: # Verifica si esta en mem
            mem[n] = f(n) # Calcula el fibonacci nuevo y almacena en mem -> Memoria

        return mem[n] # Retorna lo que se almacena
    
    return mem_func


mem_fibo = memoize(fibo_recursivo) # Aplico memorizacion a la funcion

# Comparaciones
print(f"Sin memoización fibo_recursivo(32) N. Veces 1: { timeit.timeit('fibo_recursivo(32)', globals=globals(), number=1) }" )
print(f"Sin memoización fibo_recursivo(32) N. Veces 10: { timeit.timeit('fibo_recursivo(32)', globals=globals(), number=10) }" )


print(f"Con memoización fibo_recursivo(32) N. Veces 1: { timeit.timeit('mem_fibo(32)', globals=globals(), number=1) }" )
print(f"Con memoización fibo_recursivo(32) N. Veces 10: { timeit.timeit('mem_fibo(32)', globals=globals(), number=10) }" )
print(f"Con memoización fibo_recursivo(32) N. Veces 1000: { timeit.timeit('mem_fibo(32)', globals=globals(), number=1) }" )


# Conclusion: La eficiencia se produce al ejecutar mas veces

