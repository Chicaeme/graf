import numpy as np
import matplotlib.pyplot as plt

# Generar estaturas aleatorias para 18 estudiantes (en centímetros)
estaturas = np.array([188, 160, 160, 160, 160, 160, 165, 159, 175, 159, 172, 174, 180, 170, 174, 179, 185, 168])

# Redimensionar el ndarray a una matriz de 2D con 18 filas y 1 columna
estaturas = estaturas.reshape(18, 1)

# Calcular la media, mediana y desviación estándar
media = np.mean(estaturas)
mediana = np.median(estaturas)
desviacion_estandar = np.std(estaturas)

# Mostrar los resultados
print("Estaturas de los estudiantes:\n", estaturas)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

# Graficar los datos usando imshow
plt.imshow(estaturas, aspect='auto', cmap='viridis')
plt.colorbar(label='Estaturas')
plt.title('Estaturas de los estudiantes')
plt.xlabel('Estudiantes')
plt.ylabel('Estatura')
plt.show()