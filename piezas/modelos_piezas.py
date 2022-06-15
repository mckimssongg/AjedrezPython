class Jugador:
    '''
    Las instancias de esta clase nos serviran para
    de que jugador seran las piezas

    #Parametros:
    color               --->    (string) color de las piezas del jugador
    '''

    def __init__(self, color):
        self.color = color


class PiezaBase:
    '''
    Esta clase servira para instanciae las piezas basicas tales como:
    Peon, Rey, Caballo.

    #Parametros:
    jugador             --->    (object) instancia de una clase jugador al que se asociaran
    nombre              --->    (string) nombre de la pieza
    posicion_inicial    --->    (diccionario) diccionario con las coordenadas
                                de la posicion inicial del jugador
    movimientos         --->    (diccionario) diccionario con todos los movimientos 
                                de la pieza
    '''

    def __init__(self, jugador, nombre, posicion_inicial, movimientos):
        self.jugador = jugador
        self.nombre = nombre
        self.posicion_actual = posicion_inicial
        self.movimientos = movimientos

    def mover_pieza(self, nombre_movimiento):
        '''
        Esta funcion nos servira para mover las piezas

        #Parametros:
        nombre_movimiento   --->    (string) nombre del movimiento que se desea realizar
        '''
        movimiento = self.movimientos[nombre_movimiento]

        predic = {
            "x": self.posicion_actual['x'] + movimiento['x'],
            "y": self.posicion_actual['y'] + movimiento['y']
        }

        if (predic['x'] < 8 and predic['y'] < 8 and predic['x'] >= 0 and predic['y'] >= 0):
            self.posicion_actual['x'] += movimiento['x']
            self.posicion_actual['y'] += movimiento['y']
        else:
            print(f"Posicion/movimiento de {self.nombre} no valida")

        return self.posicion_actual

    def __str__(self):
        return self.nombre


class PiezaEspecial(PiezaBase):  # Pendiente a cambios
    '''
    Esta clase servira para instanciae las piezas especiales tales como:
    Reina, Alfil, Torre. Esta class hereda de la clase PiezaBase y ademas
    tiene un metodo para moverse en diagonal y en linea recta dependiendo
    '''

    def __init__(self, jugador, nombre, posicion_inicial, movimientos):
        super().__init__(jugador, nombre, posicion_inicial, movimientos)

    def movimiento_avanzado(self,pieza, nombre_movimiento, cantidad, direccion):
        '''
        Este metodo nos servira para que las piezas especiales (reina, alfil, torre)
        -puedan moverse en diagonal
        -puedan moverse en linea recta

        #Parametros:
        pieza               --->    (object) instancia de una clase pieza
        nombre_movimiento   --->    (string) nombre del movimiento que se desea realizar
        cantidad            --->    (int) cantidad de casillas que se desea mover
        direccion           --->    (string) direccion en la que se desea mover
        '''
        movimiento = pieza['movimientos'][nombre_movimiento]

        if direccion == 'diagonal':
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
        else:
            if self.jugador.color == 'blanco':

                for i in range(cantidad):
                    pieza['posicion_actual']['x'] = (
                        pieza['posicion_actual']['x'] + movimiento['x'])
                    pieza['posicion_actual']['y'] = (
                        pieza['posicion_actual']['y'] + movimiento['y'])

                return pieza['posicion_actual']

            if self.jugador.color == 'negro':

                for i in range(cantidad):
                    pieza['posicion_actual']['x'] = (
                        pieza['posicion_actual']['x'] - movimiento['x'])
                    pieza['posicion_actual']['y'] = (
                        pieza['posicion_actual']['y'] - movimiento['y'])

                return pieza['posicion_actual']
