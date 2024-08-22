import os
import shutil

def copiar_imagenes(carpeta_fuente, carpeta_destino, max_img):
    imagenes = os.listdir(carpeta_fuente)
    for i, nombreimg in enumerate(imagenes):
        if i < max_img:
            shutil.copy(os.path.join(carpeta_fuente, nombreimg), os.path.join(carpeta_destino, nombreimg))

def main():
    carpetas_fuente = {
        'cuchara': '../../data/cuchara',
        'cuchillo': '../../data/cuchillo',
        'tenedor': '../../data/tenedor',
    }

    carpetas_destino = {
        'cuchara': '../../dataset/cuchara',
        'cuchillo': '../../dataset/cuchillo',
        'tenedor': '../../dataset/tenedor',
    }

    max_imagenes = 98

    for categoria in carpetas_fuente.keys():
        copiar_imagenes(carpetas_fuente[categoria], carpetas_destino[categoria], max_imagenes)

if __name__ == '__main__' :
    main()