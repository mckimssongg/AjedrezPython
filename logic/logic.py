
from piezas.piezas_obj import (reina_blanca, rey_blanco, torre_blanca_derecha, torre_blanca_izquierda,
                               alfil_blanco_izquierdo, alfil_blanco_derecho,
                               caballo_blanco_izquierdo, caballo_blanco_derecho, peon_uno_B, peon_dos_B, peon_tres_B, peon_cuatro_B,
                               peon_cinco_B, peon_seis_B, peon_siete_B, peon_ocho_B)
import os


def borrarPantalla(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


# borrarPantalla()


class Logic:
    def __init__(self, tablero):
        self.tablero = tablero
        self.piezas = [reina_blanca, rey_blanco, torre_blanca_derecha, torre_blanca_izquierda,
                       alfil_blanco_izquierdo, alfil_blanco_derecho,
                       caballo_blanco_izquierdo, caballo_blanco_derecho, peon_uno_B, peon_dos_B, peon_tres_B, peon_cuatro_B,
                       peon_cinco_B, peon_seis_B, peon_siete_B, peon_ocho_B]

    def obtener_pieza(self, pieza):
        for i in self.piezas:
            if i.nombre == pieza:
                return i

    def accion(self, movimiento=None, pieza=None, cantidad=None):

        comio_pieza = False

        if [self.tablero.mostrar()[x][y]
            for x in range(len(self.tablero.mostrar()))
                for y in range(len(self.tablero.mostrar()[x]))].__contains__(pieza):

            pieza = self.obtener_pieza(pieza)

            if pieza.movimiento_avanzado and cantidad is not None:
                comio_pieza = self.tablero.poner(
                    pieza.movimiento_avanzado(movimiento, cantidad),
                    pieza.nombre
                )
                return comio_pieza

            else:
                comio_pieza = self.tablero.poner(
                    pieza.mover_pieza(movimiento),
                    pieza.nombre
                )

                return comio_pieza

        else:
            print("Esta opcion no existe")
