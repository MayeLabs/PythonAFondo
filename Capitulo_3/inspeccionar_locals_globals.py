# Inspeccionar las variables definidas en cada contexto
# Funciones locals y globals

pez = 'Nemo'
def pecera():
    pez = 'Dori'
    x = 5
    print(f'Locals: {locals()}')
    print(f'Globals: {globals()}')

pecera()
''' 
Locals: {'pez': 'Dori', 'x': 5}
Globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f9c5b57d690>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/maye/Escritorio/PythonAFondo/Capitulo_3/inspeccionar_locals_globals.py', '__cached__': None,
         'pez': 'Nemo', 'pecera': <function pecera at 0x7f9c5b6bfd90>}
'''