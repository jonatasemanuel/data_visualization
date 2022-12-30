from die import Die
import pygal


# Cria um D6 e um D10
d_six = Die()
d_ten = Die(10)

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = d_six.roll() + d_ten.roll()
    results.append(result)
    frequencies = []

max_result = d_six.num_sides + d_ten.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()
hist.x_labels = ['2', '3', '4', '5', '6','7','8', '9',
                 '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Results'
hist.y_title = 'Frequency of Results'
hist.add('d6 + d10', frequencies)
hist.render_to_file('different_dice.svg')

