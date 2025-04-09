import tkinter as tk
from tkinter import ttk, messagebox
from database import *
from datetime import datetime

class ViajesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservaciones de Viajes")
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        # Pestaña de Viajes
        self.tab_viajes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_viajes, text='Viajes')
        self.setup_viajes_tab()
        
        # Pestaña de Reservaciones
        self.tab_reservaciones = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reservaciones, text='Reservaciones')
        self.setup_reservaciones_tab()
        
        # Cargar datos iniciales
        self.actualizar_lista_viajes()
        self.actualizar_lista_reservaciones()
    
    def setup_viajes_tab(self):
        # Formulario para agregar viajes
        tk.Label(self.tab_viajes, text="Origen:").grid(row=0, column=0, padx=5, pady=5)
        self.origen_entry = tk.Entry(self.tab_viajes)
        self.origen_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_viajes, text="Destino:").grid(row=1, column=0, padx=5, pady=5)
        self.destino_entry = tk.Entry(self.tab_viajes)
        self.destino_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_viajes, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self.tab_viajes)
        self.fecha_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_viajes, text="Precio:").grid(row=3, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.tab_viajes)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_viajes, text="Asientos disponibles:").grid(row=4, column=0, padx=5, pady=5)
        self.asientos_entry = tk.Entry(self.tab_viajes)
        self.asientos_entry.grid(row=4, column=1, padx=5, pady=5)
        
        tk.Button(self.tab_viajes, text="Agregar Viaje", command=self.agregar_viaje).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Lista de viajes
        self.viajes_tree = ttk.Treeview(self.tab_viajes, columns=('ID', 'Origen', 'Destino', 'Fecha', 'Precio', 'Asientos'))
        self.viajes_tree.heading('#0', text='ID')
        self.viajes_tree.heading('#1', text='Origen')
        self.viajes_tree.heading('#2', text='Destino')
        self.viajes_tree.heading('#3', text='Fecha')
        self.viajes_tree.heading('#4', text='Precio')
        self.viajes_tree.heading('#5', text='Asientos')
        self.viajes_tree.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        
        # Botón para eliminar viaje
        tk.Button(self.tab_viajes, text="Eliminar Viaje Seleccionado", command=self.eliminar_viaje).grid(row=7, column=0, columnspan=2, pady=5)
    
    def setup_reservaciones_tab(self):
        # Formulario para hacer reservaciones
        tk.Label(self.tab_reservaciones, text="Viaje:").grid(row=0, column=0, padx=5, pady=5)
        self.viaje_combobox = ttk.Combobox(self.tab_reservaciones, state='readonly')
        self.viaje_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_reservaciones, text="Nombre Cliente:").grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.tab_reservaciones)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.tab_reservaciones, text="Cantidad Pasajeros:").grid(row=2, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self.tab_reservaciones)
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(self.tab_reservaciones, text="Hacer Reservación", command=self.hacer_reservacion).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Lista de reservaciones
        self.reservaciones_tree = ttk.Treeview(self.tab_reservaciones, columns=('ID', 'Cliente', 'Viaje', 'Pasajeros', 'Total'))
        self.reservaciones_tree.heading('#0', text='ID')
        self.reservaciones_tree.heading('#1', text='Cliente')
        self.reservaciones_tree.heading('#2', text='Viaje')
        self.reservaciones_tree.heading('#3', text='Pasajeros')
        self.reservaciones_tree.heading('#4', text='Total')
        self.reservaciones_tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # Botón para cancelar reservación
        tk.Button(self.tab_reservaciones, text="Cancelar Reservación", command=self.cancelar_reservacion).grid(row=5, column=0, columnspan=2, pady=5)
    
    def actualizar_lista_viajes(self):
        # Limpiar treeview
        for item in self.viajes_tree.get_children():
            self.viajes_tree.delete(item)
        
        # Obtener viajes de la base de datos
        for viaje in listar_viajes():
            self.viajes_tree.insert('', 'end', text=str(viaje['_id']),
                                 values=(viaje['origen'], viaje['destino'], 
                                         viaje['fecha'].strftime('%Y-%m-%d'),
                                         f"${viaje['precio']:.2f}",
                                         viaje['asientos_disponibles']))
        
        # Actualizar combobox de reservaciones
        viajes_disponibles = []
        for viaje in listar_viajes():
            if viaje['asientos_disponibles'] > 0:
                viajes_disponibles.append(f"{viaje['origen']} a {viaje['destino']} - {viaje['fecha'].strftime('%Y-%m-%d')} (ID: {viaje['_id']})")
        
        self.viaje_combobox['values'] = viajes_disponibles
        if viajes_disponibles:
            self.viaje_combobox.current(0)
    
    def actualizar_lista_reservaciones(self):
        # Limpiar treeview
        for item in self.reservaciones_tree.get_children():
            self.reservaciones_tree.delete(item)
        
        # Obtener reservaciones de la base de datos
        for reservacion in listar_reservaciones():
            viaje = viajes.find_one({'_id': reservacion['viaje_id']})
            viaje_info = f"{viaje['origen']} a {viaje['destino']} - {viaje['fecha'].strftime('%Y-%m-%d')}"
            
            self.reservaciones_tree.insert('', 'end', text=str(reservacion['_id']),
                                         values=(reservacion['nombre_cliente'],
                                                 viaje_info,
                                                 reservacion['cantidad_pasajeros'],
                                                 f"${reservacion['total_pago']:.2f}"))
    
    def agregar_viaje(self):
        try:
            origen = self.origen_entry.get()
            destino = self.destino_entry.get()
            fecha = self.fecha_entry.get()
            precio = self.precio_entry.get()
            asientos = self.asientos_entry.get()
            
            if not all([origen, destino, fecha, precio, asientos]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            agregar_viaje(origen, destino, fecha, precio, asientos)
            messagebox.showinfo("Éxito", "Viaje agregado correctamente")
            
            # Limpiar campos
            self.origen_entry.delete(0, 'end')
            self.destino_entry.delete(0, 'end')
            self.fecha_entry.delete(0, 'end')
            self.precio_entry.delete(0, 'end')
            self.asientos_entry.delete(0, 'end')
            
            # Actualizar listas
            self.actualizar_lista_viajes()
            self.actualizar_lista_reservaciones()
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def eliminar_viaje(self):
        selected_item = self.viajes_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona un viaje para eliminar")
            return
        
        viaje_id = self.viajes_tree.item(selected_item)['text']
        
        # Verificar si hay reservaciones para este viaje
        reservaciones_count = reservaciones.count_documents({'viaje_id': viaje_id})
        if reservaciones_count > 0:
            messagebox.showerror("Error", "No se puede eliminar un viaje con reservaciones activas")
            return
        
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este viaje?"):
            viajes.delete_one({'_id': viaje_id})
            self.actualizar_lista_viajes()
            messagebox.showinfo("Éxito", "Viaje eliminado correctamente")
    
    def hacer_reservacion(self):
        try:
            viaje_seleccionado = self.viaje_combobox.get()
            if not viaje_seleccionado:
                messagebox.showerror("Error", "Selecciona un viaje")
                return
            
            # Extraer ID del viaje del texto del combobox
            viaje_id = viaje_seleccionado.split('(ID: ')[1][:-1]
            
            nombre_cliente = self.nombre_entry.get()
            cantidad_pasajeros = self.cantidad_entry.get()
            
            if not all([nombre_cliente, cantidad_pasajeros]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            resultado = hacer_reservacion(viaje_id, nombre_cliente, cantidad_pasajeros)
            if resultado:
                messagebox.showinfo("Éxito", "Reservación realizada correctamente")
                
                # Limpiar campos
                self.nombre_entry.delete(0, 'end')
                self.cantidad_entry.delete(0, 'end')
                
                # Actualizar listas
                self.actualizar_lista_viajes()
                self.actualizar_lista_reservaciones()
            else:
                messagebox.showerror("Error", "No hay suficientes asientos disponibles")
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    
    def cancelar_reservacion(self):
        selected_item = self.reservaciones_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Selecciona una reservación para cancelar")
            return
        
        reservacion_id = self.reservaciones_tree.item(selected_item)['text']
        
        if messagebox.askyesno("Confirmar", "¿Estás seguro de cancelar esta reservación?"):
            if cancelar_reservacion(reservacion_id):
                messagebox.showinfo("Éxito", "Reservación cancelada correctamente")
                self.actualizar_lista_viajes()
                self.actualizar_lista_reservaciones()
            else:
                messagebox.showerror("Error", "No se pudo cancelar la reservación")

if __name__ == "__main__":
    root = tk.Tk()
    app = ViajesApp(root)
    root.mainloop()