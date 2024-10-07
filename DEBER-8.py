import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestión de Proyectos de Programación")
        self.root.geometry("400x400")  # Establecer un tamaño inicial para la ventana

        # Lista para almacenar las tareas
        self.tasks = []

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botón para añadir una nueva tarea
        self.add_button = tk.Button(root, text="Añadir Proyecto", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar la tarea seleccionada como completada
        self.complete_button = tk.Button(root, text="Marcar Completado", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar la tarea seleccionada
        self.delete_button = tk.Button(root, text="Eliminar Proyecto", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista (Listbox) para mostrar las tareas pendientes
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Asignación de atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Añadir tarea con Enter
        self.root.bind('<c>', lambda event: self.complete_task())  # Marcar como completada con C
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Eliminar tarea con Delete
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Cerrar la aplicación con Escape

    def add_task(self):
        # Obtener texto de la entrada
        task_text = self.task_entry.get()
        if task_text != "":
            # Añadir tarea a la lista
            self.tasks.append(task_text)
            self.update_task_listbox()  # Actualizar la lista visual
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            # Mostrar advertencia si no se ingresa texto
            messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre del proyecto.")

    def complete_task(self):
        # Marcar la tarea seleccionada como completada
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            completed_task = self.tasks[selected_index] + " (Completado)"  # Añadir texto de completada
            self.tasks[selected_index] = completed_task  # Actualizar la tarea en la lista
            self.update_task_listbox()  # Actualizar la lista visual
        except IndexError:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, seleccione un proyecto para marcar como completado.")

    def delete_task(self):
        # Eliminar la tarea seleccionada
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            del self.tasks[selected_index]  # Eliminar la tarea de la lista
            self.update_task_listbox()  # Actualizar la lista visual
        except IndexError:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Por favor, seleccione un proyecto para eliminar.")

    def update_task_listbox(self):
        # Limpiar la lista visual antes de actualizar
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            # Insertar cada tarea en el Listbox
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManager(root)  # Instanciar la clase TaskManager
    root.mainloop()  # Iniciar el bucle de eventos