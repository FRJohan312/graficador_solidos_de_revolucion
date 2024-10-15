import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_solido(X, Y_rotado, Z, tipo_solido):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    try:
        # Graficar la superficie
        ax.plot_surface(X, Y_rotado, Z, cmap='viridis')

        # Titulo y secciones
        ax.set_title(f"Sólido de Revolución: {tipo_solido}")
        ax.set_xlabel("Eje X (Radio)")
        ax.set_ylabel("Eje Y (Radio)")
        ax.set_zlabel("Altura Z")

        plt.show()
    except Exception as e:
        print(f"Error al graficar: {e}")
