
def iniciales(cadena, sep=' '):
    """ Devuelve las iniciales concatenadas en mayusculas de la cadena que esta separadas por " "

    :params cadena: str - Cadena de la que se obtendran las iniciales. Ejemplo: cadena -> Mayer aguilera suarez sep -> ,
    :params sep: str - Delimitador, usado para separar la palabra. Ejemplo: ','
    :return str: Nueva cadena. Ejemplo: MAS
    """

    # sep='' -> Value for default, cause in the definition, I write sep=' ' 
    # join -> It is use for join the string
    # x[0].upper() -> Become the character to upper
    # cadena.split(sep) -> Divide the string according sep 
    return ''.join([x[0].upper() for x in cadena.split(sep)])

def division(num, deno=1):
    return num / deno

funciones_basicas_mejoradas
def permu(num:int, veces:float):
    return num * veces

def suma_pos(a, b, /):
    return a + b

if __name__ == '__main__':

    print("Iniciales:\nIntroducir cadena para obtener sus iniciales:")
    cadena = input()
    print(iniciales(cadena))

    print("\nDivision:")
    print("Numerador:")
    num = float(input())
    print("Denominador:")
    deno = float(input())
    print(division(num, deno))

    print("\nSuma:")
    print("a:")
    a = float(input())
    print("b:")
    b = float(input())
    print(suma_pos(a, b))
