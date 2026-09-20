#Mapeador de edades
#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) 
# que guarde en un diccionario; (2) tenga método personas_mayores(edad_minima) 
#  retorne una lista de nombres cuya edad sea ≥; (3) tenga método edad_promedio() 
# que retorne el promedio de edades.
#Entrada
#nombres y edades
#Proceso
#guardar en diccionario, filtrar, promediar
#Salida
#lista filtrada, promedio
#Ejemplo de entrada
#gp = GestorPersonas()
#gp.agregar_persona("Ana",28)
#gp.agregar_persona("Bob",17)
#gp.personas_mayores(18)
#Salida esperada
#["Ana"]
#Colecciones: diccionario nombre→edad, iteración con items()
class GestorPersonas:
    def __init__(self):
        self.personas = {}  # diccionario nombre -> edad

    def agregar_persona(self, nombre, edad):
        """Guarda la persona con su edad en el diccionario."""
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        """Retorna una lista de nombres cuya edad sea >= edad_minima."""
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]

    def edad_promedio(self):
        """Retorna el promedio de todas las edades registradas."""
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)


# --- Programa principal / prueba ---
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))   #  ['Ana']

# OTRO EJERCICIO
#Mapeador de sueldos
#Clase GestorEmpleados que: (1) tenga método agregar_empleado(nombre, sueldo)
# que guarde en un diccionario; (2) tenga método empleados_sueldo_menor(sueldo_maximo)
# que retorne una lista de nombres cuyo sueldo sea < sueldo_maximo; (3) tenga método sueldo_promedio()
# que retorne el promedio de sueldos.
#Entrada
# nombres y sueldos
#Proceso
# guardar en diccionario, filtrar, promediar
#Salida
# lista filtrada, promedio
#Ejemplo de entrada
# ge = GestorEmpleados()
# ge.agregar_empleado("Luisa", 900)
# ge.agregar_empleado("Martin", 1500)
# ge.agregar_empleado("samuel", 1200)
# ge.empleados_sueldo_menor(1300)
# ge.sueldo_promedio()
#Salida esperada
# ['Luisa', 'samuel']
# 1200.0
#Colecciones: diccionario nombre→sueldo, iteración con items()
class GestorEmpleados:
    def __init__(self):
        self.empleados = {}  # diccionario nombre -> sueldo

    def agregar_empleado(self, nombre, sueldo):
        """Guarda el empleado con su sueldo en el diccionario."""
        self.empleados[nombre] = sueldo

    def empleados_sueldo_menor(self, sueldo_maximo):
        """Retorna una lista de nombres cuyo sueldo sea menor que sueldo_maximo."""
        return [nombre for nombre, sueldo in self.empleados.items() if sueldo < sueldo_maximo]

    def sueldo_promedio(self):
        """Retorna el promedio de todos los sueldos registrados."""
        if not self.empleados:
            return 0
        return sum(self.empleados.values()) / len(self.empleados)


# --- Programa principal / prueba ---
ge = GestorEmpleados()
ge.agregar_empleado("Luisa", 900)
ge.agregar_empleado("Martin", 1500)
ge.agregar_empleado("samuel", 1200)
print(ge.empleados_sueldo_menor(1300))   # ['Luisa', 'samuel']
print(ge.sueldo_promedio())              #  1200.0
