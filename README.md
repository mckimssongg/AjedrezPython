# AjedrezPython

  ```python
  
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
        self.matriz = []
        for i in range(filas):
            self.matriz.append([])
            for j in range(columnas):
                self.matriz[i].append(0)

    def mostrar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.matriz[i][j], end=' ')
            print()

    def poner(self, posicion, valor):
        self.matriz[posicion['x']][posicion['y']] = valor

    def obtener(self, posicion):
        return self.matriz[posicion.x][posicion.y]

    def obtener_filas(self):
        return self.filas

    def obtener_columnas(self):
        return self.columnas


pieza = {
    'nombre': 'torre',
    'color': 'blanco',
    'posicion_actual': {
        'x': 7,
        'y': 1,
    },
    'movientos': []
}


taberoajedrez = TableroPlantilla(8, 8)
taberoajedrez.poner(
    {
        'x': 1,
        'y': 1,
    }, 'Reina')
taberoajedrez.mostrar()
print('-'*20)
taberoajedrez.poner(pieza['posicion_actual'], pieza['nombre'])
taberoajedrez.mostrar()

print('-'*20)

pieza = {
    'nombre': 'torre',
    'color': 'blanco',
    'posicion_actual': {
        'x': 1,
        'y': 1,
    },
    'movimientos': [pieza['posicion_actual']]
}

taberoajedrez.poner(pieza['posicion_actual'], pieza['nombre'])

taberoajedrez.mostrar()
print('te comiste una reina')

  ```
