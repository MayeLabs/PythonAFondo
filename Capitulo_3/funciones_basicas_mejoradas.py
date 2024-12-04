
def iniciales(cadena, sep=' '):
    """ Devuelve las iniciales concatenadas en mayusculas de la cadena que esta separadas por " "

    :params cadena: str - Cadena de la que se obtendran las iniciales. Ejemplo: cadena -> Mayer aguilera suarez sep -> ,
    :params sep: str - Delimitador, usado para separar la palabra. Ejemplo: ',' (por defecto un espacio en blanco)
    :return str: Nueva cadena. Ejemplo: MAS
    """

    # Validation
    if isinstance(cadena, str): #Verify if cadena is str
        return ("El valor debe ser una cadena de texto.")

    if any(char.isdigit() for char in cadena):  #Verify if at least one of the characters is true and interrup the for in case true
        return ("Lacadena no debe ser o contener un número.")

    # join -> It is use for join the string
    # x[0].upper() -> Become the character to upper
    # cadena.split(sep) -> Divide the string according sep 
    return ''.join([x[0].upper() for x in cadena.split(sep)])


def division(num, deno=1):
    return num / deno

def permu(num:int, veces:float):
    return num * veces

def suma_pos(a, b, /):
    return a + b

if __name__ == '__main__':

    print("Iniciales:\nIntroducir cadena para obtener sus iniciales:\n---------------------------------------------")
    cadena = input()
    print(iniciales(cadena))
    print("Otros Casos:")
    print(f"iniciales('Juan Perez Martinez'): {iniciales('Juan Perez Martinez')}")
    print(f"iniciales('En una ciudad de la Mancha cuyo nombre'): {iniciales('En una ciudad de la Mancha cuyo nombre')}")
    print(f"iniciales('la,planta,del,parque', sep=','): {iniciales('la,planta,del,parque', sep=',')}")
   
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
