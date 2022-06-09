try:
    import tkinter as tk 
    from tkinter import ttk
except ImportError:
    import Tkinter as tk 

from tablero.tablero_plantilla import TableroPlantilla

pantilla_tablero = TableroPlantilla(8, 8)

print(pantilla_tablero.mostrar())


