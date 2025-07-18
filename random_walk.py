from random import choice

class RandomWalk:
    """Clase para generar caminatas aleatorias."""

    def __init__(self, num_points=5000):
        """Inicializa los atributos de la caminata."""
        self.num_points = num_points

        # Todas las caminatas empiezan en (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todo los puntos de una caminata."""
        # Sigue tomando pasos hasta que la caminata llega a los puntos deseados.
        while len(self.x_values) < self.num_points:

            # Decide en que direccion ir, y que tan lejos ir.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4,])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rechaza el movimiento que no lleva a ningun lugar.
            if x_step and y_step == 0:
                continue

            # Calcula la nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)