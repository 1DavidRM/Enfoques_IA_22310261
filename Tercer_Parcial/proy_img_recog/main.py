import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# ===== IMPORTAR LIBRERÍAS =====
# cv2: OpenCV para procesamiento de imágenes
# easyocr: Librería para reconocimiento óptico de caracteres (OCR)
# matplotlib: Para visualización de gráficos e imágenes
# numpy: Para operaciones numéricas
# os: Para operaciones del sistema de archivos

# ===== CARGAR IMAGEN =====
# Construir la ruta del archivo de forma independiente del SO

import os
image_path = os.path.join(os.path.dirname(__file__), 'test2.png')

img = cv2.imread(image_path)  # Leer imagen desde archivo en formato BGR

# Verificar si la imagen se cargó correctamente
if img is None:
    print(f"Error: No se pudo cargar la imagen desde: {image_path}")
    print(f"Ruta absoluta: {os.path.abspath(image_path)}")
    exit(1)

print(f"Imagen cargada exitosamente desde: {image_path}")

# ===== INICIALIZAR DETECTOR DE TEXTO =====
# Crear un lector de OCR:
# - ['en']: detectar texto en inglés
# - gpu=False: usar CPU (cambiar a True si tienes GPU disponible)
reader = easyocr.Reader(['en'], gpu=False)

# ===== DETECTAR TEXTO EN LA IMAGEN =====
# readtext() retorna una lista con tuplas (bbox, text, score):
# - bbox: coordenadas de la caja delimitadora
# - text: texto detectado
# - score: confianza de la detección (0-1)
text_ = reader.readtext(img)

threshold = 0.25
# ===== UMBRAL DE CONFIANZA =====
# Solo procesar textos con confianza > 25%

# ===== DIBUJAR CUADROS Y TEXTO =====
# Iterar sobre cada texto detectado
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    # Si la confianza es mayor al umbral, dibujar caja y texto
    if score > threshold:
            # Dibujar rectángulo verde alrededor del texto
            # bbox[0] = esquina superior izquierda
            # bbox[2] = esquina inferior derecha
            # (0, 255, 0) = verde en formato BGR
            # 5 = grosor de la línea en píxeles
        cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
        
            # Escribir texto detectado sobre la imagen
            # bbox[0] = posición superior izquierda
            # cv2.FONT_HERSHEY_COMPLEX = tipo de fuente
            # 0.65 = escala de tamaño
            # (255, 0, 0) = azul en formato BGR
            # 2 = grosor del texto
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

# ===== VISUALIZACIÓN Y GUARDADO =====
# Convertir imagen de BGR (OpenCV) a RGB (Matplotlib) para colores correctos
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.savefig('output.png')  # Guardar imagen procesada en archivo
plt.show()  # Mostrar imagen en pantalla