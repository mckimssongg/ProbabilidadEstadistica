from TablaFrecuencia import TablaDeFrecuencia, rango, numClases, amplitud
import pandas as pd

# TESTS

# Instanciando la clase con datos de ejemplo y sin especificar el número de clases
datos_ejemplo = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]
datos_ejemplo_clase = [1,1,3,2,4,5,6,2,4,7,8,1,9,2,3,5,10,12,11,6]
datos_ejemplo = datos_ejemplo_clase
tabla_frecuencia = TablaDeFrecuencia(datos=datos_ejemplo)

tabla = tabla_frecuencia.mostrar_tabla()
tabla_alternativa = tabla_frecuencia.generar_tabla_alternativa()
info_adicional = tabla_frecuencia.info_adicional()

print(tabla)
pd.set_option('display.max_columns', None)
print(tabla_alternativa)
print(rango(datos_ejemplo))
print(numClases(datos_ejemplo))
print(amplitud(datos_ejemplo))
print(info_adicional) 