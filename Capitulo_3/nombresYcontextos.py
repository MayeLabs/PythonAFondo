# Que variables pueden ser modificadas y accedidas y cuales no
# Variables globales: - Definidas a nivel de fichero de texto 
#                     - Lectura: Desde cualquier parte
#                     - Edicion: Uso de la palbra reservada global (Se diferencia de C en ello)


var_global = 10

# Uso permitido de var_global

def foo(x):
    return x + var_global

print(foo(5)) #15

'''
# La actualizacion sin el global NO esta permitido
def foo_act_no(x):
    var_global += 10
    return var_global + x

print(foo_act_no(5)) # UnboundLocalError: local variable 'var_global' referenced before assignment
'''

# Uso de global para su actualizacion
def foo_act(x):
    global var_global # Define que la variable pertenece al contexto global
    var_global += 10
    return var_global + x

print(foo_act(5)) # 25

# Se modifica la variable global
print(var_global)


# Variable de una funcion interna - Local:
#                     - Definidas a nivel de una funcion
#                     - Edicion: Uso de la palbra reservada nonlocal
def foo_correct():
    ruedas = 4
    def pinchar_rueda():
        nonlocal ruedas # Ya que no se pasa como argumento, es necesario nonlocal para que se pueda modificar dentro y fuera
        ruedas -=1

    print(f'Numero de ruedas: {ruedas}') # 4
    pinchar_rueda()    
    print(f'Numero de ruedas: {ruedas}') # 3

# Se crean diferentes contextos una vez se definen las variables: Un contexto para la f(x) principal y otro para f(x) interna

foo_correct()


# Si no se usa el nonlocal y se pasa como arg solo 
def foo_prueba_solo_arg():
    partes = 4
    def dividir(partes):
        partes -=1 # Se modifica el arg
        print(f'Numero de partes - Funcion dividir(ruedas): {partes}') # 3

    dividir(partes)
    print(f'Numero de partes - Funcion foo_prueba_solo_arg: {partes}') # 4


foo_prueba_solo_arg()