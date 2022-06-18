from piezas.piezas_obj import *
from logic.logic import Logic


class TableroPlantilla:
    '''
    Esta va ser la plantilla donde se mapearan la piezas segun
    su atributo posicion y podra mover las piezas por
    su metodo poner y obtener
    '''

    def __init__(self, filas, columnas):
        '''
        mapeo de las piezas en el tablero
        '''
        self.filas = filas
        self.columnas = columnas

        self.p_init = [reina_blanca, rey_blanco, torre_blanca_derecha, torre_blanca_izquierda,
                       alfil_blanco_izquierdo, alfil_blanco_derecho,
                       caballo_blanco_izquierdo, caballo_blanco_derecho, peon_uno_B, peon_dos_B, peon_tres_B, peon_cuatro_B,
                       peon_cinco_B, peon_seis_B, peon_siete_B, peon_ocho_B,
                       torre_negra_derecha, torre_negra_izquierda,
                       reina_negro, reyNegro,
                       alfil_negro_derecha, alfil_negro_izquierda,
                       caballo_negro_derecha, caballo_negro_izquierda
                       ]

        self.matriz = [[0 for i in range(columnas)] for j in range(filas)]

    def colocarPiezas(self, piezas):
        for i in range(len(piezas)):
            if piezas[i].is_activated:
                self.poner(piezas[i].posicion_actual, piezas[i].nombre)

    def mostrar(self):
        self.matriz = [[0 for i in range(self.columnas)]
                       for j in range(self.filas)]
        self.colocarPiezas(self.p_init)
        return self.matriz

    def poner(self, posicion, valor):
        comio_pieza = True
        try:
            if self.matriz[posicion['x']][posicion['y']] == 0:
                print(self.matriz[posicion['x']][posicion['y']])
                print("sipaso")
                self.matriz[posicion['x']][posicion['y']] = valor
                comio_pieza = False
            if self.matriz[posicion['x']][posicion['y']] != 0:
                print("no paso")

                pieza_actual = self.obtener_pieza(
                    pieza=self.matriz[posicion['x']][posicion['y']])
                pieza_nueva = self.obtener_pieza(pieza=valor)

                if pieza_actual.jugador.color == pieza_nueva.jugador.color:
                    print("Hay otra pieza del mismo color")
                    comio_pieza = False
                else:
                    pieza_actual.change_is_activated()
                    self.matriz[posicion['x']][posicion['y']] = 0
                    self.matriz[posicion['x']][posicion['y']] = valor

                    comio_pieza = True
        except IndexError:
            print("Error")
            self.colocarPiezas(self.p_init)
            print("Error, movimiento fuera del tablero")

        return comio_pieza

    def invertir_matriz(self):
        matriz_invertida = self.mostrar()
        matriz_invertida = matriz_invertida[::-1]
        return matriz_invertida

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_pieza(self, pieza):
        for i in self.p_init:
            if i.nombre == pieza:
                return i


play = TableroPlantilla(8, 8)
