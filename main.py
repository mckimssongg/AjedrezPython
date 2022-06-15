import tkinter as tk # Se importa la libreria tkinter
import posicionesP #importar archivo de posiciones

class ventana():
    def __init__(self, cuadro):
        self.posicion = posicionesP.juego () #se impora el rchivo con la clase
        self.cuadro = cuadro
        self.imagenes = {} 
       
        self.ventana = tk.Tk() # se crea una ventana
        self.ventana.title("Juego de Ajedrez") # titulo de la ventana
        self.ventana.iconbitmap("./imagenes/icon.ico/") # icono de la ventana pendiente
        self.ventana.geometry(f"{str(cuadro * 8 )}x{str(cuadro * 8 )}") # se proporciona la altura y ancho
        self.ventana.resizable(0,0) #tamaño fijo de la ventana, evita que se agrande o minimice

        self.interfaz = tk.Canvas(self.ventana) # Permite acceder a graficos
        self.interfaz.pack(fill="both", expand=True)  #para que ocupe toda la ventana   
    
    def __call__(self):
     self.ventana.mainloop()

    def crearTablero(self):
        cuadradoC= 300
        for i in range (cuadradoC):
            for j in range (cuadradoC):
                if (i+j) % 2 == 0: #0
                    #0+0 % 2 = 0 no tiene residuo entra al if y al tener residuo su valor sera uno se dirigira al else
                    self.interfaz.create_rectangle(i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#FFFFFF")
                    # 0 *0 , 0*0, 0, 0,

                else: #1
                    self.interfaz.create_rectangle(i*self.cuadro, j*self.cuadro, (i+1)*self.cuadro, (j+1)*self.cuadro, fill="#58A0AD")
     
    def importarpiezas(self):
        piezas= ["peonN", "peonB", "caballoN", "caballoB", "alfilN", "alfilB", "torreN", "torreB", "reinaN", "reinaB", "reyN", "reyB"]
        for pieza in piezas:
            self.imagenes[pieza] = tk.PhotoImage(file="./imagenes/" + pieza + ".png")

    def mostrarPiezas(self): 
        for indicea, i in enumerate(self.posicion.piezas): #listas
         for indiceb, j in enumerate(i): #valores de las listas
           if j != (""): #al cumplirse la condicion de ser diferente de vacio se crea una pieza de lo contrario sigue
            self.interfaz.create_image(indiceb*self.cuadro, indicea*self.cuadro, image=self.imagenes[j], anchor= "nw")


correventana = ventana(83)
correventana.crearTablero()
correventana.importarpiezas()
correventana.mostrarPiezas()
correventana()