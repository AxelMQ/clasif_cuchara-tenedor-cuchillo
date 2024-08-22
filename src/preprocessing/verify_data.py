import os

def contar_imagenes(carpeta):
    return len([nombre for nombre in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, nombre))])

def main():
    carpetas = {
        'cucharas': '../../data/cuchara',
        'cuchillos': '../../data/cuchillo',
        'tenedores': '../../data/tenedor',
    }

    for categoria, carpeta in carpetas.items():
        cantidad = contar_imagenes(carpeta)
        print(f"- Cantidad de imagenes en {categoria}: {cantidad}")

if __name__ == '__main__':
    main()
