import tkinter as tk
from tkinter import messagebox

class SimpleDataManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos Simple")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=(20, 5))

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botones en un frame para mejor organización
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Agregar", width=10, command=self.add_data)
        self.add_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Limpiar", width=10, command=self.clear_action)
        self.clear_button.grid(row=0, column=1, padx=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.MULTIPLE)
        self.listbox.pack(pady=10)

    def add_data(self):
        """Agrega el texto del campo a la lista si no está vacío."""
        data = self.entry.get().strip()
        if data:
            self.listbox.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese un dato antes de agregar.")

    def clear_action(self):
        """Limpia el campo de texto si tiene contenido, 
        si no, elimina los elementos seleccionados en la lista.
        Si no hay nada para limpiar, muestra un mensaje."""
        data_in_entry = self.entry.get().strip()
        selected_indices = self.listbox.curselection()

        if data_in_entry:
            # Limpiar solo el campo de texto
            self.entry.delete(0, tk.END)
        elif selected_indices:
            # Eliminar elementos seleccionados en la lista
            for index in reversed(selected_indices):
                self.listbox.delete(index)
        else:
            messagebox.showinfo("Nada para limpiar", "No hay texto para limpiar ni elementos seleccionados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleDataManager(root)
    root.mainloop()
