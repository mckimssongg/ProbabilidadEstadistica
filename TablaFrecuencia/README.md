# Tabla de frecuencia

Este paquete proporciona herramientas para generar tablas de frecuencia a partir de un conjunto de datos. La tabla de frecuencia es una herramienta estadística clave que permite resumir la distribución de los datos agrupándolos en intervalos o clases.

## Características

El paquete incluye funciones para calcular:

- Intervalos de clase
- Frecuencias
- Frecuencias acumuladas
- Frecuencias relativas
- Límites reales de clase
- Marca de clase

### Generación de Tabla de Frecuencia

`TablaFrecuencia.py` incluye dos métodos principales para generar la tabla de frecuencia:

1. `generar_tabla`: Utiliza `numpy` para calcular los intervalos de clase y las frecuencias.
2. `generar_tabla_alternativa`: Calcula los intervalos y las frecuencias manualmente para mayor control sobre los intervalos de clase.


## Análisis de Diferencias entre Métodos de Generación de Tablas

Al generar tablas de frecuencia con este paquete, se ofrecen dos métodos principales que pueden producir resultados ligeramente diferentes:

### Intervalos de Clase y Límites Reales

- **`generar_tabla`**: Utiliza `np.linspace` para distribuir uniformemente los intervalos entre el mínimo y el máximo de los datos ajustados. Este método puede no reflejar exactamente el dato mínimo como el límite inferior del primer intervalo.
- **`generar_tabla_alternativa`**: Calcula manualmente los intervalos de clase basándose directamente en el mínimo de los datos, asegurando que el límite inferior del primer intervalo sea exactamente el mínimo de tus datos.

### Precisión y Redondeo

La precisión de los números flotantes y el redondeo pueden variar entre las funciones, afectando ligeramente cómo se calculan los límites reales y las marcas de clase.

## ¿Cuál Método es el Correcto?

Ambos métodos son correctos pero sirven a diferentes necesidades de análisis:
- Si se necesita que el límite inferior del primer intervalo refleje exactamente el mínimo de los datos, `generar_tabla_alternativa` es preferible.
- Para una distribución uniforme de intervalos ajustados, `generar_tabla` es adecuado.

## Ajustes Recomendados

Para que los intervalos de clase reflejen adecuadamente tus datos desde el mínimo hasta el máximo, considera cómo defines los intervalos y cómo ajustas los límites. Modificar este comportamiento en `generar_tabla` o asegurar que `generar_tabla_alternativa` calcule los intervalos de manera que satisfaga tus necesidades analíticas es crucial para obtener los resultados deseados.

## Conclusión

Ambos enfoques son válidos, y la elección depende de tus criterios específicos para el análisis de datos. Es importante entender cómo cada método calcula los intervalos para elegir el que mejor se adapte a tus necesidades. Ajustar el primer intervalo para incluir el dato mínimo exacto de tu conjunto de datos es una práctica común en análisis estadísticos, logrado con el enfoque manual de `generar_tabla_alternativa`.


### Ejemplo de uso:

```python
# Instanciando la clase con datos de ejemplo y sin especificar el número de clases
datos_ejemplo = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]
datos_ejemplo_clase = [1,1,3,2,4,5,6,2,4,7,8,1,9,2,3,5,10,12,11,6]
datos_ejemplo = datos_ejemplo_clase
tabla_frecuencia = TablaDeFrecuencia(datos=datos_ejemplo)

# Mostrar la tabla de frecuencia y la información adicional
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
```

Output:

```
  Intervalo de Clase  Frecuencia  ...            L�mites Reales  Marca de Clase
0          0.5 - 2.9           6  ...                 0.5 - 2.9             1.7
1          2.9 - 5.3           6  ...                 2.9 - 5.3             4.1
2          5.3 - 7.7           3  ...   5.3 - 7.699999999999999             6.5
3         7.7 - 10.1           3  ...  7.699999999999999 - 10.1             8.9
4        10.1 - 12.5           2  ...               10.1 - 12.5            11.3

[5 rows x 6 columns]
  Intervalo de Clase  Frecuencia  Frecuencia Acumulada  Frecuencia Relativa  \
0        1.00 - 3.20           8                     8             0.421053   
1        3.20 - 5.40           4                    12             0.210526   
2        5.40 - 7.60           3                    15             0.157895   
3        7.60 - 9.80           2                    17             0.105263   
4       9.80 - 12.00           2                    19             0.105263   

  L�mites Reales  Marca de Clase  
0    0.50 - 3.70             2.1  
1    2.70 - 5.90             4.3  
2    4.90 - 8.10             6.5  
3   7.10 - 10.30             8.7  
4   9.30 - 12.50            10.9  
11
5
2.2
{'Rango': 11, 'N�mero de Clases': 5, 'Tama�o del Intervalo': 3.0}
```

## NOTA 

Codigo:

`np.linspace`: Genera un arreglo de valores equidistantes para definir los límites de cada clase.

`np.histogram`: Calcula la frecuencia de los datos en cada intervalo definido por bins.

`np.cumsum`: Calcula la suma acumulativa de las frecuencias para obtener la frecuencia acumulada.

