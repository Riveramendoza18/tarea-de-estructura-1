#Validador de notas con promedio
#Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, 
# False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, 
# agregue solo las válidas a una lista interna, y retorne esa lista; (3) tenga método promedio()
#  que retorne el promedio de notas almacenadas.
# Entrada
# notas individuales o en lotes (*args)
# Proceso
# validar cada nota (0-100), guardar en lista, calcular promedio
# Salida
# True/False, lista de válidas, promedio
# Ejemplo de entrada
# c = Calificador()
# c.cargar_notas(85, 92, 110, 78, -5, 88)
# c.promedio()
# Salida esperada
# [85, 92, 78, 88]
# 85.75
# Colecciones: lista interna de notas válidas
class Calificador:
    def __init__(self):
        self.notas = []  # lista interna donde se guardan solo las notas válidas

    def validar_nota(self, nota):
        """Retorna True si la nota está entre 0 y 100, False en caso contrario."""
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        """Recibe varias notas (*args), valida cada una y guarda solo las válidas."""
        for nota in args:
            if self.validar_nota(nota):   # reutiliza el método base
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        """Retorna el promedio de las notas válidas almacenadas."""
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)


# --- Programa principal / prueba ---
c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))   # [85, 92, 78, 88]
print(c.promedio())  

#otro ejercicio que se hizosimilar pero diferente valores

#Validador de salarios con promedio
#Clase RegistroSalarios que: (1) tenga método validar_salario(salario) que retorne True si 400 ≤ salario ≤ 5000,
# False en caso contrario; (2) tenga método cargar_salarios(*args) que reciba múltiples salarios, los valide,
# agregue solo los válidos a una lista interna, y retorne esa lista; (3) tenga método promedio()
# que retorne el promedio de los salarios almacenados.
# Entrada
# salarios individuales o en lotes (*args)
# Proceso
# validar cada salario (400-5000), guardar en lista, calcular promedio
# Salida
# True/False, lista de válidos, promedio
# Ejemplo de entrada
# rs = RegistroSalarios()
# rs.cargar_salarios(450, 1200, 90, 6000, 800, -20, 2500)
# rs.promedio()
# Salida esperada
# [450, 1200, 800, 2500]
# 1237.5
# Colecciones: lista interna de salarios válidos
class RegistroSalarios:
    def __init__(self):
        self.salarios = []  # lista interna donde se guardan solo los salarios válidos

    def validar_salario(self, salario):
        """Retorna True si el salario está entre 400 y 5000, False en caso contrario."""
        return 400 <= salario <= 5000

    def cargar_salarios(self, *args):
        """Recibe varios salarios (*args), valida cada uno y guarda solo los válidos."""
        for salario in args:
            if self.validar_salario(salario):   # reutiliza el método base
                self.salarios.append(salario)
        return self.salarios

    def promedio(self):
        """Retorna el promedio de los salarios válidos almacenados."""
        if not self.salarios:
            return 0
        return sum(self.salarios) / len(self.salarios)


# --- Programa principal / prueba ---
rs = RegistroSalarios()
print(rs.cargar_salarios(450, 1200, 90, 6000, 800, -20, 2500))   #[450, 1200, 800, 2500]
print(rs.promedio())  