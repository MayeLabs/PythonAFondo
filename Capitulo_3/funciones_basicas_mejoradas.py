import time

def iniciales(cadena, sep=' '):
    """ Devuelve las iniciales concatenadas en mayusculas de la cadena que esta separadas por " "

    :params cadena: str - Cadena de la que se obtendran las iniciales. Ejemplo: cadena -> Mayer aguilera suarez sep -> ,
    :params sep: str - Delimitador, usado para separar la palabra. Ejemplo: ',' (por defecto un espacio en blanco)
    :return str: Nueva cadena. Ejemplo: MAS
    """

    # Validation
    if isinstance(cadena, str): #Verify if cadena is strAdded validations and new cases for the function iniciales
        return ("El valor debe ser una cadena de texto.")

    if any(char.isdigit() for char in cadena):  #Verify if at least one of the characters is true and interrup the for in case true
        return ("Lacadena no debe ser o contener un número.")

    # join -> It is use for join the string
    # x[0].upper() -> Become the character to upper
    # cadena.split(sep) -> Divide the string according sep 
    return ''.join([x[0].upper() for x in cadena.split(sep)])


def division(num, deno=1):
    """ Devuelve la división del num  entre el deno

    :params num: float - Valor del numerador de la funcion
    :params deno: float - Valor del denominador de la funcion , por defecto 1
    :return float: Resultado de la división
    """

    return num / deno

# Al agregar los tipos de datos a la definicion 
# 1. se considera buena practica 
# 2. se visualiza otra forma de definir la f(x) 
def permu(num:int, veces:float) -> float:
    """ Calcula el producto de un número y una cantidad de veces.

    :params num: int -  El número que se va a multiplicar.
    :params veces: float - La cantidad de veces con la que se multiplicará el número.
    :return float: Resultado de multiplicar num por veces.
    """
    return num * veces

# El caracter '/' indica:
# Los parametros desde el comienzo se usan solamente posicionalmente
# No se puede permutar
# No se puede usar argumento por clave valor suma_pos(a=2,b=26)
def suma_pos(a, b, /):
    """ Calcula la suma de los numeros a y b

    :params a: float - El elemento a de la suma
    :params a: float - El elemento b de la suma
    :return float: Resultado de la suma de a + b 
    """
    return a + b

if __name__ == '__main__':

    print("Iniciales:\nIntroducir cadena para obtener sus iniciales:\n---------------------------------------------")
    cadena = input()
    print(iniciales(cadena))
    print("Otros Casos:")
    print(f"iniciales('Juan Perez Martinez'): {iniciales('Juan Perez Martinez')}")
    print(f"iniciales('En una ciudad de la Mancha cuyo nombre'): {iniciales('En una ciudad de la Mancha cuyo nombre')}")
    print(f"iniciales('la,planta,del,parque', sep=','): {iniciales('la,planta,del,parque', sep=',')}")
   
    print("\nDivision - division(num, deno) :\n---------------------------------------------")
    print("Numerador:")
    num = float(input())
    print("Denominador:")
    deno = float(input())
    print(division(num, deno))
    print("Otros casos")
    print(f"division(3, 45): {division(3,45)}")
    print(f"division(300, 3): {division(300, 3)}")
    time.sleep(2)
    print("\n\033[3mAl usar los nombres en la llamada se pueden permutar los argumentos\033[0m")
    print(f"division(deno= 3, num=45): {division(deno= 3, num=45)}")
    print(f"division(deno= 300, num=3): {division(deno= 300, num=3)}")

    time.sleep(2)
    print("\nSuma - suma_pos(a, b, /):\n---------------------------------------------")
    print("a:")
    a = float(input())
    print("b:")
    b = float(input())
    print(suma_pos(a, b))
    print("\n\033[3mPor el caracter '/' en la def. de la f(x) no se puede permutar\nSe debe usar en estrictor orden\033[0m")
    print(f"suma_pos(20,8): {suma_pos(20,8)}")
    print("\033[3m A continuacion el error \033[0m")
    time.sleep(2)
    print(f"suma_pos(b=20,a=8): {suma_pos(b=20,a=8)}")

