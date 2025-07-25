from random import choice

class RandomWalk:
    """Una clase que genera caminatas random"""

    def __init__(self, num_points=5000):
        """Inicializo los atributos de la caminata."""
        self.num_points = num_points

        # Todas las caminatas empiezan en (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Calcula los puntos de los pasos."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


    def fill_walk(self):
        """Calcula todos los puntos en una caminata."""
        # Sigue contando los pasos hasta que llegue a la cantidad deseada.
        while len(self.x_values) < self.num_points:

            # Decide en que direccion ir, y que tan lejos ir.
            x_step = self.get_step()
            y_step = self.get_step()

            # Rechaza movimientos que no van a ningun lado.
            if x_step == 0 and y_step == 0:
                continue

            # Calcula la nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
