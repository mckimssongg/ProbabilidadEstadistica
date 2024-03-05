# Tabla de frecuencia

Ejemplo de uso:

```python
# Instanciando la clase con datos de ejemplo y sin especificar el número de clases
datos_ejemplo = [23, 24, 24, 25, 22, 26, 28, 29, 27, 25, 26, 24, 23, 25, 27, 28, 29, 30, 22, 23]
tabla_frecuencia = TablaDeFrecuencia(datos=datos_ejemplo)

# Mostrar la tabla de frecuencia y la información adicional
tabla = tabla_frecuencia.mostrar_tabla()
info_adicional = tabla_frecuencia.info_adicional()

print(tabla)
print(info_adicional)
```

Codigo:

`np.linspace`: Genera un arreglo de valores equidistantes para definir los límites de cada clase.
`np.histogram`: Calcula la frecuencia de los datos en cada intervalo definido por bins.
`np.cumsum`: Calcula la suma acumulativa de las frecuencias para obtener la frecuencia acumulada.

```

```
