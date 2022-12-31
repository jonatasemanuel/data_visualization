import pygal
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
# Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    # Define o tamanho da janela de plotagem
    plt.figure(dpi=80, figsize=(10, 9))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
    #             cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.plot(point_numbers, rw.x_values, rw.y_values, linewidth=5)
    # Enfatiza o primeiro e o último ponto 
    """plt.plot(0, 0, c='green', edgecolors='none', s=100)
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=100)"""
    # Remove os eixos
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    #plt.show()
    hist = pygal.Bar()
    hist.title = f'Results of random walk'
    hist.x_title = 'Results'
    hist.y_title = 'Frequency of Results'
    hist.add('Randow Walk', rw.x_values)
    hist.add('Randow Walk', rw.y_values)
    hist.render_to_file('rw_visual.svg')
    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running in 'n N':
       break
