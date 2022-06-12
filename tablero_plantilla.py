import os
borrarPantalla = lambda: os.system("cls")
borrarPantalla()

from piezas.piezas_obj import *

class TableroPlantilla:
    '''
    Esta va ser la plantilla donde se mapearan la piezas segun
    su atributo posicion y podra mover las piezas por
    su metodo poner y obtener

    [
        ["torre", "alfil", "caballo", "reina", "rey", "caballo", "alfil", "torre"],
        ["peon", "peon", "peon", "peon", "peon", "peon", "peon", "peon"],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    '''

    def __init__(self, filas, columnas):
        '''
        mapeo de las piezas en el tablero
        '''
        self.filas = filas
        self.columnas = columnas
        self.matriz = [ [0 for i in range(columnas)] for j in range(filas) ]
        
    def colocarPiezas(self, piezas):
        for pieza in piezas:
            self.poner(pieza.posicion_actual, pieza.nombre)
            
    def mostrar(self):
        p_init = [reina_blanca]
        self.colocarPiezas(p_init)
        
        matrizfomateada = f"""
        {self.matriz[0]}
        {self.matriz[1]}
        {self.matriz[2]}
        {self.matriz[3]}
        {self.matriz[4]}
        {self.matriz[5]}
        {self.matriz[6]}
        {self.matriz[7]}
        """
        print(matrizfomateada)
        #return self.matriz

    def poner(self, posicion, valor):
        self.matriz = [ [0 for i in range( self.columnas )] for j in range( self.filas ) ]
        self.matriz[posicion['x']][posicion['y']] = valor

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_filas(self):
        return self.filas

    def obtener_columnas(self):
        return self.columnas


play = TableroPlantilla(8, 8)

end = False
while not end:
    print("\n")
    play.mostrar()
    print("\n")
    op = input("Siguiente accion: ")
    if op == "bye":
        end = True
        input('Bye')
    elif op == "mover":
        select = input("Seleccione pieza: ")
        movimiento = input("Seleccione movimiento: ")
        if select == "reina_b":
            if movimiento == "frente":
                play.poner(reina_blanca.mover_pieza(movimiento), "reina_b")
                borrarPantalla()
            else:
                input("Esta opcion no existe")
                borrarPantalla()
        else:
            input("Esta opcion no existe")
            borrarPantalla()
    
    else:
        input("Esta opcion no existe")
        borrarPantalla()