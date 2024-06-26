import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conf_general import *

NOMBRE_TABLA = "produccion"

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
    
    def insertar(self, ProMar, ProFabNom, ProCar, ProEmb):
        cur = self.cnn.cursor()
        sql = "INSERT INTO {} (ProMar, ProFabNom, ProCar, ProEmb) VALUES (%s, %s, %s, %s)".format(NOMBRE_TABLA)
        cur.execute(sql, (ProMar, ProFabNom, ProCar, ProEmb))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    
    def eliminar(self, ProMar):
        cur = self.cnn.cursor()
        sql = "DELETE FROM {} WHERE ProMar = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (ProMar,))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modificar(self, ProMar, ProFabNom, ProCar, ProEmb):
        cur = self.cnn.cursor()
        sql = "UPDATE {} SET ProFabNom = %s, ProCar = %s, ProEmb = %s WHERE ProMar = %s".format(NOMBRE_TABLA)
        cur.execute(sql, (ProFabNom, ProCar, ProEmb, ProMar))
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def obtener_fabricantes(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT FabNom FROM fabricante") 
        fabricantes = cur.fetchall()
        cur.close()
        return fabricantes




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
        self.txtMarca.configure(state=estado)
        self.txtFabricante.configure(state=estado)
        self.txtCarton.configure(state=estado)
        self.txtEmbalaje.configure(state=estado)

    def limpiarCajas(self):
        self.txtMarca.delete(0,END)
        self.txtFabricante.delete(0,END)
        self.txtCarton.delete(0,END)
        self.txtEmbalaje.delete(0,END)
        
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
            self.grid.insert("",END,text=row[0], values=(row[0], row[1], row[2], row[3]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fAdicionar(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtMarca.focus()
    
    def fGuardar(self):
        ############################################################################################### 
        if self.id ==-1:       
            self.operacion.insertar(self.txtMarca.get(),self.txtFabricante.get(), self.txtCarton.get(), self.txtEmbalaje.get())           
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.operacion.modificar(self.txtMarca.get(),self.txtFabricante.get(), self.txtCarton.get(), self.txtEmbalaje.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1  
            
        # Habilitar el codigo para el siguiente registro
        self.txtMarca.configure(state="normal")

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
            self.txtMarca.insert(0,valores[0])
            self.txtFabricante.insert(0,valores[1])   
            self.txtCarton.insert(0,valores[2])
            self.txtEmbalaje.insert(0,valores[3])        
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

            # No se debe modificar el codigo
            self.txtMarca.configure(state="disabled")
            

            self.txtMarca.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n")            
            if r == messagebox.YES:
                n = self.operacion.eliminar(clave)
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
        lbl1 = Label(frame2,text="Marca: ")
        lbl1.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtMarca=Entry(frame2)
        self.txtMarca.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)                
        
        lbl2 = Label(frame2,text="Fabricante: ")
        lbl2.place(x=3,y=self.aumentarPosEtiqueta())        
        self.txtFabricante = ttk.Combobox(frame2, state="readonly")
        self.txtFabricante.place(x=3, y=self.aumentarPosCampo(), width=130, height=20)
        fabricantes = self.operacion.obtener_fabricantes()
        self.txtFabricante['values'] = [f[0] for f in fabricantes]

        lbl3 = Label(frame2,text="N. Carton: ")
        lbl3.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtCarton=Entry(frame2)
        self.txtCarton.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)
        lbl4 = Label(frame2,text="N. Embalaje: ")
        lbl4.place(x=3,y=self.aumentarPosEtiqueta())
        self.txtEmbalaje=Entry(frame2)
        self.txtEmbalaje.place(x=3,y=self.aumentarPosCampo(),width=130, height=20)

               
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
        nombre_columnas = ["Marca", "Fabricante", "N. Carton", "N. Embalaje"]

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