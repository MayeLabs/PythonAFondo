
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
    """ Devuelve la division del num  entre el deno

    :params num: float - Valor del numerador de la funcion
    :params deno: float - Valor del denominador de la funcion , por defecto 1
    :return float: Resultado de la division
    """

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
   
    print("\nDivision - division(num, deno) :\n---------------------------------------------")
    print("Numerador:")
    num = float(input())
    print("Denominador:")
    deno = float(input())
    print(division(num, deno))
    print("Otros casos")
    print(f"division(3, 45): {division(3,45)}")
    print(f"division(300, 3): {division(300, 3)}")
    print("\n\033[3mAl usar los nombres en la llamada se pueden permutar los argumentos\033[0m")
    print(f"division(deno= 3, num=45): {division(deno= 3, num=45)}")
    print(f"division(deno= 300, num=3): {division(deno= 300, num=3)}")

    print("\nSuma:")
    print("a:")
    a = float(input())
    print("b:")
    b = float(input())
    print(suma_pos(a, b))
