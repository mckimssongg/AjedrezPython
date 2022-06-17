from piezas.piezas_obj import reina_blanca

import os


def borrarPantalla(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


borrarPantalla()


class Logic:
    def __init__(self, tablero):
        self.tablero = tablero

    def accion(self, movimiento):
        # if select == "reinaB":
        #     movimiento = input("Seleccione movimiento: ")
        if movimiento == "frente":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        elif movimiento == "atras":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        elif movimiento == "izquierda":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()
        elif movimiento == "derecha":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        elif movimiento == "esq_1":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()
        elif movimiento == "esq_2":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        elif movimiento == "esq_3":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        elif movimiento == "esq_4":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
            borrarPantalla()

        else:
            input("Esta opcion no existe")
            borrarPantalla()
        # else:
        #     input("Esta opcion no existe")
        #     borrarPantalla()
