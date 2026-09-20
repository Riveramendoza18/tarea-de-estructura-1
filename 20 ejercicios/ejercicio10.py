#Gestor de tareas con prioridad
#Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad)
# que guarde en una lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() 
# que retorne solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) 
# que borre la tarea de la lista.
#Entrada
#descripciones y prioridades
#Proceso
#guardar tuplas, filtrar por prioridad, eliminar
#Salida
#tareas filtradas
#Ejemplo de entrada
#t = Tareas()
#t.agregar_tarea("Estudiar", "alta")
#t.agregar_tarea("Leer", "baja")
#t.tareas_prioritarias()
#Salida esperada
#[("Estudiar", "alta")]
# Colecciones: lista de tuplas (inmutables, ordenadas)
class Tareas:
    def __init__(self):
        self.tareas = []  # lista de tuplas (descripcion, prioridad)

    def agregar_tarea(self, descripcion, prioridad):
        """Agrega una nueva tarea como tupla (descripcion, prioridad)."""
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        """Retorna solo las tareas cuya prioridad es 'alta'."""
        return [t for t in self.tareas if t[1] == "alta"]

    def eliminar_completada(self, descripcion):
        """Elimina de la lista la tarea que coincida con la descripción dada."""
        self.tareas = [t for t in self.tareas if t[0] != descripcion]


# --- Programa principal / prueba ---
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())   # [('Estudiar', 'alta')

# OTRO EJERCICIO
#Agenda de citas por hora
#Clase Agenda que: (1) tenga método agregar_cita(descripcion, hora)
# que guarde en una lista de tuplas (descripción, hora) con hora entre 0 y 23; (2) tenga método citas_de_la_manana()
# que retorne solo las citas con hora menor a 12; (3) tenga método cancelar_cita(descripcion)
# que borre la cita de la lista.
#Entrada
# descripciones y horas
#Proceso
# guardar tuplas, filtrar por hora, eliminar
#Salida
# citas filtradas
#Ejemplo de entrada
# a = Agenda()
# a.agregar_cita("Dentista", 9)
# a.agregar_cita("Reunion", 15)
# a.citas_de_la_manana()
#Salida esperada
# [('Dentista', 9)]
# Colecciones: lista de tuplas (inmutables, ordenadas)
class Agenda:
    def __init__(self):
        self.citas = []  # lista de tuplas (descripcion, hora)

    def agregar_cita(self, descripcion, hora):
        """Agrega una nueva cita como tupla (descripcion, hora)."""
        self.citas.append((descripcion, hora))

    def citas_de_la_manana(self):
        """Retorna solo las citas cuya hora es menor a 12."""
        return [c for c in self.citas if c[1] < 12]

    def cancelar_cita(self, descripcion):
        """Elimina de la lista la cita que coincida con la descripción dada."""
        self.citas = [c for c in self.citas if c[0] != descripcion]


# --- Programa principal / prueba ---
a = Agenda()
a.agregar_cita("Dentista", 9)
a.agregar_cita("Reunion", 15)
print(a.citas_de_la_manana())   #  [('Dentista', 9)]
a.cancelar_cita("Dentista")
print(a.citas)                  # [('Reunion', 15)]
