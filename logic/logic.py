from piezas.piezas_obj import (reina_blanca, torre_blanca, torre_blanca0, alfil_blanco0,
                               alfil_blanco)
import os


def borrarPantalla(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


borrarPantalla()


class Logic:
    def __init__(self, tablero):
        self.tablero = tablero

    def accion(self, movimiento=None, pieza=None):

        if pieza is self.tablero.mostrar():
            if pieza.movimiento_avanzado:
                self.tablero.poner(pieza.mover_pieza, pieza.nombre)
        else:
            print("Esta opcion no existe")
