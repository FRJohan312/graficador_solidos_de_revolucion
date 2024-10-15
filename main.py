from validaciones import solicitar_funcion
from calculo_del_solido import generar_malla, check_solido
from grafica import graficar_solido

def main():
    # Solicitar la función
    funcion_usuario = solicitar_funcion()

    # Generar la malla de puntos
    X, Y_rotado, Z = generar_malla(funcion_usuario)

    # Verificacion del tipo de solido
    tipo_solido = check_solido(funcion_usuario)
    print(f"El sólido de revolución es un: {tipo_solido}")

    # Grafica
    graficar_solido(X, Y_rotado, Z, tipo_solido)


if __name__ == "__main__":
    main()
