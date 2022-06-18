import tkinter as tk  # Se importa la libreria tkinter
from tablero_plantilla import play as tb
from logic.logic import Logic


class ventana():
    def __init__(self, cuadro):
        self.posicion = tb  # se impora el rchivo con la clase
        self.cuadro = cuadro
        self.imagenes = {}
        self.ventana = tk.Tk()  # se crea una ventana
        self.motor = Logic(self.posicion)
        self.ventana.title("Juego de Ajedrez")  # titulo de la ventana
        # icono de la ventana pendiente
        self.ventana.iconbitmap("./imagenes/icon.ico/")
        # se proporciona la altura y ancho
        self.ventana.geometry(
            f"{str(cuadro * 8 )}x{str(cuadro * 8+ 55)}")
        # tamaño fijo de la ventana, evita que se agrande o minimice
        self.ventana.resizable(0, 0)
        self.interfaz = tk.Canvas(self.ventana)  # Permite acceder a graficos
        # para que ocupe toda la ventana
        self.interfaz.pack(fill="both", expand=True)

        self.pieza_seleccionada = tk.StringVar(
            self.ventana, value="pieza", name=None)

        self.movimiento_seleccionado = tk.StringVar(
            self.ventana, value="Movimiento...", name=None)

        self.cant_casillas = tk.IntVar(
            self.ventana, value="Cantidad de casillas...", name=None)

        self.Change_Tablero = True

    def __call__(self):
        self.ventana.mainloop()

    def seleccionar(self, valor):
        self.pieza_seleccionada.set(value=valor)

    def mover_pieza(self, valor):
        self.movimiento_seleccionado.set(value=valor)

    def casillas_cantidad(self, valor):
        self.cant_casillas.set(value=valor)

    def btn_select_movimiento(self):
        option_movimiento = tk.OptionMenu(self.ventana, self.movimiento_seleccionado,
                                          "frente", "atras", "derecha", "izquierda",  "diagIU", "diagDU",  "diagDD", "diagID", command=self.mover_pieza)
        option_movimiento.pack(padx=10, pady=10, side="left")

    def btn_selec_pieza(self):
        option = tk.OptionMenu(self.ventana, self.pieza_seleccionada, "Peon",
                               "Caballo", "Alfil", "Torre", "reinaB", "Rey", command=self.seleccionar)
        option.pack(padx=10, pady=10, side="right")

    def btn_select_cantidad(self):
        option_cantidad = tk.OptionMenu(self.ventana, self.cant_casillas,
                                        1, 2, 3, 4, 5, 6, 7, command=self.casillas_cantidad)
        option_cantidad.pack(padx=10, pady=10, side="left")

    def moverPieza(self):
        comio_pieza = self.motor.accion(
            movimiento=self.movimiento_seleccionado.get(),
            pieza=self.pieza_seleccionada.get(),
            cantidad=self.cant_casillas.get(),
        )
        if comio_pieza:
            self.posicion.invertir_matriz()
            self.mostrarPiezas()
        else:
            self.posicion.mostrar()
            self.mostrarPiezas()

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
        self.btn_select_movimiento()
        self.btn_selec_pieza()
        self.btn_select_cantidad()
        self.pintarCuadros()
        boton = tk.Button(
            self.ventana, text="Mover", command=lambda: self.moverPieza(), bg="#318A9B", fg="#FFFFFF")

        boton.pack(padx=10, pady=10, )

    def importarpiezas(self):
        piezas = ["peonN", "peonB", "caballoN", "caballoB", "alfilN",
                  "alfilB", "torreN", "torreB", "reinaN", "reinaB", "reyN", "reyB"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(
                file="./imagenes/" + pieza + ".png")

    def mostrarPiezas(self):
        self.pintarCuadros()

        if self.Change_Tablero:
            tablero_matriz = self.posicion.mostrar()
            self.Change_Tablero = not self.Change_Tablero
        else:
            tablero_matriz = self.posicion.invertir_matriz()
            self.Change_Tablero = not self.Change_Tablero

        for indicea, i in enumerate(tablero_matriz):  # listas
            for indiceb, j in enumerate(i):  # valores de las listas
                if j != 0:  # al cumplirse la condicion de ser diferente de vacio se crea una pieza de lo contrario sigue
                    self.interfaz.create_image(
                        indiceb*self.cuadro, indicea*self.cuadro, image=self.imagenes[j], anchor="nw")


correventana = ventana(83)
correventana.crearTablero()
correventana.importarpiezas()
correventana.mostrarPiezas()
correventana()
