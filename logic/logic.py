import os
from piezas.piezas_obj import (reina_blanca, torre_blanca, torre_blanca0, alfil_blanco0,
                               alfil_blanco)


def borrarPantalla(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


# borrarPantalla()


class Logic:
    def __init__(self, tablero):
        self.tablero = tablero
        self.piezas = [reina_blanca, torre_blanca, torre_blanca0, alfil_blanco0,
                       alfil_blanco]

    def obtener_pieza(self, pieza):
        for i in self.piezas:
            if i.nombre == pieza:
                return i

    def accion(self, movimiento=None, pieza=None, cantidad=None):

        comio_prieza = False

        if [self.tablero.mostrar()[x][y]
            for x in range(len(self.tablero.mostrar()))
                for y in range(len(self.tablero.mostrar()[x]))].__contains__(pieza):

            pieza = self.obtener_pieza(pieza)

            if pieza.movimiento_avanzado and cantidad is not None:
                comio_prieza = self.tablero.poner(
                    pieza.movimiento_avanzado(movimiento, cantidad),
                    pieza.nombre
                )

            else:
                comio_prieza = self.tablero.poner(
                    pieza.mover_pieza(movimiento),
                    pieza.nombre
                )

        else:
            print("Esta opcion no existe")

        return comio_prieza
