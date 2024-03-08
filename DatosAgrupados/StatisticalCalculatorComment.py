import numpy as np

class StatisticalCalculator:
    def __init__(self, intervals, frequencies):
        self.intervals = intervals
        self.frequencies = frequencies
        self.midpoints = np.mean(self.intervals, axis=1)
        self.cumulative_frequencies = np.cumsum(self.frequencies)
        self.total_observations = self.cumulative_frequencies[-1]
        print(f"Total de observaciones (Total observations) = {self.total_observations}")
        print(f"Intervalos (Intervals) = {self.intervals}")
        print(f"Frecuencias (Frequencies) = {self.frequencies}")
        print(f"Suma de frecuencias (Sum of frequencies) = {np.sum(self.frequencies)}")
        print(f"Suma de frecuencias acumuladas (Sum of cumulative frequencies) = {np.sum(self.cumulative_frequencies)}")
        print(f"Suma de midpoints * frecuencias (Sum of midpoints * frequencies) = {np.sum(self.midpoints * self.frequencies)}")
        
    
    def calculate_mean(self):
        # Fórmula de la media: \bar{x} = \sum (f_i \cdot x_i) / \sum f_i
        mean_calculation = np.sum(self.midpoints * self.frequencies) / np.sum(self.frequencies)
        print(f"Media (Mean) = Sum(midpoints * frequencies) / Sum(frequencies)")
        print(f"             = {np.sum(self.midpoints * self.frequencies)} / {np.sum(self.frequencies)}")
        print(f"             = {mean_calculation}")
        return mean_calculation
    
    def find_value_at_position(self, position, description):
        # Encuentra el valor en una posición específica para calcular mediana, cuartiles y percentiles
        interval_index = np.where(self.cumulative_frequencies >= position)[0][0]
        L = self.intervals[interval_index][0]
        F = self.cumulative_frequencies[interval_index - 1] if interval_index != 0 else 0
        f = self.frequencies[interval_index]
        c = self.intervals[interval_index][1] - L
        value = L + ((position - F) / f) * c
        print(f"{description} = L + ((position - F) / f) * c")
        print(f"              = {L} + (({position} - {F}) / {f}) * {c}")
        print(f"              = {value}")
        return value
    
    def calculate_median(self):
        # La mediana es el valor en la posición n/2
        median_position = 0.5 * self.total_observations
        return self.find_value_at_position(median_position, "Mediana (Median)")
    
    def calculate_mode(self):
        # La moda es el intervalo con la mayor frecuencia
        mode_interval_index = self.frequencies.argmax()
        mode_interval = self.intervals[mode_interval_index]
        L = mode_interval[0]
        f_mode = self.frequencies[mode_interval_index]
        f_previous = self.frequencies[mode_interval_index - 1] if mode_interval_index != 0 else 0
        f_next = self.frequencies[mode_interval_index + 1] if mode_interval_index < len(self.frequencies) - 1 else 0
        c = mode_interval[1] - L
        mode = L + ((f_mode - f_previous) / ((f_mode - f_previous) + (f_mode - f_next))) * c
        print(f"Moda (Mode) = L + ((f_mode - f_previous) / ((f_mode - f_previous) + (f_mode - f_next))) * c")
        print(f"             = {L} + (({f_mode} - {f_previous}) / (({f_mode} - {f_previous}) + ({f_mode} - {f_next}))) * {c}")
        print(f"             = {mode}")
        return mode
    
    def calculate_quartile(self, quartile_number):
        # Los cuartiles son valores que dividen los datos en cuatro partes iguales
        quartile_position = (quartile_number * 0.25) * self.total_observations
        return self.find_value_at_position(quartile_position, f"Cuartil {quartile_number} (Quartile {quartile_number})")
    
    def calculate_percentile(self, percentile):
        # Los percentiles son valores que dividen los datos en cien partes iguales
        percentile_position = (percentile / 100) * self.total_observations
        return self.find_value_at_position(percentile_position, f"Percentil {percentile} (Percentile {percentile})")

class ExtendedStatisticalCalculator(StatisticalCalculator):
    def __init__(self, intervals, frequencies):
        super().__init__(intervals, frequencies)
        self.class_widths = self.intervals[:, 1] - self.intervals[:, 0] + 1
    
    def calculate_decile(self, decile_number):
        # Los deciles son valores que dividen los datos en diez partes iguales
        decile_position = (decile_number * 0.1) * self.total_observations
        return self.find_value_at_position(decile_position, f"Decil {decile_number} (Decile {decile_number})")
    
    def calculate_quintile(self, quintile_number):
        # Los quintiles son valores que dividen los datos en cinco partes iguales
        quintile_position = (quintile_number * 0.2) * self.total_observations
        return self.find_value_at_position(quintile_position, f"Quintil {quintile_number} (Quintile {quintile_number})")
    
    # Este método calcula la media aritmética y muestra todo el procedimiento
    def calculate_arithmetic_mean(self):
        mean_calculation = np.sum(self.midpoints * self.frequencies) / np.sum(self.frequencies)
        print(f"Media Aritmética (Arithmetic Mean) = Σ(midpoints * frequencies) / Σ(frequencies)")
        print(f"                                = {np.sum(self.midpoints * self.frequencies)} / {np.sum(self.frequencies)}")
        print(f"                                = {mean_calculation}")
        return mean_calculation
    
    # Este método calcula la mediana con la fórmula y muestra todo el procedimiento
    def calculate_median_with_formula(self):
        median_position = 0.5 * self.total_observations
        median_interval_index = np.where(self.cumulative_frequencies >= median_position)[0][0]
        L = self.intervals[median_interval_index, 0]  # Límite real inferior
        F = self.cumulative_frequencies[median_interval_index - 1] if median_interval_index != 0 else 0
        f = self.frequencies[median_interval_index]
        c = self.intervals[median_interval_index, 1] - L
        median = L + (((median_position - F) / f) * c)
        print(f"Mediana (Median) = L + [(n/2 - F) / f] * c")
        print(f"                = {L} + [({median_position} - {F}) / {f}] * {c}")
        print(f"                = {median}")
        return median
    
    # Este método calcula la moda con la fórmula y muestra todo el procedimiento
    def calculate_mode_with_formula(self):
        modal_class_index = self.frequencies.argmax()
        L = self.intervals[modal_class_index, 0]  # Límite real inferior
        delta1 = self.frequencies[modal_class_index] - (self.frequencies[modal_class_index - 1] if modal_class_index != 0 else 0)
        delta2 = self.frequencies[modal_class_index] - (self.frequencies[modal_class_index + 1] if modal_class_index < len(self.frequencies) - 1 else 0)
        c = self.intervals[modal_class_index, 1] - L
        mode = L + ((delta1 / (delta1 + delta2)) * c)
        print(f"Moda (Mode) = L + (Δ1 / (Δ1 + Δ2)) * c")
        print(f"            = {L} + ({delta1} / ({delta1} + {delta2})) * {c}")
        print(f"            = {mode}")
        return mode


# # Datos de los intervalos y sus frecuencias absolutas
# intervals = np.array([[350, 399], [400, 449], [450, 499], [500, 549],
#                       [550, 599], [600, 649], [650, 699], [700, 749],
#                       [750, 799], [800, 849]])
# frequencies = np.array([4, 6, 9, 20, 31, 80, 42, 10, 8, 2])

# # Crear la instancia de la clase con los datos de intervalos y frecuencias
# stat_calc = ExtendedStatisticalCalculator(intervals, frequencies)

# # Obtener los resultados
# mean = stat_calc.calculate_mean()
# median = stat_calc.calculate_median()
# mode = stat_calc.calculate_mode()
# quartile1 = stat_calc.calculate_quartile(1)
# quartile2 = stat_calc.calculate_quartile(2)
# quartile3 = stat_calc.calculate_quartile(3)
# percentile90 = stat_calc.calculate_percentile(90)
# decile1 = stat_calc.calculate_decile(1)
# decile5 = stat_calc.calculate_decile(5)
# decile9 = stat_calc.calculate_decile(9)
# median_with_formula = stat_calc.calculate_median_with_formula()
# mode_with_formula = stat_calc.calculate_mode_with_formula()
# mean_with_formula = stat_calc.calculate_arithmetic_mean()
