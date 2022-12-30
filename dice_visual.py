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
hist = pygal.Bar()
hist.title = 'Results of rollings one D6 1000 times.'
hist.x_labels = []
for num_guess in range(2, max_result+1):
    hist.x_labels.append(num_guess)
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')

