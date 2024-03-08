import pandas as pd
from TablaFrecuencia import TablaDeFrecuencia
from func.funcTablaFrecuencias import *
# TESTS

# Instanciando la clase con datos de ejemplo y sin especificar el número de clases
datos_ejemplo = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]
datos_ejemplo_clase = [80, 20, 60, 75, 40, 55, 70, 75, 60, 85, 40, 60, 75, 78, 37, 42, 60, 80, 88, 75,
 70, 60, 80, 90, 95, 65, 32, 43, 44, 62, 28, 45, 35, 63, 66, 88, 95, 98, 96, 94]
datos_ejemplo = datos_ejemplo_clase
tabla_frecuencia = TablaDeFrecuencia(datos=datos_ejemplo)

tabla = tabla_frecuencia.mostrar_tabla()
tabla_alternativa = tabla_frecuencia.generar_tabla_alternativa()
info_adicional = tabla_frecuencia.info_adicional()

pd.set_option('display.max_columns', None)
print(tabla)
print(info_adicional) 


# pd.set_option('display.max_columns', None)
# print(tabla_alternativa)
# print(rango(datos_ejemplo))
# print(numClases(datos_ejemplo))
# print(amplitud(datos_ejemplo))