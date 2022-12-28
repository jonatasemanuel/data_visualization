import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
# Define o título do gráfico e nomeia os eixos
plt.title('Square Numbers', fontsize=14)
# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)
plt.show()

