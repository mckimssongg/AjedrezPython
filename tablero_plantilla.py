from piezas.piezas_obj import *


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
        self.p_init = [reina_blanca, torre_blanca,
                       torre_blanca0, alfil_blanco0]
        self.matriz = [[0 for i in range(columnas)] for j in range(filas)]

    def colocarPiezas(self, piezas):
        for i in range(len(piezas)):
            self.poner(piezas[i].posicion_actual, piezas[i].nombre)

    def mostrar(self):
        self.matriz = [[0 for i in range(self.columnas)]
                       for j in range(self.filas)]
        self.colocarPiezas(self.p_init)

        # matrizfomateada = f"""
        # {self.matriz[0]}
        # {self.matriz[1]}
        # {self.matriz[2]}
        # {self.matriz[3]}
        # {self.matriz[4]}
        # {self.matriz[5]}
        # {self.matriz[6]}
        # {self.matriz[7]}
        # """
        # print(matrizfomateada)
        return self.matriz

    def poner(self, posicion, valor):
        for x in range(self.filas):
            for y in range(self.columnas):
                if self.matriz[x][y] == 0:
                    self.matriz[posicion['x']][posicion['y']] = valor

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_filas(self):
        return self.filas

    def obtener_columnas(self):
        return self.columnas


play = TableroPlantilla(8, 8)
