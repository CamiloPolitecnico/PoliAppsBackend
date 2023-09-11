from sympy import symbols, sympify, Not, Implies, Equivalent, And, Or, pprint
from itertools import product
import numpy as np

def get_true_table(expresion_str):
    result = []
    # Definir las variables proposicionales
    p, q = symbols('p q ')
    
    # Obtener la expresión lógica como una cadena desde el usuario
    #expresion_str = input("Ingresa la expresión lógica en notación SymPy: ")
    
    # Convertir la cadena en una expresión lógica SymPy
    try:
        expresion = sympify(expresion_str)
    except Exception as e:
        print("Error al analizar la expresión:", e)
        exit(1)
    
    # Generar todas las combinaciones posibles de valores verdadero y falso para las variables
    variables = (p, q)
    valores = list(product([True, False], repeat=len(variables)))
    
    # Imprimir el encabezado de la tabla de verdad
    encabezado = [str(var) for var in variables] + [str(expresion)]
    result.append(encabezado)
    
    # Calcular y mostrar los resultados en la tabla de verdad
    for valor in valores:
        asignaciones = dict(zip(variables, valor))
        resultado = expresion.subs(asignaciones)
        fila = [str(asignaciones[var]) for var in variables] + [str(resultado)]
        result.append(fila)
    
    return result