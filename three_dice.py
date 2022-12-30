import pygal
from die import Die 


die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = f'Results of rollings three d6 {len(results)} times.'
hist.x_labels = []
for num_guess in range(3, max_result+1):
    hist.x_labels.append(num_guess)
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'
hist.add('d6 + d6 + d6', frequencies)
hist.render_to_file('three_dice.svg')

