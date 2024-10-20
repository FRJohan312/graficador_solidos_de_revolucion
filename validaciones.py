import numpy as np
import sympy as sp

x = sp.symbols('x')

# BLINDAJE
def solicitar_funcion():
    funciones_permitidas = ['sin', 'cos', 'tan', 'sqrt', 'exp', 'x']
    
    while True:
        entrada_usuario = input("Ingresa una función de x (sin, cos, sqrt, exp): ")

        # Funciones a usar
        if any(func in entrada_usuario for func in funciones_permitidas):
            try:
                expresion = sp.sympify(entrada_usuario, evaluate=False)
                funcion_usuario = sp.lambdify(x, expresion, "numpy")  # Convertir a función numpy

                # Probar si la función funciona en el intervalo para evitar errores
                x_test = np.linspace(0, 2, 10)
                prueba = funcion_usuario(x_test)
                
                if np.any(np.isnan(prueba)) or np.any(np.isinf(prueba)):
                    print("La función tiene valores indefinidos o infinitos en el intervalo. Inténtalo de nuevo.")
                    continue
                return funcion_usuario 
                
            except (sp.SympifyError, TypeError) as e:
                print(f"Error en la función: {e}. Ingrese una función válida.")
        else:
            print(f"Función no permitida")
