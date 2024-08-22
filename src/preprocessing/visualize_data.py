import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def mostrar_imagenes(carpeta, cantidad=25):
    imagenes = os.listdir(carpeta)

    plt.figure(figsize=(7,6))
    for i, nombreimg in enumerate(imagenes[:cantidad]):
        plt.subplot(5, 5, i + 1)
        imagen = mpimg.imread(os.path.join(carpeta,nombreimg))
        plt.imshow(imagen)
        # plt.axis('off')

    plt.show()


def main():
    carpetas = {
        'cucharas': '../../data/cuchara',
        'cuchillos': '../../data/cuchillo',
        'tenedores': '../../data/tenedor',
    }

    for categoria, carpeta in carpetas.items():
        print(f"- Mostrando imagenes de {carpeta}: ")
        mostrar_imagenes(carpeta)

if __name__ == '__main__':
    main()