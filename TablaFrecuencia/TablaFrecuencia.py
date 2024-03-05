import numpy as np
import pandas as pd

class TablaDeFrecuencia:
    def __init__(self, datos, num_clases=None):
        """
        Inicializa la tabla de frecuencia con los datos proporcionados.
        Si no se proporciona el número de clases, se calcula automáticamente.
        """
        self.datos = datos
        self.num_clases = num_clases if num_clases is not None else self.calcular_num_clases()
        self.rango = self.calcular_rango()
        self.intervalo = self.calcular_intervalo()
        self.tabla = self.generar_tabla()

    def calcular_rango(self):
        """Calcula el rango de los datos."""
        return max(self.datos) - min(self.datos)

    def calcular_num_clases(self):
        """
        Calcula el número de clases usando la regla de Sturges: K = 1 + 3.322 log(N),
        donde N es el número total de datos.
        """
        return int(1 + 3.322 * np.log10(len(self.datos)))

    def calcular_intervalo(self):
        """Calcula el tamaño del intervalo de clase dividiendo el rango entre el número de clases."""
        return np.ceil(self.rango / self.num_clases)

    def generar_tabla(self):
        """
        Genera la tabla de frecuencia completa, detallando cada paso del proceso.
        """
        # Crear intervalos de clase utilizando numpy.linspace para generar los bordes de los intervalos.
        # Se ajusta el mínimo y el máximo para asegurar que todos los datos sean incluidos.
        bins = np.linspace(min(self.datos)-0.5, max(self.datos)+0.5, self.num_clases+1)

        # Etiquetar cada intervalo para la visualización en la tabla.
        etiquetas = [f"{bins[i]:.1f} - {bins[i+1]:.1f}" for i in range(len(bins)-1)]

        # Calcular la frecuencia de los datos en cada intervalo utilizando numpy.histogram.
        hist, edges = np.histogram(self.datos, bins=bins)

        # Construir la tabla de frecuencia como un DataFrame de pandas.
        tabla = pd.DataFrame({
            "Intervalo de Clase": etiquetas,
            "Frecuencia": hist,
            "Frecuencia Acumulada": np.cumsum(hist),  # Suma acumulativa de las frecuencias para cada intervalo.
            "Frecuencia Relativa": hist / sum(hist),  # Proporción de cada frecuencia respecto al total de observaciones.
            "Límites Reales": [f"{edges[i]} - {edges[i+1]}" for i in range(len(edges)-1)],  # Límites exactos usados para el cálculo de frecuencias.
            "Marca de Clase": (edges[:-1] + edges[1:]) / 2  # Promedio de los límites de cada intervalo, representando el valor central.
        })

        return tabla

    def mostrar_tabla(self):
        """Muestra la tabla de frecuencia generada."""
        return self.tabla

    def info_adicional(self):
        """Devuelve información adicional: el rango, el número de clases y el tamaño del intervalo de la distribución de los datos."""
        return {
            "Rango": self.rango,
            "Número de Clases": self.num_clases,
            "Tamaño del Intervalo": self.intervalo
        }

# Instanciando la clase con datos de ejemplo y sin especificar el número de clases
datos_ejemplo = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]
tabla_frecuencia = TablaDeFrecuencia(datos=datos_ejemplo)

# Mostrar la tabla de frecuencia y la información adicional
tabla = tabla_frecuencia.mostrar_tabla()
info_adicional = tabla_frecuencia.info_adicional()

print(tabla)
print(info_adicional)