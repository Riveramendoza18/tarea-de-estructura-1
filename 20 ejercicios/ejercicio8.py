#Asignador de equipos
# Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) 
# que inicie un equipo como una lista vacía en un diccionario; (2) 
# tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
# (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
#Entrada
#nombres de equipos y jugadores
#Proceso
#crear estructura equipo→[jugadores], contar, comparar
#Salida
#equipo con mayor cantidad
#Ejemplo de entrada
#eq = Equipos()
#eq.crear_equipo("A")
#eq.agregar_jugador("A","Juan")
#eq.agregar_jugador("A","Pedro")
#Salida esperada
#—
#Colecciones: diccionario de listas (estructura anidada)
class Equipos:
    def __init__(self):
        self.equipos = {}  # diccionario

    def crear_equipo(self, nombre_equipo):
        """Crea un nuevo equipo con una lista vacía de jugadores."""
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        """Añade un jugador a la lista del equipo indicado."""
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        """Retorna el nombre del equipo con más jugadores."""
        return max(self.equipos, key=lambda eq: len(self.equipos[eq]))


# --- Programa principal / prueba ---
eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
print(eq.equipos)                        # {'A': ['Juan', 'Pedro']}
print(eq.equipo_mayor_integrantes())     #  'A'

# OTRO EJERCICIO
#Gestor de cursos e inscripciones
# Clase Cursos que: (1) tenga método crear_curso(nombre_curso)
# que inicie un curso como una lista vacía en un diccionario; (2)
# tenga método inscribir_alumno(curso, alumno) que añada el alumno al curso y retorne True,
# o retorne False si el curso no existe o el alumno ya estaba inscrito;
# (3) tenga método curso_con_menos_alumnos() que retorne el nombre del curso con menos alumnos.
#Entrada
# nombres de cursos y alumnos
#Proceso
# crear estructura curso→[alumnos], validar, contar, comparar
#Salida
# True/False y curso con menor cantidad
#Ejemplo de entrada
# c = Cursos()
# c.crear_curso("Python")
# c.crear_curso("Java")
# c.inscribir_alumno("Python", "Arnol")
# c.inscribir_alumno("Python", "Luna")
# c.inscribir_alumno("Java", "Arnol")
# c.inscribir_alumno("Python", "Arnol")
# c.curso_con_menos_alumnos()
#Salida esperada
# True, True, True, False
# 'Java'
#Colecciones: diccionario de listas (estructura anidada)
class Cursos:
    def __init__(self):
        self.cursos = {}  # diccionario: nombre_curso -> [alumnos]

    def crear_curso(self, nombre_curso):
        """Crea un nuevo curso con una lista vacía de alumnos."""
        self.cursos[nombre_curso] = []

    def inscribir_alumno(self, curso, alumno):
        """Inscribe al alumno. Retorna False si el curso no existe o el alumno ya está inscrito."""
        if curso not in self.cursos or alumno in self.cursos[curso]:
            return False
        self.cursos[curso].append(alumno)
        return True

    def curso_con_menos_alumnos(self):
        """Retorna el nombre del curso con menos alumnos inscritos."""
        return min(self.cursos, key=lambda c: len(self.cursos[c]))


# --- Programa principal / prueba ---
c = Cursos()
c.crear_curso("Python")
c.crear_curso("Java")
print(c.inscribir_alumno("Python", "Arnol"))    #  True
print(c.inscribir_alumno("Python", "Luna"))   # True
print(c.inscribir_alumno("Java", "Arnol"))      #  True
print(c.inscribir_alumno("Python", "Arnol"))    #  False (ya inscrita)
print(c.cursos)                               #  {'Python': ['Arnol', 'Luna'], 'Java': ['Arnol']}
print(c.curso_con_menos_alumnos())            #  'Java'
