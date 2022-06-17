from piezas.piezas_obj import reina_blanca

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

        elif movimiento == "atras":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

        elif movimiento == "izquierda":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
        elif movimiento == "derecha":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

        elif movimiento == "esq_1":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)
        elif movimiento == "esq_2":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

        elif movimiento == "esq_3":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

        elif movimiento == "esq_4":
            self.tablero.poner(reina_blanca.mover_pieza(
                movimiento), reina_blanca.nombre)

        else:
            input("Esta opcion no existe")
            borrarPantalla()
        # else:
        #     input("Esta opcion no existe")
        #     borrarPantalla()
