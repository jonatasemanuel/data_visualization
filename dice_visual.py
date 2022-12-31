import matplotlib.pyplot as plt
import pygal
from die import Die


# Cria um D6
die_1 = Die()
die_2 = Die()
# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
plt.plot(frequencies)
plt.title('Dice roll', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
