import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
import matplotlib.pyplot as plt

def aumentar_datos(ruta_dataset, target_size=(224,224), batch_size=32, muestra_imagenes=10):
    datagen = ImageDataGenerator(
        rescale=1. / 255,
        rotation_range=30,
        width_shift_range=0.25,
        height_shift_range=0.25,
        shear_range=15,
        zoom_range=[0.5, 1.5],
        validation_split=0.2  # 20% para pruebas
    )

    # Generadores para sets de entrenamiento y pruebas
    data_gen_entrenamiento = datagen.flow_from_directory(
        ruta_dataset, 
        target_size=target_size,
        batch_size=batch_size, 
        shuffle=True, 
        subset='training'
    )

    data_gen_pruebas = datagen.flow_from_directory(
        ruta_dataset, 
        target_size=target_size,
        batch_size=batch_size, 
        shuffle=True, 
        subset='validation'
    )

    # Imprimir algunas imágenes del generador de entrenamiento
    for imagenes, etiquetas in data_gen_entrenamiento:
        for i in range(muestra_imagenes):
            plt.subplot(2, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(imagenes[i])
        plt.show()
        break  # Para mostrar solo un lote de imágenes

    return data_gen_entrenamiento, data_gen_pruebas

def main():
    ruta_dataset = '../../dataset'
    aumentar_datos(ruta_dataset)

if __name__ == '__main__':
    main()