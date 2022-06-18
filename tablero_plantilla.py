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
                       peon_cinco_B, peon_seis_B, peon_siete_B, peon_ocho_B, torre_negra_derecha, torre_negra_izquierda,
                       reina_negro, reyNegro,
                       alfil_negro_derecha, alfil_negro_izquierda,
                       caballo_negro_derecha, caballo_negro_izquierda,
                       peon_uno_N, peon_dos_N, peon_tres_N, peon_cuatro_N, peon_cinco_N, peon_seis_N, peon_siete_N, peon_ocho_N

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
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.matriz[x][y] == 0:
                    self.matriz[posicion['x']][posicion['y']] = valor
                    return False
                if self.matriz[x][y] != 0:
                    # pieza = Logic.obtener_pieza(self.matriz[x][y])
                    # pieza['is_activated'] = False
                    self.matriz[posicion['x']][posicion['y']] = valor
                    return True

    def invertir_matriz(self):
        matriz_invertida = self.mostrar()
        matriz_invertida = matriz_invertida[::-1]
        return matriz_invertida

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_filas(self):
        return self.filas

    def obtener_columnas(self):
        return self.columnas


play = TableroPlantilla(8, 8)
