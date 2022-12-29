from random import choice


class RandomWalk():
    """Um a classe para gerar passeios aleatórios"""
    def __init__(self, num_points=5000) -> None:
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points
        # Todos os passeios começam em (0, 0)
        self.x_values, self.y_values = [0], [0]

    def get_step(self, direction, distance):
            step = direction * distance
            return step

    def fill_walk(self):
        """Calcula todos os pontos do passeio."""
        # Continua dando passos até que o passeio alcance o tamanho desejado
        while len(self.x_values) < self.num_points:
            # Decide direção a ser seguida e distância a ser percorrida nessa direção
            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            # x_step = x_direction * x_distance
            x_step = get_step()
            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = get_step()
            # y_step = y_direction * y_distance
            # Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0:
                continue
            # Calcula os próximos valores de x e de y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

