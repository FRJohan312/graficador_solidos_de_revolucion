import numpy as np

def generar_malla(funcion_usuario):
    # Intervalo de x
    x_valores = np.linspace(0, 2, 100)
    
    # Angulos de la rotación (0 a 2pi)
    theta_valores = np.linspace(0, 2 * np.pi, 100)

    # Malla de puntos para rotar la función
    X, Theta = np.meshgrid(x_valores, theta_valores)
    Y = funcion_usuario(X)  # coor y
    Z = Y * np.cos(Theta)  # Rotación yz
    Y_rotado = Y * np.sin(Theta)  # Rotación en el plano yz 

    return X, Y_rotado, Z

def check_solido(func):
    try:
        if func(0) == 0:
            return "Disco"
        else:
            return "Arandela"
    except (ValueError, ZeroDivisionError):
        return "Indefinido"
