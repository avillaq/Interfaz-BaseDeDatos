import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conf_general import *

NOMBRE_TABLA = "estanco"

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
        consulta_sql = """
        SELECT t.*, u.*
        FROM {} AS t
        JOIN Ubigeo AS u ON t.EstUbi = u.UbiCod ORDER BY EstIdeFisEst ASC
        """.format(NOMBRE_TABLA)
        cur.execute(consulta_sql)
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def insertar(self, EstIdeFisEst, EstNumExp, EstNom, EstUbi):
        cur = self.cnn.cursor()
        sql = "INSERT INTO {} (EstIdeFisEst, EstNumExp, EstNom, EstUbi) VALUES (%s, %s, %s, %s)".format(NOMBRE_TABLA)
        cur.execute(sql, (EstIdeFisEst, EstNumExp, EstNom, EstUbi))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    
    def eliminar(self, EstIdeFisEst):
        cur = self.cnn.cursor()
        sql = "DELETE FROM {} WHERE EstIdeFisEst = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (EstIdeFisEst,))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modificar(self, EstIdeFisEst, EstNumExp, EstNom, EstUbi):
        cur = self.cnn.cursor()
        sql = "UPDATE {} SET EstNumExp = %s, EstNom = %s, EstUbi = %s WHERE EstIdeFisEst = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (EstNumExp, EstNom, EstUbi, EstIdeFisEst,))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def obtener_ubicaciones_disponibles(self):
        cur = self.cnn.cursor()
        cur.execute("""
            SELECT UbiCod, UbiPro, UbiLoc, UbiDic 
            FROM ubigeo 
            WHERE NOT EXISTS (
                SELECT 1 FROM estanco WHERE estanco.EstUbi = ubigeo.UbiCod
            )
            ORDER BY UbiLoc ASC
        """) 
        ubicaciones_disponibles = cur.fetchall()
        cur.close()
        return ubicaciones_disponibles


    def obtener_id_ubicacion(self, UbiPro, UbiLoc, UbiDic):
        cur = self.cnn.cursor()
        cur.execute("SELECT UbiCod FROM ubigeo WHERE UbiPro = %s AND UbiLoc = %s AND UbiDic = %s", (UbiPro, UbiLoc, UbiDic))
        resultado = cur.fetchall()
        cur.close()
        id = resultado[0][0]
        return id


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
                   
    def habilitarCajas(self,estado):
        self.txtIdeFiscal.configure(state=estado)
        self.txtNumExpendiduria.configure(state=estado)
        self.txtNombre.configure(state=estado)
        self.txtUbicacion.configure(state=estado)

    def limpiarCajas(self):
        self.txtIdeFiscal.delete(0,END)
        self.txtNumExpendiduria.delete(0,END)
        self.txtNombre.delete(0,END)
        self.txtUbicacion.delete(0,END)
        
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
        datos = self.operacion.consultar()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[0], row[1], row[2], f"{row[6]} - {row[5]} - {row[7]}"))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fAdicionar(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtIdeFiscal.focus()
    
    def fGuardar(self):
        ############################################################################################### 
        Ubicacion = self.txtUbicacion.get().split(" - ")
        UbiPro = Ubicacion[0]
        UbiLoc = Ubicacion[1]
        UbiDic = Ubicacion[2]
        id_ubicacion = self.operacion.obtener_id_ubicacion(UbiPro, UbiLoc, UbiDic)
        if self.id ==-1:
            self.operacion.insertar(self.txtIdeFiscal.get(),self.txtNumExpendiduria.get(), self.txtNombre.get(), id_ubicacion)
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.operacion.modificar(self.txtIdeFiscal.get(),self.txtNumExpendiduria.get(), self.txtNombre.get(), id_ubicacion)
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1
        
        # Actualizar la lista de ubicaciones disponibles
        ubicaciones = self.operacion.obtener_ubicaciones_disponibles()
        self.txtUbicacion['values'] = [f"{f[1]} - {f[2]} - {f[3]}" for f in ubicaciones]

        # Habilitar el codigo para el siguiente registro
        self.txtIdeFiscal.configure(state="normal")

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
            self.txtIdeFiscal.insert(0,valores[0])
            self.txtNumExpendiduria.insert(0,valores[1])   
            self.txtNombre.insert(0,valores[2])
            self.txtUbicacion.insert(0,valores[3])        
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

            # No se debe modificar este campo
            self.txtIdeFiscal.configure(state="disabled")

            self.txtNumExpendiduria.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        id_fiscal = self.grid.item(selected,'text')
        if id_fiscal == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n")            
            if r == messagebox.YES:
                n = self.operacion.eliminar(id_fiscal)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()

                    # Actualizar la lista de ubicaciones disponibles
                    ubicaciones = self.operacion.obtener_ubicaciones_disponibles()
                    self.txtUbicacion['values'] = [f"{f[1]} - {f[2]} - {f[3]}" for f in ubicaciones]

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
        lbl1 = Label(frame2,text="Indentificacion Fiscal: ")
        lbl1.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtIdeFiscal=Entry(frame2)
        self.txtIdeFiscal.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)                
        lbl2 = Label(frame2,text="Numero Expendiduria: ")
        lbl2.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtNumExpendiduria = Entry(frame2)
        self.txtNumExpendiduria.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        lbl3 = Label(frame2,text="Nombre: ")
        lbl3.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)

        lbl4 = Label(frame2,text="Ubicacion: ")
        lbl4.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtUbicacion = ttk.Combobox(frame2, state="readonly")
        self.txtUbicacion.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        ubicaciones = self.operacion.obtener_ubicaciones_disponibles()
        self.txtUbicacion['values'] = [f"{f[1]} - {f[2]} - {f[3]}" for f in ubicaciones]
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
        nombre_columnas = ["Indentificacion Fiscal", "Numero Expendiduria", "Nombre", "Ubicacion"]

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