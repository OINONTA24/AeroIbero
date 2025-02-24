import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

def crear_ventana(ventana, ancho=450, alto=580):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    centro_x = int(pantalla_ancho / 2 - ancho / 2)
    centro_y = int(pantalla_alto / 2 - alto / 2)
    ventana.geometry(f"{ancho}x{alto}+{centro_x}+{centro_y}")

class Interfaz_main:
    def __init__(self, ventana_main):
        self.ventana_main = ventana_main
        self.ventana_main.title("AeroIbero Kevin y Pepe")
        crear_ventana(ventana_main)
        
        self.Breservacion = tk.Button(self.ventana_main, text="Reserva vuelo", command=self.ir_reservacion)
        self.Breservacion.place(x=60, y=120, width=350, height=100)
        
        self.Bconsulta = tk.Button(self.ventana_main, text="Consulta reserva", command=self.ir_consulta)
        self.Bconsulta.place(x=60, y=340, width=350, height=100)
        
    def ir_reservacion(self):
        self.ventana_main.withdraw()  # Oculta la ventana principal
        crear_reservacion(self.ventana_main)  # Pasa la referencia
        
    def ir_consulta(self):
        self.ventana_main.withdraw()  # Oculta la ventana principal
        consulta_reservacion(self.ventana_main)  # Pasa la referencia

class crear_reservacion():
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.Nventana = tk.Toplevel()  # Usamos Toplevel para no crear una nueva instancia de Tk
        self.Nventana.title("Reservación vuelo")

        def confirma_reserva():
            self.Nventana.destroy()
            confirmar_reservacion(self.Nventana)

        def get_fecha():
            self.select_date = self.EnFecSalida.get()

        # Vista ciudad origen
        self.LCiuOr = tk.Label(self.Nventana, text="Ciudad de origen")
        self.LCiuOr.place(x=20, y=0, width=120, height=30)
        
        self.CmBoxCiuOr = ttk.Combobox(self.Nventana, values=["python", "c"])
        self.CmBoxCiuOr.place(x=20, y=30, width=150, height=30)
 
        # Vista ciudad destino
        self.LCiuDes = tk.Label(self.Nventana, text="Ciudad de destino")
        self.LCiuDes.place(x=20, y=60, width=120, height=30)
        
        self.CmBoxCiuDes = ttk.Combobox(self.Nventana, values=["Narnia", "Narnia2"])
        self.CmBoxCiuDes.place(x=20, y=90, width=150, height=30)

        # Vista cantidad de personas
        self.Lcantidad = tk.Label(self.Nventana, text="Cantidad")
        self.Lcantidad.place(x=20, y=120, width=80, height=30)

        self.comBoxCanti = ttk.Combobox(self.Nventana, values=["1", "2", "3", "4", "5", "6", "7", "8"])
        self.comBoxCanti.place(x=20, y=150, width=150, height=30)
        
        # Vista fecha salida
        self.LSalida = tk.Label(self.Nventana, text="Fecha de salida")
        self.LSalida.place(x=20, y=180, width=80, height=30)

        self.EnFecSalida = DateEntry(self.Nventana, date_pattern="yyyy-mm-dd")
        self.EnFecSalida.place(x=20, y=210)
        
        self.BtnFecSalida = tk.Button(self.Nventana, text="Guardar fecha", command=get_fecha)
        self.BtnFecSalida.place(x=20, y=240, width=120, height=30)
        
        #Estimacion de tiempo de vuelo
        self.LTiempoT = tk.Label(self.Nventana,text="Tiempo estimado")
        self.LTiempoT.place(x=230,y=0,width=150,height=30)
        
        self.TxtTiempoT = tk.Text(self.Nventana,width=150,height=30)
        self.TxtTiempoT.config(state="disable")
        self.TxtTiempoT.place(x=230,y=30,width=150,height=30)
        self.TxtTiempoT.insert(tk.INSERT,"aqui va una operacion")
        
        
        #Esto es la estimacion del costo total
        self.LCostoT = tk.Label(self.Nventana,text="Costo total")
        self.LCostoT.place(x=230,y=60,width=150,height=30)
        
        self.TxtCostoT = tk.Text(self.Nventana,width=150,height=30)
        self.TxtCostoT.config(state="disable")
        self.TxtCostoT.place(x=230,y=90,width=150,height=30)
        self.TxtCostoT.insert(tk.INSERT,"aqui va una operacion2")
        
        #Reservar vista
        self.BReservar = tk.Button(self.Nventana,text="Confirmar reservacion",command=confirma_reserva)
        self.BReservar.place(x=70,y=330,width=150,height=30)

        # Botón para regresar al menú principal
        self.BRegresar = tk.Button(self.Nventana, text="Regresar", command=self.regresar)
        self.BRegresar.place(x=250, y=330, width=120, height=30)

        crear_ventana(self.Nventana)

    def regresar(self):
        self.Nventana.destroy()  # Cierra la ventana de reservación
        self.ventana_anterior.deiconify()  # Muestra el menú principal nuevamente

class consulta_reservacion():
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.Nventana = tk.Toplevel()
        self.Nventana.title("Consulta de Reservación")
        
        self.LConsulta = tk.Label(self.Nventana, text="Ingresa el código\nprimeras letras de Nombre y apellidos")
        self.LConsulta.place(x=100, y=40, width=200, height=60)
        
        self.TxtConsulta = tk.Text(self.Nventana, width=150, height=30)
        self.TxtConsulta.place(x=120, y=100, width=150, height=30)
        
        self.BConsulta = tk.Button(self.Nventana, text="Buscar", command=self.buscar_vuelo)
        self.BConsulta.place(x=120, y=130, width=150, height=30)
        
        # Botón para regresar al menú principal
        self.BRegresar = tk.Button(self.Nventana, text="Regresar", command=self.regresar)
        self.BRegresar.place(x=120, y=180, width=150, height=30)

        crear_ventana(self.Nventana)

    def buscar_vuelo(self):
        return None  # Se implementará más adelante

    def regresar(self):
        self.Nventana.destroy()  # Cierra la ventana de consulta
        self.ventana_anterior.deiconify()  # Muestra el menú principal nuevamente

class confirmar_reservacion():
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.Nventana = tk.Toplevel()
        self.Nventana.title("Confirma reservación")
        
        self.BConfirma = tk.Button(self.Nventana, text="Confirmar", command=self.Irllenar_infoPerso)
        self.BConfirma.place(x=120, y=130, width=150, height=30)
        
        self.BRegresar = tk.Button(self.Nventana, text="Regresa", command=self.regresar)
        self.BRegresar.place(x=120, y=180, width=150, height=30)
        
        crear_ventana(self.Nventana)
        
    def Irllenar_infoPerso(self):
        self.Nventana.withdraw()
        llenar_infoPerso(self.Nventana)
        
    def regresar(self):
        self.Nventana.destroy()  # Cierra la ventana de consulta
        self.ventana_anterior.deiconify()  # Muestra el menú principal nuevamente
        
        
class llenar_info():
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.Nventana = tk.Toplevel()  # Usamos Toplevel para no crear una nueva instancia de Tk
        self.Nventana.title("Informacion personal")
        
        self.BRegresar = tk.Button(self.Nventana, text="Regresar", command=self.regresar)
        self.BRegresar.place(x=120, y=180, width=150, height=30)

        crear_ventana(self.Nventana)

    def regresar(self):
        self.Nventana.destroy()
        self.ventana_anterior.deiconify()

ventanaM = tk.Tk()
interfaz = Interfaz_main(ventanaM)
ventanaM.mainloop()


