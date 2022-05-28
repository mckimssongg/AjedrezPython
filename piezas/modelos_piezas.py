class Jugador:
    '''

    '''

    def __init__(self, color):
        self.color = color


class PiezaBase:
    def __init__(self, jugador, nombre, posicion_inicial, movimientos):
        self.jugador = jugador
        self.posicion_actual = posicion_inicial
        self.movimientos = movimientos

    def mover_pieza(pieza, nombre_movimiento=None):
        movimiento = pieza['movimientos'][nombre_movimiento]

        if self.jugador.color == 'blancas':

            pieza['posicion_actual']['x'] = (
                pieza['posicion_actual']['x'] + movimiento['x'])

            pieza['posicion_actual']['y'] = (
                pieza['posicion_actual']['y'] + movimiento['y'])

            return pieza['posicion_actual']

        if self.jugador.color == 'negro':

            pieza['posicion_actual']['x'] = (
                pieza['posicion_actual']['x'] - movimiento['x'])

            pieza['posicion_actual']['y'] = (
                pieza['posicion_actual']['y'] - movimiento['y'])

            return pieza['posicion_actual']


class PiezaEspecial:
    pass
