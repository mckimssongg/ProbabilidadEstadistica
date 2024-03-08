import numpy as np

class StatisticalCalculator:
    def __init__(self, intervals, frequencies):
        self.intervals = intervals
        self.frequencies = frequencies
        self.midpoints = np.mean(self.intervals, axis=1)
        self.cumulative_frequencies = np.cumsum(self.frequencies)
        self.total_observations = self.cumulative_frequencies[-1]
        
    def calculate_mean(self):
        return np.sum(self.midpoints * self.frequencies) / self.total_observations
    
    def find_value_at_position(self, position):
        interval_index = np.where(self.cumulative_frequencies >= position)[0][0]
        interval = self.intervals[interval_index]
        F_lower = self.cumulative_frequencies[interval_index - 1] if interval_index != 0 else 0
        f_value = self.frequencies[interval_index]
        return (interval[0] + ((position - F_lower) / f_value) * (interval[1] - interval[0]))
    
    def calculate_median(self):
        median_position = 0.5 * self.total_observations
        return self.find_value_at_position(median_position)
    
    def calculate_mode(self):
        return self.intervals[self.frequencies.argmax()]
    
    def calculate_quartile(self, quartile_number):
        if quartile_number not in [1, 2, 3]:
            raise ValueError("Quartile number must be 1, 2, or 3")
        quartile_position = (quartile_number * 0.25) * self.total_observations
        return self.find_value_at_position(quartile_position)
    
    def calculate_percentile(self, percentile):
        if not 0 <= percentile <= 100:
            raise ValueError("Percentile must be between 0 and 100")
        percentile_position = (percentile / 100) * self.total_observations
        return self.find_value_at_position(percentile_position)

class ExtendedStatisticalCalculator(StatisticalCalculator):
    def __init__(self, intervals, frequencies):
        super().__init__(intervals, frequencies)
        self.class_widths = self.intervals[:, 1] - self.intervals[:, 0] + 1
            
    def calculate_decile(self, decile_number):
        if not 1 <= decile_number <= 9:
            raise ValueError("Decile number must be between 1 and 9")
        decile_position = (decile_number * 0.1) * self.total_observations
        return self.find_value_at_position(decile_position)

    def calculate_quintile(self, quintile_number):
        if not 1 <= quintile_number <= 4:
            raise ValueError("Quintile number must be between 1 and 4")
        quintile_position = (quintile_number * 0.2) * self.total_observations
        return self.find_value_at_position(quintile_position)
    
    def calculate_arithmetic_mean(self):
        return np.sum(self.frequencies * self.midpoints) / np.sum(self.frequencies)
    
    def calculate_median_with_formula(self):
        median_position = 0.5 * self.total_observations
        median_interval_index = np.where(self.cumulative_frequencies >= median_position)[0][0]
        L = self.intervals[median_interval_index, 0]  # Límite real inferior
        F = self.cumulative_frequencies[median_interval_index - 1] if median_interval_index != 0 else 0
        f = self.frequencies[median_interval_index]
        c = self.class_widths[median_interval_index]
        return L + (((median_position - F) / f) * c)
    
    def calculate_mode_with_formula(self):
        modal_class_index = self.frequencies.argmax()
        L = self.intervals[modal_class_index, 0] - 0.5 # Límite real inferior
        delta1 = self.frequencies[modal_class_index] - self.frequencies[modal_class_index - 1]
        delta2 = self.frequencies[modal_class_index] - self.frequencies[modal_class_index + 1]
        c = self.class_widths[modal_class_index]
        return L + ((delta1 / (delta1 + delta2)) * c)



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
