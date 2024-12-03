def iniciales(cadena, sep=' '):
    return ''.join([x[0].upper() for x in cadena.split(sep)])

def division(num, deno=1):
    return num / deno


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
