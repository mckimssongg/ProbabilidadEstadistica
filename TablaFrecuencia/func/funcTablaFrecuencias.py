# Tabla Distribucion de frecuencias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rango(data):
    return max(data) - min(data)

def numClases(data):
    return int(1 + 3.322 * np.log10(len(data)))

def amplitud(data):
    return rango(data) / numClases(data)

def intervalos(data):
    amp = amplitud(data)
    clases = numClases(data)
    limInf = min(data)
    limSup = limInf + amp
    intervalos = []
    for _ in range(clases):
        intervalos.append((limInf, limSup))
        limInf = limSup
        limSup += amp
    return intervalos

def frecuencias(data):
    interval = intervalos(data)
    frecuencias = []
    for i in range(len(interval)):
        frecuencias.append(len([x for x in data if interval[i][0] <= x < interval[i][1]]))
    return frecuencias

def tablaFrecuencias(data):
    interval = intervalos(data)
    frec = frecuencias(data)
    tabla = pd.DataFrame({'Intervalo': interval, 'Frecuencia': frec})
    return tabla

def graficoFrecuencias(data):
    tabla = tablaFrecuencias(data)
    plt.bar(range(len(tabla)), tabla['Frecuencia'])
    plt.xticks(range(len(tabla)), tabla['Intervalo'], rotation=90)
    plt.show()
    
