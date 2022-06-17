import tkinter as tk  # Se importa la libreria tkinter
from tablero_plantilla import play
import posicionesP  # importar archivo de posiciones
from logic.logic import Logic


class ventana():
    def __init__(self, cuadro):
        self.posicion = play  # se impora el rchivo con la clase
        self.cuadro = cuadro
        self.imagenes = {}
        self.ventana = tk.Tk()  # se crea una ventana
        self.motor = Logic(play)
        self.ventana.title("Juego de Ajedrez")  # titulo de la ventana
        # icono de la ventana pendiente
        self.ventana.iconbitmap("./imagenes/icon.ico/")
        # se proporciona la altura y ancho
        self.ventana.geometry(f"{str(cuadro * 8 )}x{str(cuadro * 8+ 55 )}")
        # tamaño fijo de la ventana, evita que se agrande o minimice
        self.ventana.resizable(0, 0)

        # agregarle un input para que el usuario pueda ingresar datos que se pinten en la consola

        self.interfaz = tk.Canvas(self.ventana)  # Permite acceder a graficos
        # para que ocupe toda la ventana
        self.interfaz.pack(fill="both", expand=True)

    def __call__(self):
        self.ventana.mainloop()

    def mover_pieza(self, valor):
        self.motor.accion(movimiento=valor)
        self.posicion.mostrar()
        self.mostrarPiezas()

    def btn_movimiento(self):
        movimiento = tk.StringVar(
            self.ventana, value="Movimiento...", name="movimiento")
        option_movimiento = tk.OptionMenu(self.ventana, movimiento,
                                          "frente", "atras", "derecha", "izquierda", "esq_1", "esq_2", "esq_3", "esq_4", command=self.mover_pieza)
        option_movimiento.pack(padx=10, pady=10)

    def btn_selec_pieza(self):
        select = tk.StringVar(self.ventana, value="Pieza...", name="select")
        # option = tk.OptionMenu(self.ventana, select, "Peon",
        #                        "Caballo", "Alfil", "Torre", "Reina", "Rey", command=self.seleccionar)
        # option.pack(padx=10, pady=10)

    def pintarCuadros(self):
        cuadradoC = 8
        for i in range(cuadradoC):
            for j in range(cuadradoC):
                if (i+j) % 2 == 0:  # 0
                    # 0+0 % 2 = 0 no tiene residuo entra al if y al tener residuo su valor sera uno se dirigira al else
                    self.interfaz.create_rectangle(
                        i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#FFFFFF")
                    # 0 *0 , 0*0, 0, 0,

                else:  # 1
                    self.interfaz.create_rectangle(
                        i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#58A0AD")

    def crearTablero(self):
        self.btn_movimiento()
        self.btn_selec_pieza()
        self.pintarCuadros()

    def importarpiezas(self):
        piezas = ["peonN", "peonB", "caballoN", "caballoB", "alfilN",
                  "alfilB", "torreN", "torreB", "reinaN", "reinaB", "reyN", "reyB"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(
                file="./imagenes/" + pieza + ".png")

    def mostrarPiezas(self):
        self.pintarCuadros()
        for indicea, i in enumerate(self.posicion.mostrar()):  # listas
            for indiceb, j in enumerate(i):  # valores de las listas
                if j != 0:  # al cumplirse la condicion de ser diferente de vacio se crea una pieza de lo contrario sigue
                    self.interfaz.create_image(
                        indiceb*self.cuadro, indicea*self.cuadro, image=self.imagenes[j], anchor="nw")


correventana = ventana(83)
correventana.crearTablero()
correventana.importarpiezas()
correventana.mostrarPiezas()
correventana()
