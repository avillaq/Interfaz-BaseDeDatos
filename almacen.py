import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conf_general import *

NOMBRE_TABLA = "almacen"

class Operaciones:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="ventacigarrillo")

    def __str__(self):
        datos=self.consultar()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
    
    def obtener_nombres_columnas(self):
        # Ejecutar una consultar para obtener los nombres de los campos
        cur = self.cnn.cursor()
        cur.execute("DESCRIBE {}".format(NOMBRE_TABLA))
        columnas = cur.fetchall()
        # Extraer los nombres de las columnas
        nombres_columnas = [columna[0] for columna in columnas]
        return nombres_columnas

    def consultar(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM {}".format(NOMBRE_TABLA))
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def insertar(self, AlmIdeFisEst, AlmCigMar, AlmCigFil, AlmCigCol, AlmClaTra, AlmCarMen, AlmUniSto):
        cur = self.cnn.cursor()
        sql = "INSERT INTO {} (AlmIdeFisEst, AlmCigMar, AlmCigCol, AlmCigFil, AlmClaTra, AlmCarMen, AlmUniSto) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(NOMBRE_TABLA)
        cur.execute(sql, (AlmIdeFisEst, AlmCigMar, AlmCigCol, AlmCigFil, AlmClaTra, AlmCarMen, AlmUniSto))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    
    def eliminar(self, AlmIdeFisEst, AlmCigMar, AlmCigFil, AlmCigCol, AlmClaTra, AlmCarMen):
        cur = self.cnn.cursor()
        sql = "DELETE FROM {} WHERE AlmIdeFisEst = %s AND AlmCigMar = %s AND AlmCigCol = %s AND AlmCigFil = %s AND AlmClaTra = %s AND AlmCarMen = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (AlmIdeFisEst, AlmCigMar, AlmCigCol, AlmCigFil, AlmClaTra, AlmCarMen))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modificar(self, AlmIdeFisEst, AlmCigMar, AlmCigFil, AlmCigCol, AlmClaTra, AlmCarMen, AlmUniSto):
        cur = self.cnn.cursor()
        sql = "UPDATE {} SET AlmUniSto = %s WHERE AlmIdeFisEst = %s AND AlmCigMar = %s AND AlmCigCol = %s AND AlmCigFil = %s AND AlmClaTra = %s AND AlmCarMen = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (AlmUniSto, AlmIdeFisEst, AlmCigMar, AlmCigCol, AlmCigFil, AlmClaTra, AlmCarMen))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def obtener_marcas(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT DISTINCT CigMar FROM cigarrillo") 
        marcas = cur.fetchall()
        cur.close()
        return marcas

    def obtener_id_fiscal(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT EstIdeFisEst FROM estanco") 
        id_fiscal = cur.fetchall()
        cur.close()
        return id_fiscal

    # Operaciones para obtener las opciones válidas para los otros campos basado en la marca seleccionada

    def obtener_opciones_filtro(self, marca):
        cur = self.cnn.cursor()
        cur.execute("SELECT DISTINCT CigFil FROM cigarrillo WHERE CigMar = %s", (marca,))
        opciones_filtro = cur.fetchall()
        cur.close()
        return opciones_filtro
    
    def obtener_opciones_color(self, marca):
        cur = self.cnn.cursor()
        cur.execute("SELECT DISTINCT CigCol FROM cigarrillo WHERE CigMar = %s", (marca,))
        opciones_color = cur.fetchall()
        cur.close()
        return opciones_color
    
    def obtener_opciones_clase(self, marca):
        cur = self.cnn.cursor()
        cur.execute("SELECT DISTINCT CigClaTra FROM cigarrillo WHERE CigMar = %s", (marca,))
        opciones_clase = cur.fetchall()
        cur.close()
        return opciones_clase
    
    def obtener_opciones_mentolado(self, marca):
        cur = self.cnn.cursor()
        cur.execute("SELECT DISTINCT CigCarMen FROM cigarrillo WHERE CigMar = %s", (marca,))
        opciones_mentolado = cur.fetchall()
        cur.close()
        return opciones_mentolado

#############################################################################################################################################


class Ventana(Frame):
    
    operacion = Operaciones()
    # Variable para cambiar la posición de los elementos dinámicamente
    posEtiquetas = 0
    posCampos = 0
        
    def __init__(self, master=None):
        super().__init__(master,width=V_ANCHO, height=V_ALTO)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1   

    def aumentarPosEtiqueta(self):
        if self.posEtiquetas == 0:
            self.posEtiquetas = 5
        else :
            self.posEtiquetas += 50
        return self.posEtiquetas
    
    def aumentarPosCampo(self):
        if self.posCampos == 0:
            self.posCampos = 25
        else :
            self.posCampos += 50
        return self.posCampos
    
    def obtenerDatoEquivalente(self, tipo, dato):
        if tipo == "color":
            if dato == "N":
                return "Negra"
            elif dato == "R":
                return "Rubia"

        if tipo == "filtro" or tipo == "mentolado":
            if dato == "S":
                return "Si"
            elif dato == "N":
                return "No"
        return dato
    
    def on_marca_selected(self, event):
        marca_seleccionada = self.txtMarca.get()
        
        # Consultar las opciones válidas para los otros campos basado en la marca seleccionada
        opciones_filtro = self.operacion.obtener_opciones_filtro(marca_seleccionada)
        opciones_color = self.operacion.obtener_opciones_color(marca_seleccionada)
        opciones_clase = self.operacion.obtener_opciones_clase(marca_seleccionada)
        opciones_mentolado = self.operacion.obtener_opciones_mentolado(marca_seleccionada)
        
        # Actualizar las opciones de los ComboBox con las nuevas opciones
        self.txtFiltro['values'] = [self.obtenerDatoEquivalente("filtro",f[0]) for f in opciones_filtro]
        self.txtColor['values'] = [self.obtenerDatoEquivalente("color",f[0]) for f in opciones_color]
        self.txtClase['values'] = opciones_clase
        self.txtMentolado['values'] = [self.obtenerDatoEquivalente("mentolado",f[0]) for f in opciones_mentolado]
    
        # Opcional: Limpiar la selección actual de los ComboBox si es necesario
        self.txtColor.set('')
        self.txtFiltro.set('')
        self.txtClase.set('')
        self.txtMentolado.set('')
    
    def habilitarCajas(self,estado):
        self.txtIdentificacion.configure(state=estado)
        self.txtMarca.configure(state=estado)
        self.txtFiltro.configure(state=estado)
        self.txtColor.configure(state=estado)
        self.txtClase.configure(state=estado)
        self.txtMentolado.configure(state=estado)
        self.txtUnidades.configure(state=estado)

    def limpiarCajas(self):
        self.txtIdentificacion.delete(0,END)
        self.txtMarca.delete(0,END)
        self.txtFiltro.delete(0,END)
        self.txtColor.delete(0,END)
        self.txtClase.delete(0,END)
        self.txtMentolado.delete(0,END)
        self.txtUnidades.delete(0,END)
        
    def habilitarBtnOper(self,estado):
        self.btnAdicionar.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatos(self):
        ############################################################################################### 
        datos = self.operacion.consultar()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[0], row[1], self.obtenerDatoEquivalente("filtro", row[2]), self.obtenerDatoEquivalente("color", row[3]), row[4], self.obtenerDatoEquivalente("mentolado", row[5]), row[6]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fAdicionar(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtIdentificacion.focus()
    
    def fGuardar(self):
        ############################################################################################### 
        if self.id ==-1:       
            self.operacion.insertar(self.txtIdentificacion.get(),self.txtMarca.get(), self.txtFiltro.get()[0], self.txtColor.get()[0], self.txtClase.get(), self.txtMentolado.get()[0], self.txtUnidades.get())         
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.operacion.modificar(self.txtIdentificacion.get(),self.txtMarca.get(), self.txtFiltro.get()[0], self.txtColor.get()[0], self.txtClase.get(), self.txtMentolado.get()[0], self.txtUnidades.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1  
            
        # Habilitar el codigo para el siguiente registro
        self.habilitarCajas("normal")

        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
                    
    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")
        
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()
            ###############################################################################################
            self.txtIdentificacion.insert(0,valores[0])
            self.txtMarca.insert(0,valores[1])   
            self.txtFiltro.insert(0,valores[2])    
            self.txtColor.insert(0,valores[3])
            self.txtClase.insert(0,valores[4])
            self.txtMentolado.insert(0,valores[5])
            self.txtUnidades.insert(0,valores[6])

            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

            # No se debe modificar el codigo
            self.txtIdentificacion.configure(state="disabled")
            self.txtMarca.configure(state="disabled")
            self.txtColor.configure(state="disabled")
            self.txtFiltro.configure(state="disabled")
            self.txtClase.configure(state="disabled")
            self.txtMentolado.configure(state="disabled")

            self.txtUnidades.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            id_fiscal = valores[0]
            marca = valores[1]
            filtro = valores[2]
            color = valores[3]
            clase = valores[4]
            mentolado = valores[5] 
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n")            
            if r == messagebox.YES:
                n = self.operacion.eliminar(id_fiscal, marca, filtro[0], color[0], clase, mentolado[0])
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.habilitarCajas("normal")
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        N_COLUMNAS = len(self.operacion.obtener_nombres_columnas())

        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=V_ALTO-1)
        
        self.btnAdicionar=Button(frame1,text="Adicionar", command=self.fAdicionar, bg="blue", fg="white")
        self.btnAdicionar.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)

        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=V_ALTO-1)  

        ###################################### MODIFICAR AQUI ###############################################
        # Solo se debe modificar el nombre de las etiquetas y los Entry
        lbl1 = Label(frame2,text="Identificacion Fiscal: ")
        lbl1.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtIdentificacion=ttk.Combobox(frame2, state="readonly")
        self.txtIdentificacion.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)   
        id_fiscal = self.operacion.obtener_id_fiscal()
        self.txtIdentificacion['values'] = [f[0] for f in id_fiscal]
        
        lbl2 = Label(frame2,text="Marca*: ")
        lbl2.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtMarca = ttk.Combobox(frame2, state="readonly")
        self.txtMarca.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        marcas = self.operacion.obtener_marcas()
        self.txtMarca['values'] = [f[0] for f in marcas]
        self.txtMarca.bind("<<ComboboxSelected>>", self.on_marca_selected)


        # Las opciones estarán vacías hasta que se seleccione una marca.

        lbl3 = Label(frame2,text="Filtro: ")
        lbl3.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtFiltro = ttk.Combobox(frame2, state="readonly", values=[])
        self.txtFiltro.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)

        lbl4 = Label(frame2,text="Color: ")
        lbl4.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtColor = ttk.Combobox(frame2, state="readonly", values=[])
        self.txtColor.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        
        lbl5 = Label(frame2,text="Clase de Tratamiento: ")
        lbl5.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtClase = ttk.Combobox(frame2, state="readonly", values=[])
        self.txtClase.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        
        lbl6 = Label(frame2,text="Mentolado: ")
        lbl6.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtMentolado = ttk.Combobox(frame2, state="readonly", values=[])
        self.txtMentolado.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        lbl7 = Label(frame2,text="Unidades en Stock: ")
        lbl7.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtUnidades=Entry(frame2)
        self.txtUnidades.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)

               
        ######################################################################################################


        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=N_COLUMNAS*50+10,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=N_COLUMNAS*50+10,width=60, height=30)
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=T_ANCHO, height=V_ALTO-1)   

        columnas = [f"col{i}" for i in range(N_COLUMNAS)]
        self.grid = ttk.Treeview(frame3, columns=columnas)

        nombre_columnas = self.operacion.obtener_nombres_columnas()
        
        ###################################### MODIFICAR AQUI ###############################################

        # Modificar los nombres de las columnas en la lista nombre_columnas
        nombre_columnas = ["Identificacion Fiscal", "Marca", "Filtro", "Color", "Clase de Tratamiento", "Mentolado", "Unidades en Stock"]

        ######################################################################################################


        for col, nombre in zip(columnas,nombre_columnas):
            self.grid.column(col,width=int(T_ANCHO/N_COLUMNAS), anchor=CENTER)
            self.grid.heading(col, text=nombre, anchor=CENTER)          
       
        self.grid.pack(side=LEFT,fill = Y)        
       
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['show'] = 'headings'  # Solo muestra las columnas especificadas
        self.grid['selectmode']='browse'        

def main():
    root = Tk()
    root.wm_title("{}".format(NOMBRE_TABLA.upper()))
    app = Ventana(root)
    app.mainloop()



if __name__ == "__main__":
    main()