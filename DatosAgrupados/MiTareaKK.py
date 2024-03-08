from StatisticalCalculatorComment import ExtendedStatisticalCalculator
import numpy as np

# Datos de los intervalos y sus frecuencias absolutas
intervals = np.array([[ 50,  60],
 [ 60,  70],
 [ 70,  80],
 [ 80,  90],
 [ 90, 100]])

frequencies = np.array([18, 32, 45, 17, 8])
calculator = ExtendedStatisticalCalculator(intervals, frequencies)

calculator.calculate_quartile(3)
calculator.calculate_decile(4)
calculator.calculate_percentile(90)







# List of intervals
# intervals = np.array([
#     [1.65, 1.69],
#     [1.70, 1.74],
#     [1.75, 1.79],
#     [1.80, 1.84],
#     [1.85, 1.89],
#     [1.90, 1.94]
# ])

# # intervals = [
# #     [165, 169],
# #     [170, 174],
# #     [175, 179],
# #     [180, 184],
# #     [185, 189],
# #     [190, 194]
# # ]

# # List of frequencies
# frequencies = np.array([6, 12, 33, 22, 8, 2])

# calculator = ExtendedStatisticalCalculator(intervals, frequencies)

# # a) Determine media, mediana y moda de los datos del puntaje de PSU obtenidos en una generación de un Colegio.
# # b) Determina el cuartil 2 de los datos e interprétalo.
# # c) Determina el decil 8 de los datos e interpreta su valor.

# calculator.calculate_median_with_formula()
# calculator.calculate_mode_with_formula()
# calculator.calculate_arithmetic_mean()
# calculator.calculate_quartile(2)
# calculator.calculate_decile(8)


# intervals = np.array([
#     [350, 399],
#     [400, 449],
#     [450, 499],
#     [500, 549],
#     [550, 599],
#     [600, 649],
#     [650, 699],
#     [700, 749],
#     [750, 799],
#     [800, 849]
# ])

# frequencies = np.array([4, 6, 9, 20, 31, 80, 42, 10, 8, 2])

# calculator = ExtendedStatisticalCalculator(intervals, frequencies)

# calculator.calculate_median_with_formula()
# calculator.calculate_mode_with_formula()
# calculator.calculate_arithmetic_mean()

# # b) Determina el cuartil 3 de los datos e interprétalo.
# # c) Determina el decil 9 de los datos e interpreta su valor.
# # d) Determina el cuartil 2

# print(f"El cuartil 3 de los datos es: {calculator.calculate_quartile(3)}")
# print(f"El decil 9 de los datos es: {calculator.calculate_decile(9)}")
# print(f"El cuartil 2 de los datos es: {calculator.calculate_quartile(2)}")


