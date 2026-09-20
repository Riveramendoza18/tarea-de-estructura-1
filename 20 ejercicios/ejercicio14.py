#Mapeo de estudiantes a notas
# Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota)
#  que guarde en un diccionario; (2) tenga método estudiantes_aprobados(nota_minima) 
#  que retorne lista de estudiantes; (3) tenga método mejor_estudiante() 
# que retorne nombre y nota del que tiene mayor calificación.
# Entrada
# estudiante → nota
# Proceso
# guardar diccionario, iterar con items(), comparar
# Salida
# listas filtradas, tupla (nombre, nota)
# Ejemplo de entrada
# rn = RegistroNotas()
# rn.registrar("Ana", 95)
# rn.registrar("Bob", 70)
# rn.mejor_estudiante()
# Salida esperada
# ("Ana", 95)
# Colecciones: diccionario.items() para iterar clave-valor

class RegistroNotas:
    def __init__(self):
        self.notas = {}  # diccionario

    def registrar(self, estudiante, nota):
        """Guarda o actualiza la nota de un estudiante."""
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        """Retorna una lista de nombres cuya nota sea >= nota_minima."""
        return [nombre for nombre, nota in self.notas.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        """Retorna una tupla (nombre, nota) del estudiante con la nota más alta."""
        nombre = max(self.notas, key=self.notas.get)
        return (nombre, self.notas[nombre])


# --- Programa principal / prueba ---
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.mejor_estudiante())   # ('Ana', 95)

# OTRO EJERCICIO
#Registro de goles por jugador
# Clase RegistroGoles que: (1) tenga método registrar(jugador, goles)
#  que guarde en un diccionario ACUMULANDO los goles del jugador; (2) tenga método goleadores(minimo)
#  que retorne lista de jugadores con al menos esa cantidad de goles; (3) tenga método maximo_goleador()
# que retorne nombre y goles del jugador con más goles.
# Entrada
# jugador → goles
# Proceso
# guardar/acumular en diccionario, iterar con items(), comparar
# Salida
# listas filtradas, tupla (nombre, goles)
# Ejemplo de entrada
# rg = RegistroGoles()
# rg.registrar("Angelica", 3)
# rg.registrar("Lorenzo", 1)
# rg.registrar("Angelica", 2)
# rg.registrar("Carla", 4)
# rg.maximo_goleador()
# rg.goleadores(4)
# Salida esperada
# ('Angelica', 5)
# ['Angelica', 'Carla']
# Colecciones: diccionario.items() para iterar clave-valor

class RegistroGoles:
    def __init__(self):
        self.goles = {}  # diccionario

    def registrar(self, jugador, goles):
        """Suma los goles al total acumulado del jugador."""
        self.goles[jugador] = self.goles.get(jugador, 0) + goles

    def goleadores(self, minimo):
        """Retorna una lista de jugadores con goles >= minimo."""
        return [jugador for jugador, g in self.goles.items() if g >= minimo]

    def maximo_goleador(self):
        """Retorna una tupla (jugador, goles) del jugador con más goles."""
        jugador = max(self.goles, key=self.goles.get)
        return (jugador, self.goles[jugador])


# --- Programa principal / prueba ---
rg = RegistroGoles()
rg.registrar("Angelica", 3)
rg.registrar("Lorenzo", 1)
rg.registrar("Angelica", 2)
rg.registrar("Carla", 4)
print(rg.maximo_goleador())   # ('Angelica', 5)
print(rg.goleadores(4))       # ['Angelica', 'Carla']
