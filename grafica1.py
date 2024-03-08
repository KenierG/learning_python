import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Crear el gráfico de dispersión
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')

# Agregar títulos y etiquetas
plt.title('Diagrama de Dispersión Aleatorio')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la gráfica
plt.colorbar(label='Tamaño de los puntos')
plt.show()