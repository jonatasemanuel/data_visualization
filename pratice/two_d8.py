import pygal
from die import Die 


die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(90000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = f'Results of rollings two d8 {len(results)} times.'
hist.x_labels = []
for num_guess in range(2, max_result+1):
    hist.x_labels.append(num_guess)
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'
hist.add('d8 + d8', frequencies)
hist.render_to_file('two_d8.svg')

