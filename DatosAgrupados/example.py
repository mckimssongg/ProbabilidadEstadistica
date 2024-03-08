from StatisticalCalculatorComment import ExtendedStatisticalCalculator
import numpy as np

# Datos de los intervalos y sus frecuencias absolutas
intervals = np.array([[20, 28],
                      [28, 36],
                      [36, 44],
                      [44, 52],
                      [52, 60],
                      [60, 68]])
frequencies = np.array([3,9,15,18,8,5])

calculator = ExtendedStatisticalCalculator(intervals, frequencies)

# ¿Cuantos abdominales como máximo logro hacer el 25% del total de los estudiantes con rendimiento mas bajo?

print(f"El 25% de los estudiantes con rendimiento mas bajo lograron hacer {calculator.calculate_quartile(1)} abdominales como máximo")

# ¿Cuantos abdominales como mínimo realizaron el 50% de los estudiantes con mejor rendimiento?

print(f"El 50% de los estudiantes con mejor rendimiento lograron hacer {calculator.calculate_quartile(2)} abdominales como mínimo")

# ¿Cuantos abdominales como mínimo hicieron los estudiantes que se encuentran en el 10% con mejor rendimiento?

print(f"El 10% de los estudiantes con mejor rendimiento lograron hacer {calculator.calculate_decile(9)} abdominales como mínimo")

