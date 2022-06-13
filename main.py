import tkinter as tk

from tablero.tablero_plantilla import TableroPlantilla

#pantilla_tablero = TableroPlantilla(8, 8)
# print(pantilla_tablero.mostrar())


class play():
    def __init__(self, cuadro):
        self.cuadro = cuadro

        self.ventana = tk.Tk()
        self.ventana.title("Ajedrez")
        self.ventana.iconbitmap("")
        self.ventana.geometry(f"{str(cuadro * 8 )}x{str(cuadro * 8 )}")
        self.ventana.resizable(0, 0)

        self.interfaz = tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def crearTablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    self.interfaz.create_rectangle(
                        i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#FFFFFF")
                else:
                    self.interfaz.create_rectangle(
                        i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#000000")


MotorAjedrez = play(80)
MotorAjedrez.crearTablero()

MotorAjedrez()
