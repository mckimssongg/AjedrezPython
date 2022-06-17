from piezas.piezas_obj import (reina_blanca, torre_blanca, torre_blanca0, alfil_blanco0,
                                alfil_blanco)

import os


def borrarPantalla(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


borrarPantalla()


class Logic:
    def __init__(self, tablero):
        self.tablero = tablero

    def accion(self, movimiento):
        print(movimiento)
        # if select == "reinaB": #aca se eligira la pieza, "select" debera de ser un parametro de la funcion
        #     movimiento = input("Seleccione movimiento: ")
        if movimiento == "frente":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(torre_blanca.mover_pieza(
                movimiento), torre_blanca.nombre)

            self.tablero.poner(torre_blanca0.mover_pieza(
                movimiento), torre_blanca0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "atras":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(torre_blanca.mover_pieza(
                movimiento), torre_blanca.nombre)

            self.tablero.poner(torre_blanca0.mover_pieza(
                movimiento), torre_blanca0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "izquierda":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(torre_blanca.mover_pieza(
                movimiento), torre_blanca.nombre)

            self.tablero.poner(torre_blanca0.mover_pieza(
                movimiento), torre_blanca0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "derecha":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(torre_blanca.mover_pieza(
                movimiento), torre_blanca.nombre)

            self.tablero.poner(torre_blanca0.mover_pieza(
                movimiento), torre_blanca0.nombre)
#---------------------------------------------------------------------------               
        elif movimiento == "diagDD":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(alfil_blanco0.mover_pieza(
                movimiento), alfil_blanco0.nombre)

            self.tablero.poner(alfil_blanco.mover_pieza(
                movimiento), alfil_blanco0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "diagDU":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(alfil_blanco0.mover_pieza(
                movimiento), alfil_blanco0.nombre)

            self.tablero.poner(alfil_blanco.mover_pieza(
                movimiento), alfil_blanco0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "diagIU":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(alfil_blanco0.mover_pieza(
                movimiento), alfil_blanco0.nombre)

            self.tablero.poner(alfil_blanco.mover_pieza(
                movimiento), alfil_blanco0.nombre)
#---------------------------------------------------------------------------
        elif movimiento == "diagID":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

            self.tablero.poner(alfil_blanco0.mover_pieza(
                movimiento), alfil_blanco0.nombre)

            self.tablero.poner(alfil_blanco.mover_pieza(
                movimiento), alfil_blanco0.nombre)
#---------------------------------------------------------------------------
                
        else:
            input("Esta opcion no existe")
            borrarPantalla()
        # else:
        #     input("Esta opcion no existe")
        #     borrarPantalla()
