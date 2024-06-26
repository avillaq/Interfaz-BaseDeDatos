import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conf_general import *

N_COLUMNAS = 4
class Ubigeo:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="ventacigarrillo")

    def __str__(self):
        datos=self.consulta_ubigeos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_ubigeos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM ubigeo")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def inserta_ubigeo(self,UbiCod, UbiLoc, UbiPro, UbiDic):
        cur = self.cnn.cursor()
        sql='''INSERT INTO ubigeo (UbiCod, UbiLoc, UbiPro, UbiDic) 
        VALUES('{}', '{}', '{}', '{}')'''.format(UbiCod, UbiLoc, UbiPro, UbiDic)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_ubigeo(self,UbiCod):
        cur = self.cnn.cursor()
        sql='''DELETE FROM ubigeo WHERE UbiCod = {}'''.format(UbiCod)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_ubigeo(self,UbiCod, UbiLoc, UbiPro, UbiDic):
        cur = self.cnn.cursor()
        sql='''UPDATE ubigeo SET UbiLoc='{}', UbiPro='{}',
        UbiDic='{}' WHERE UbiCod={}'''.format(UbiLoc, UbiPro, UbiDic,UbiCod)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   










#############################################################################################################################################


class Ventana(Frame):
    
    ubigeos = Ubigeo()
        
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
                   
    def habilitarCajas(self,estado):
        self.txtCodigo.configure(state=estado)
        self.txtLocalidad.configure(state=estado)
        self.txtProvincia.configure(state=estado)
        self.txtDireccion.configure(state=estado)
        
    def habilitarBtnOper(self,estado):
        self.btnAdicionar.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtCodigo.delete(0,END)
        self.txtLocalidad.delete(0,END)
        self.txtProvincia.delete(0,END)
        self.txtDireccion.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatos(self):
        datos = self.ubigeos.consulta_ubigeos()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[0], row[2],row[1], row[3]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fAdicionar(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtCodigo.focus()
    
    def fGuardar(self): 
        if self.id ==-1:       
            self.ubigeos.inserta_ubigeo(self.txtCodigo.get(),self.txtLocalidad.get(),self.txtProvincia.get(),self.txtDireccion.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.ubigeos.modifica_ubigeo(self.txtCodigo.get(),self.txtLocalidad.get(),self.txtProvincia.get(),self.txtDireccion.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1  
            
        # Habilitar el codigo para el siguiente registro
        self.txtCodigo.configure(state="normal")

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
            self.txtCodigo.insert(0,valores[0])
            self.txtLocalidad.insert(0,valores[2])
            self.txtProvincia.insert(0,valores[1])
            self.txtDireccion.insert(0,valores[3])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

            # No se debe modificar el codigo
            self.txtCodigo.configure(state="disabled")
            

            self.txtCodigo.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n")            
            if r == messagebox.YES:
                n = self.ubigeos.elimina_ubigeo(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
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

        lbl1 = Label(frame2,text="Codigo: ")
        lbl1.place(x=3,y=5)        
        self.txtCodigo=Entry(frame2)
        self.txtCodigo.place(x=3,y=25,width=50, height=20)                
        lbl2 = Label(frame2,text="Provincia: ")
        lbl2.place(x=3,y=55)        
        self.txtProvincia=Entry(frame2)
        self.txtProvincia.place(x=3,y=75,width=100, height=20) 
        lbl3 = Label(frame2,text="Localidad: ")
        lbl3.place(x=3,y=105)        
        self.txtLocalidad=Entry(frame2)
        self.txtLocalidad.place(x=3,y=125,width=100, height=20)        
        lbl4 = Label(frame2,text="Direccion: ")
        lbl4.place(x=3,y=155)        
        self.txtDireccion=Entry(frame2)
        self.txtDireccion.place(x=3,y=175,width=100, height=20)  


        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=210,width=60, height=30)

        frame3 = Frame(self,bg="yellow" ) #680
        frame3.place(x=247,y=0,width=T_ANCHO, height=V_ALTO-1)                      
        self.grid = ttk.Treeview(frame3, columns=("col0", "col1","col2","col3"))        
        #self.grid.column("#0",width=60)
        self.grid.column("col0",width=int(T_ANCHO/N_COLUMNAS), anchor=CENTER)
        self.grid.column("col1",width=int(T_ANCHO/N_COLUMNAS), anchor=CENTER)
        self.grid.column("col2",width=int(T_ANCHO/N_COLUMNAS), anchor=CENTER)
        self.grid.column("col3",width=int(T_ANCHO/N_COLUMNAS), anchor=CENTER)      
        #self.grid.heading("#0", text="Codigo", anchor=CENTER)
        self.grid.heading("col0", text="Codigo", anchor=CENTER)
        self.grid.heading("col1", text="Provincia", anchor=CENTER)
        self.grid.heading("col2", text="Localidad", anchor=CENTER)
        self.grid.heading("col3", text="Direccion", anchor=CENTER)              
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['show'] = 'headings'  # Solo muestra las columnas especificadas
        self.grid['selectmode']='browse'        




def main():
    root = Tk()
    root.wm_title("UBIGEO")
    app = Ventana(root) 
    app.mainloop()



if __name__ == "__main__":
    main()