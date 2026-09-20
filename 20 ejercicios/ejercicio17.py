#Grupo de edades
#Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) 
# que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
# (2) tenga método agrupar_por_categoria(*edades) 
# que retorne un diccionario con {categoría: [edades]}; 
# (3) tenga método edad_promedio_categoria(categoria).
#Entrada
#edades en lote
#Proceso
#clasificar con if/elif, agrupar en diccionario
#Salida
#diccionario agrupado, promedio
#Ejemplo de entrada
#ae = AgrupadorEdades()
#ae.agrupar_por_categoria(5, 15, 30, 70)
#Salida esperada
#{'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}
#Colecciones: diccionario de listas (estructura anidada)
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}

    def clasificar_edad(self, edad):
        """Retorna la categoría según rangos de edad definidos."""
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        """Clasifica cada edad y la agrega a la lista de su categoría correspondiente."""
        for edad in edades:
            categoria = self.clasificar_edad(edad)   # reutiliza el método base
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        """Retorna el promedio de edades dentro de una categoría dada."""
        edades = self.grupos.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)


# --- Programa principal / prueba ---
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
# {'niño': [5], 'adolescente': [15], 'adulto': [30], 'mayor': [70]}

# OTRO EJERCICIO
#Agrupador de notas por letra
#Clase AgrupadorNotas que: (1) tenga método clasificar_nota(nota)
# que retorne la letra ("A" ≥ 90, "B" ≥ 80, "C" ≥ 70, "D" ≥ 60, "F" el resto);
# (2) tenga método agrupar_por_letra(*notas)
# que retorne un diccionario con {letra: [notas]}; (3) tenga método promedio_letra(letra).
#Entrada
#notas en lote
#Proceso
#clasificar con if/elif, agrupar en diccionario
#Salida
#diccionario agrupado, promedio
#Ejemplo de entrada
#an = AgrupadorNotas()
#an.agrupar_por_letra(95, 82, 71, 64, 30, 91)
#an.promedio_letra("A")
#Salida esperada
#{'A': [95, 91], 'B': [82], 'C': [71], 'D': [64], 'F': [30]}
#93.0
#Colecciones: diccionario de listas (estructura anidada)
class AgrupadorNotas:
    def __init__(self):
        self.grupos = {"A": [], "B": [], "C": [], "D": [], "F": []}

    def clasificar_nota(self, nota):
        """Retorna la letra según el rango de la nota."""
        if nota >= 90:
            return "A"
        elif nota >= 80:
            return "B"
        elif nota >= 70:
            return "C"
        elif nota >= 60:
            return "D"
        else:
            return "F"

    def agrupar_por_letra(self, *notas):
        """Clasifica cada nota y la agrega a la lista de su letra correspondiente."""
        for nota in notas:
            letra = self.clasificar_nota(nota)   # reutiliza el método base
            self.grupos[letra].append(nota)
        return self.grupos

    def promedio_letra(self, letra):
        """Retorna el promedio de notas dentro de una letra dada."""
        notas = self.grupos.get(letra, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)


# --- Programa principal / prueba ---
an = AgrupadorNotas()
print(an.agrupar_por_letra(95, 82, 71, 64, 30, 91))
#  {'A': [95, 91], 'B': [82], 'C': [71], 'D': [64], 'F': [30]}
print(an.promedio_letra("A"))   #  93.0
