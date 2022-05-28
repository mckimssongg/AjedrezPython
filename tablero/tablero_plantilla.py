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
        self.matriz = []
        for i in range(8):
            self.matriz.append([])
            for j in range(8):
                self.matriz[i].append(0)

    def mostrar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j]
        return self.matriz

    def poner(self, posicion, valor):
        self.matriz[posicion['x']][posicion['y']] = valor

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_filas(self):
        return self.filas

    def obtener_columnas(self):
        return self.columnas
