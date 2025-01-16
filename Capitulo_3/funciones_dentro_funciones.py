# Definir funciones dentro de otras funciones
# Clausuras o Cerramientas = Crean su propio contexto
# Obj: Realizar encapsulamiento u organizar logica interna
# 

# Como hacerlo ? Definir la f(x) dentro del bloque:


# CASO 1: Generar funciones diferentes que se puedan reusar como funciones nuevas
# ------------------------------------------------------------------------------
def telefono_con_prefijo(prefijo_pais):
    def f_telefono(num_tlf):
        return f'+{prefijo_pais} {num_tlf}'
    return f_telefono

# La f(x) f_telefono accede a la variable prefijo_pais

telefono_espanha = telefono_con_prefijo(34) # telefono_espanha se usa mas adelante como funcion, y ena la instancia de telefono_espanha se almacena 34 como prefijo

print(telefono_espanha(33665478)) # Aca se pasa el num_tlf y la funcion telefono_con_prefijo accede al prefijo y completa el numero, haciendo su propio contexto, que sera diferente para otra variable
# +34 33665478

# Veamos x cada nueva variable se crea su propio contexto
telefono_aleman = telefono_con_prefijo(96)
telefono_andorra = telefono_con_prefijo(376)

print(telefono_aleman(47839020)) # +96 47839020
print(telefono_andorra(231547839020)) # +376 231547839020


# NOTA:
# Clausuras (Closure): La a función interna (f_telefono) "recuerda" y usa el valor de las variables de la función externa (telefono_con_prefijo).

# CASO 2: Encapsular - Encapsulando la logica de la funcion principal en funciones pequenhas
# ------------------------------------------------------------------------------------------
def beneficios(gastos: list, ingresos: list, tramos_impuestos):
    def obtener_impuestos(ingreso):
        
        impuesto_actual = tramos_impuestos[0][1]
        
        for hasta_valor, impuesto in tramos_impuestos:
            if hasta_valor > ingreso:
                break
            else:
                impuesto_actual = impuesto
        
        return impuesto

    def calculo_neto(ingreso_bruto):
        impuesto = obtener_impuestos(ingreso_bruto)
        return ingreso_bruto - (ingreso_bruto * impuesto)

    gastos_totales = sum(gastos)
    ingresos_netos = sum(map(calculo_neto, ingresos))
    return ingresos_netos - gastos_totales


gastos = [22, 314, 32, 52]
ingresos = [45, 623, 12, 90]
tramos_impuestos = [(20, 0.06),  (50, 0.08), (200, 0.1), (500, 0.2), (float('Inf'),0.21)]
balance_final = beneficios(gastos, ingresos, tramos_impuestos)
print(balance_final) # 205.85000000000002

