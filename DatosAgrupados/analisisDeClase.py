import numpy as np

# Datos de los intervalos y sus frecuencias absolutas
intervals = np.array([[350, 399], [400, 449], [450, 499], [500, 549],
                      [550, 599], [600, 649], [650, 699], [700, 749],
                      [750, 799], [800, 849]])
frequencies = np.array([4, 6, 9, 20, 31, 80, 42, 10, 8, 2])

# Calcular la media
midpoints = np.mean(intervals, axis=1)  # Punto medio de cada intervalo
mean = np.sum(midpoints * frequencies) / np.sum(frequencies)

# Calcular la mediana
# La mediana se encuentra en la posición 0.5 * suma(frecuencias) en los datos ordenados
cumulative_frequencies = np.cumsum(frequencies)
total_observations = cumulative_frequencies[-1]
median_position = 0.5 * total_observations

# Encontrar el intervalo que contiene la mediana
median_interval_index = np.where(cumulative_frequencies >= median_position)[0][0]
# Intervalo donde se encuentra la mediana
median_interval = intervals[median_interval_index]
F_lower = cumulative_frequencies[median_interval_index - 1] if median_interval_index != 0 else 0
f_median = frequencies[median_interval_index]
median = (median_interval[0] + 
          ((median_position - F_lower) / f_median) * 
          (median_interval[1] - median_interval[0]))

# Moda - el intervalo con la mayor frecuencia absoluta
mode_interval = intervals[frequencies.argmax()]

# Cuartil 3 (Q3), el valor debajo del cual se encuentra el 75% de los datos
Q3_position = 0.75 * total_observations
Q3_interval_index = np.where(cumulative_frequencies >= Q3_position)[0][0]
Q3_interval = intervals[Q3_interval_index]
F_lower_Q3 = cumulative_frequencies[Q3_interval_index - 1] if Q3_interval_index != 0 else 0
f_Q3 = frequencies[Q3_interval_index]
Q3 = (Q3_interval[0] + 
      ((Q3_position - F_lower_Q3) / f_Q3) * 
      (Q3_interval[1] - Q3_interval[0]))

# Decil 9 (D9), el valor debajo del cual se encuentra el 90% de los datos
D9_position = 0.9 * total_observations
D9_interval_index = np.where(cumulative_frequencies >= D9_position)[0][0]
D9_interval = intervals[D9_interval_index]
F_lower_D9 = cumulative_frequencies[D9_interval_index - 1] if D9_interval_index != 0 else 0
f_D9 = frequencies[D9_interval_index]
D9 = (D9_interval[0] + 
      ((D9_position - F_lower_D9) / f_D9) * 
      (D9_interval[1] - D9_interval[0]))

# Cuartil 2 (Q2) es equivalente a la mediana
Q2 = median

print (mean, median, mode_interval, Q3, D9, Q2)
