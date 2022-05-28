class Jugador:
    '''
    Las instancias de esta clase nos serviran para
    de que jugador seran las piezas

    Parametros:
    color ----> (string) color de las piezas del jugador
    '''

    def __init__(self, color):
        self.color = color


class PiezaBase:
    '''
    Esta clase servira para instanciae las piezas basicas tales como:
    Peon, Rey, Caballo.

    Parametros:
    jugador             --->    (object) instancia de una clase jugador al que se asociaran
    nombre              --->    (string) nombre de la pieza
    posicion_inicial    --->    (diccionario) diccionario con las coordenadas
                                de la posicion inicial del jugador
    movimientos         --->    (diccionario) diccionario con todos los movimientos 
                                de la pieza
    '''

    def __init__(self, jugador, nombre, posicion_inicial, movimientos):
        self.jugador = jugador
        self.posicion_actual = posicion_inicial
        self.movimientos = movimientos

    def mover_pieza(self, pieza, nombre_movimiento):
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


class PiezaEspecial(PiezaBase):
    '''
    Esta clase servira para instanciae las piezas especiales tales como:
    Reina, Alfil, Torre. Esta class hereda de la clase PiezaBase y ademas
    tiene un metodo para moverse en diagonal y en linea recta dependiendo
    '''

    def __init__(self, jugador, nombre, posicion_inicial, movimientos):
        super().__init__(jugador, nombre, posicion_inicial, movimientos)

    def movimiento_avanzado(self, pieza, nombre_movimiento, cantidad):
        '''
        Este metodo nos servira para que las piezas especiales (reina, alfil, torre)
        -puedan moverse en diagonal
        -puedan moverse en linea recta
        '''
        movimiento = pieza['movimientos'][nombre_movimiento]

        if self.jugador.color == 'blanco':

            pieza['posicion_actual']['x'] = (
                pieza['posicion_actual']['x'] + movimiento['x'] * cantidad)

            pieza['posicion_actual']['y'] = (
                pieza['posicion_actual']['y'] + movimiento['y'] * cantidad)

            return pieza['posicion_actual']

        if self.jugador.color == 'negro':

            pieza['posicion_actual']['x'] = (
                pieza['posicion_actual']['x'] - movimiento['x'] * cantidad)

            pieza['posicion_actual']['y'] = (
                pieza['posicion_actual']['y'] - movimiento['y'] * cantidad)

            return pieza['posicion_actual']
