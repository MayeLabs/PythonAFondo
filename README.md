# Indice

[Capitulo III](#capitulo-iii)

[Funciones](#funciones)

- [Memoizacio](#memoizacion)
- [Decoradores](#decoradores)
- [Funciones Generadoras](#funciones-generadoras)

# Capitulo III

## Funciones

### *Memoización*

> ***Palabras claves:*** 
>
> Técnica de optimización que evita recalculos.  
> Memorización.
> Eficiencia computacional(ejecución).  

Conciste en crear una memoria de cache interna. Es reservar un espacio de memoria en la función principal de los resultados de la función interna.

Es una técnica que ayuda con la optimizacion ya que usa los resultados anteriores para el actual, pero hay que tener espacial cuidado de no llenar la memoria interna.

### *Decoradores*

Son funciones de orden superior que manejan parametros arbitrarios, donde la función es manejada como cualquier otro objeto y se recibe un función como argumento y retorna una función.

Permiten extender, modificar el comportamiento de una función sin modificar el codigo original.

Los decoradores se puede usar en cualquier función.

Para decorar una función usar @ y el interprete la identificara que la función que esta decorando a la función final.

Se podria dividir como minimo en 3 funciones:
1. Función que recibe: Función decorada 
2. Función principal (función interna o envoltura): Cuerpo del decorador
3. Función que retorna

Si f() NO tiene argumentos -> No usar  
Sino -> Usar *args y *kwars

Ejemplo:

```python
def decorador(func):  # Función que recibe
    def envoltura(*args, **kwargs):  # Función principal (envoltura)
        print("Antes de ejecutar la función")
        resultado = func(*args, **kwargs)  # Llamamos a la función original
        print("Después de ejecutar la función")
        return resultado
    return envoltura  # Función que retorna


@decorador
def saludar():
    print("¡Hola mundo!")

saludar()
```

### *Funciones Generadoras*

> *Generador*  ➙ Objeto que puede producir valor 1 a 1  
> Tipo especial de iterador  
> lazy validation que calcula el siguiente cuando se solicita

Son funciones que permiten crear generadores personalizables.

Se usa **yield** en vez de **return**

Es un tipo especial porque posee una implementación más eficiente en cuanto a memoria (generan valores sobre la marcha) y rendimiento (almacena valor actual).
