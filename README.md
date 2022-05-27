# AjedrezPython
:)
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
    'nombre': 'caballo',
    'color': 'blanco',
    'posicion_actual': {
        'x': 7,
        'y': 1,
    },
    'movimientos': {
        'primer_tipo_moviento': {
            'x': -2,
            'y': 1,
        },  # primer_tipo_moviento simula el movimiento en L de un caballo
        'segundo_tipo_moviento': {
            'x': -1,
            'y': 2,
        },
    }
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


def mover_pieza(pieza, nombre_movimiento=None):
    movimiento = pieza['movimientos'][nombre_movimiento]

    pieza['posicion_actual']['x'] = (
        pieza['posicion_actual']['x'] + movimiento['x'])

    pieza['posicion_actual']['y'] = (
        pieza['posicion_actual']['y'] + movimiento['y'])

    return pieza['posicion_actual']


print(pieza['posicion_actual'])

taberoajedrez.poner(
    mover_pieza(pieza, 'primer_tipo_moviento'), pieza['nombre'])

print(pieza['posicion_actual'])

taberoajedrez.mostrar()

  ```
