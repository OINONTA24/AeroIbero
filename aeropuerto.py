import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import pandas as pd

def crear_ventana(ventana, ancho=450, alto=380):
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
        self.Breservacion.place(x=60, y=60, width=350, height=100)
        
        self.Bconsulta = tk.Button(self.ventana_main, text="Consulta reserva", command=self.ir_consulta)
        self.Bconsulta.place(x=60, y=200, width=350, height=100)
        
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
        
        self.df = pd.read_csv("CiudadesAeroIbero.csv", encoding = "latin1",usecols=["Origen", "Destino", "Tiempo total (Hrs)", " Costo total "])

        self.box_value = StringVar()
        self.box_tipoV = StringVar()

        def confirma_reserva():
            self.Nventana.withdraw()
            confirmar_reservacion(self.Nventana)

        def get_fecha():
            self.select_date = self.EnFecSalida.get()
            fecha_elegida = datetime.strptime(self.select_date,"%Y-%m-%d")
            if datetime.now() > fecha_elegida:
                print("Fecha no disponible\n")
            else:
                return self.select_date

        # Vista ciudad origen
        self.LCiuOr = tk.Label(self.Nventana, text="Ciudad de origen")
        self.LCiuOr.place(x=20, y=0, width=120, height=30)
        
        self.CmBoxCiuOr = ttk.Combobox(self.Nventana, values=list(self.df['Origen'].unique()),state="readonly")
        self.CmBoxCiuOr.place(x=20, y=30, width=150, height=30)
        self.CmBoxCiuOr.bind("<<ComboboxSelected>>", lambda e: self.actualizar_info_vuelo())
 
        # Vista ciudad destino
        self.LCiuDes = tk.Label(self.Nventana, text="Ciudad de destino")
        self.LCiuDes.place(x=20, y=60, width=120, height=30)
        
        self.CmBoxCiuDes = ttk.Combobox(self.Nventana, values=list(self.df['Destino'].unique()),state ="readonly")
        self.CmBoxCiuDes.place(x=20, y=90, width=150, height=30)
        self.CmBoxCiuDes.bind("<<ComboboxSelected>>", lambda e: self.actualizar_info_vuelo())

        # Vista cantidad de personas
        self.Lcantidad = tk.Label(self.Nventana, text="pasajeros")
        self.Lcantidad.place(x=20, y=120, width=80, height=30)

        self.comBoxCanti = ttk.Combobox(self.Nventana,textvariable=self.box_value, state = 'readonly')
        self.comBoxCanti["values"] = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.comBoxCanti.place(x=20, y=150, width=150, height=30)

        #Tipo de viaje
        self.LSalida = tk.Label(self.Nventana, text="Tipo de viaje")
        self.LSalida.place(x=260, y=120, width=80, height=30)    
            
        self.tipoViaje = ttk.Combobox(self.Nventana,textvariable=self.box_tipoV, state = 'readonly')
        self.tipoViaje["values"] = ["Corto", "Optimo", "Economico"]
        self.tipoViaje.place(x=230, y=150, width=150, height=30)
        
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
        
        self.TxtTiempoT = tk.Label(self.Nventana, text="----")
        self.TxtTiempoT.place(x=230,y=30,width=150,height=30)
        
        #Esto es la estimacion del costo total
        self.LCostoT = tk.Label(self.Nventana,text="Costo total")
        self.LCostoT.place(x=230,y=60,width=150,height=30)
        
        self.TxtCostoT = tk.Label(self.Nventana,text="---")
        self.TxtCostoT.place(x=230,y=90,width=150,height=30)
        
        #Reservar vista
        self.BReservar = tk.Button(self.Nventana,text="Confirmar reservacion",command=self.valida_reserva)
        self.BReservar.place(x=70,y=330,width=150,height=30)

        # Botón para regresar al menú principal
        self.BRegresar = tk.Button(self.Nventana, text="Regresar", command=self.regresar)
        self.BRegresar.place(x=250, y=330, width=120, height=30)

        crear_ventana(self.Nventana)
        
    def actualizar_info_vuelo(self):
        origen = self.CmBoxCiuOr.get().strip()
        destino = self.CmBoxCiuDes.get().strip()
        
        if origen and destino:
            resultado = self.df[(self.df['Origen'].str.strip() == origen) & (self.df['Destino'].str.strip() == destino)]
            
            if not resultado.empty:
                tiempo_estimado = resultado.iloc[0]['Tiempo total (Hrs)']
                costo_total = resultado.iloc[0][' Costo total ']

                self.TxtTiempoT.config(text=f"{tiempo_estimado} horas")
                self.TxtCostoT.config(text=f"{costo_total}")
            else:
                self.TxtTiempoT.config(text="No disponible")
                self.TxtCostoT.config(text="No disponible")
        
    def valida_reserva(self):
        origen = self.CmBoxCiuOr.get().strip()
        destino = self.CmBoxCiuDes.get().strip()
        cantidadPer = self.box_value.get().strip()
        fecha_salida = self.EnFecSalida.get()
        tipo_viaje = self.tipoViaje.get().strip()
        tiempo_estimado = self.TxtTiempoT.cget("text")
        costo_total = self.TxtCostoT.cget("text")
        if not origen or not destino or not cantidadPer or tiempo_estimado == '---' or costo_total == '---':
            print("Checa que los campos no esten vacios\n")
            return
        if origen == destino:
            print("Error: La ciudad de origen y destino no pueden ser las mismas.")
            return
        
        #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        Narchivo = f"confirmacion_de_vuelo_{origen}_{destino}_{cantidadPer}.txt"
        with open(Narchivo,"w") as archivo:
            archivo.write(f"Ciudad origen: {origen}\n")
            archivo.write(f"Ciudad destino: {destino}\n")
            archivo.write(f"Pasajeros: {cantidadPer}\n")
            archivo.write(f"Fecha de salida: {fecha_salida}\n")
            archivo.write(f"Tiempo estimado: {tiempo_estimado}\n")
            archivo.write(f"Tiempo estimado: {tipo_viaje}\n")
            archivo.write(f"Costo total: {costo_total}\n")
                
        print(f"Reservación guardada en {Narchivo}")

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
        self.BConsulta.place(x=120, y=140, width=150, height=30)
        
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
        
        self.Lsalida = tk.Label(self.Nventana,text="Fecha salida: ")
        self.Lsalida.place(x=0, y=20, width=120, height=30)
        
        self.LOrigen = tk.Label(self.Nventana,text="Origen: ")
        self.LOrigen.place(x=0, y=50, width=120, height=30)
        
        self.LDestino = tk.Label(self.Nventana,text="Destino: ")
        self.LDestino.place(x=0, y=80, width=120, height=30)
        
        self.LPasajero = tk.Label(self.Nventana,text="Pasajeros: ")
        self.LPasajero.place(x=0, y=110, width=120, height=30)
        
        self.LTvuelo = tk.Label(self.Nventana,text="Tipo de vuelo: ")
        self.LTvuelo.place(x=0, y=140, width=120, height=30)
        
        self.LTiempo = tk.Label(self.Nventana,text="Tiempo estimado: ")
        self.LTiempo.place(x=0, y=170, width=120, height=30)
        
        self.LCosto = tk.Label(self.Nventana,text="Costo total: ")
        self.LCosto.place(x=0, y=200, width=120, height=30)
        
        self.BConfirma = tk.Button(self.Nventana, text="Confirmar", command=self.Irllenar_infoPerso)
        self.BConfirma.place(x=140, y=260, width=150, height=30)
        
        self.BRegresar = tk.Button(self.Nventana, text="Regresa", command=self.regresar)
        self.BRegresar.place(x=140, y=300, width=150, height=30)
        
        crear_ventana(self.Nventana)
        
    def Irllenar_infoPerso(self):
        self.Nventana.withdraw()
        llenar_infoPerso(self.Nventana)
        
    def regresar(self):
        self.Nventana.destroy()  # Cierra la ventana de consulta
        self.ventana_anterior.deiconify()  # Muestra el menú principal nuevamente
        
        
class llenar_infoPerso():
    def __init__(self, ventana_anterior):
        self.ventana_anterior = ventana_anterior
        self.Nventana = tk.Toplevel()
        self.Nventana.title("Informacion personal")
        
        #Nombre(s)
        self.LNombre = tk.Label(self.Nventana, text="Nombre(s)")
        self.LNombre.place(x=20, y=0, width=120, height=20)
        
        self.TxtNombre = tk.Text(self.Nventana, width=150, height=30)
        self.TxtNombre.place(x=20, y=20, width=150, height=20)
        
        #Apellido Paterno
        self.LApaterno = tk.Label(self.Nventana, text="Apellido paterno")
        self.LApaterno.place(x=20, y=40, width=150, height=30)
        
        self.TxtApaterno = tk.Text(self.Nventana, width=120, height=30)
        self.TxtApaterno.place(x=20, y=70, width=150, height=20)
        
        #Apellido Materno
        self.LAmaterno = tk.Label(self.Nventana, text="Apellido materno")
        self.LAmaterno.place(x=20, y=100, width=150, height=30)
        
        self.TxtAmaterno = tk.Text(self.Nventana, width=120, height=30)
        self.TxtAmaterno.place(x=20, y=130, width=150, height=20)
        
        #Raza
        self.LRaza= tk.Label(self.Nventana, text="Raza")
        self.LRaza.place(x=20, y=160, width=150, height=30)
        
        self.CmBoxRaza = ttk.Combobox(self.Nventana, values=["Humano", "Elfo","Orco","Enano"])
        self.CmBoxRaza.place(x=20, y=180, width=150, height=20)

        #otra raza
        self.LRaza= tk.Label(self.Nventana, text="Nombra tu raza")
        self.LRaza.place(x=20, y=210, width=150, height=20)
        
        self.TxtRaza = tk.Text(self.Nventana, width=150, height=30)
        self.TxtRaza.place(x=20, y=240, width=150, height=20)
        
        self.BGuardaRaza = tk.Button(self.Nventana,text="Guardar Raza", command=self.agregar_Nraza)
        self.BGuardaRaza.place(x=20,y=270,width=150, height=20)
        
        #Correo
        self.LCorreo= tk.Label(self.Nventana, text="Correo")
        self.LCorreo.place(x=210, y=0, width=150, height=20)
        
        self.TxtCorreo = tk.Text(self.Nventana, width=150, height=30)
        self.TxtCorreo.place(x=210, y=20, width=150, height=20)
        
        #Numero de celular
        self.LNcel= tk.Label(self.Nventana, text="Num. Celular")
        self.LNcel.place(x=210, y=40, width=150, height=20)
        
        self.TxtNcel = tk.Text(self.Nventana, width=150, height=30)
        self.TxtNcel.place(x=210, y=70, width=150, height=20)
        
        #Nacionalidad
        self.LNcel= tk.Label(self.Nventana, text="Nacionalidad")
        self.LNcel.place(x=210, y=100, width=150, height=20)
        
        self.CmBoxRaza = ttk.Combobox(self.Nventana, values=["Narnia", "Nose","Nose","Nose"])
        self.CmBoxRaza.place(x=210, y=130, width=150, height=20)
        
        self.BListo = tk.Button(self.Nventana,text="Listo",command=self.guardar_infoPer)
        self.BListo.place(x=120, y=300,width=150,height=20)
        
        #vuelve a la ventana anterior
        self.BRegresar = tk.Button(self.Nventana, text="Regresar", command=self.regresar)
        self.BRegresar.place(x=120, y=330, width=150, height=20)

        crear_ventana(self.Nventana)
        
    def guardar_infoPer(self):
        print("Listo\n")
        return None

    def regresar(self):
        self.Nventana.destroy()
        self.ventana_anterior.deiconify()
    
    def agregar_Nraza(self):
        return None

ventanaM = tk.Tk()
interfaz = Interfaz_main(ventanaM)
ventanaM.mainloop()
