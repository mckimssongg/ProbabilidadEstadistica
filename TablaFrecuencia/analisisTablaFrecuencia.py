import numpy as np
import pandas as pd

# Datos de ejemplo
datos = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]

# Creación de intervalos de clase
bins = np.linspace(min(datos)-0.5, max(datos)+0.5, 6) # 5 intervalos de clase
etiquetas = [(f"{bins[i]:.1f} - {bins[i+1]:.1f}") for i in range(len(bins)-1)]

# Agrupar los datos en esos intervalos
hist, edges = np.histogram(datos, bins=bins)

# Crear un DataFrame para la tabla de frecuencia
tabla = pd.DataFrame({
    "Intervalo de Clase": etiquetas,
    "Frecuencia": hist,
    "Frecuencia Acumulada": np.cumsum(hist),
    "Frecuencia Relativa": hist / sum(hist)
})

# Calcular los límites reales y la marca de clase
tabla['Límites Reales'] = [(f"{edges[i]} - {edges[i+1]}") for i in range(len(edges)-1)]
tabla['Marca de Clase'] = (edges[:-1] + edges[1:]) / 2

print(tabla)
