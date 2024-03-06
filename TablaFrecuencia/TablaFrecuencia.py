import numpy as np
import pandas as pd
from func.funcTablaFrecuencias import rango, numClases, amplitud, intervalos, frecuencias

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
    
    def generar_tabla_alternativa(self):
        # Calcula los intervalos y las frecuencias usando las funciones importadas
        interval = intervalos(self.datos)
        frec = frecuencias(self.datos)
        
        # Etiqueta los intervalos para mostrarlos en la tabla
        etiquetas = [f"{inf:.2f} - {sup:.2f}" for inf, sup in interval]

        # Calcula la frecuencia acumulada
        frec_acumulada = [sum(frec[:i+1]) for i in range(len(frec))]

        # Calcula la frecuencia relativa
        total_datos = sum(frec)
        frec_relativa = [f / total_datos for f in frec]

        # Calcula los límites reales como inf-0.5 y sup+0.5
        limites_reales = [f"{inf-0.5:.2f} - {sup+0.5:.2f}" for inf, sup in interval]

        # Calcula la marca de clase como el punto medio de cada intervalo
        marca_clase = [(inf + sup) / 2 for inf, sup in interval]

        # Construye la tabla de frecuencia como un DataFrame de Pandas
        tabla = pd.DataFrame({
            "Intervalo de Clase": etiquetas,
            "Frecuencia": frec,
            "Frecuencia Acumulada": frec_acumulada,
            "Frecuencia Relativa": frec_relativa,
            "Límites Reales": limites_reales,
            "Marca de Clase": marca_clase
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
