#Analizador de patrones en textos
#Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) 
# que busque palabras que inicien con el patrón y retorne una lista; 
# (2) tenga método agrupar_por_longitud(texto) que
#  retorne un diccionario {longitud: [palabras]}; (3) tenga método palabras_unicas() usando un conjunto.
#Entrada
#texto y patrón de búsqueda
#Proceso
#split(), filtrar, agrupar por longitud, eliminar duplicados
#Salida
#listas, diccionario, conjunto
#Ejemplo de entrada
#ap = AnalizadorPatrones()
#ap.agrupar_por_longitud("el gato está aquí")
#Salida esperada
#{2:['el'], 4:['gato'], 5:['está'], 5:['aquí']}
#Colecciones: todas (lista, diccionario, conjunto) + métodos de string (split, startswith)
class AnalizadorPatrones:
    def __init__(self):
        self.todas_las_palabras = set()  # conjunto: acumula todas las palabras vistas

    def encontrar_palabras(self, texto, patron):
        """Retorna las palabras del texto que empiezan con el patrón dado."""
        palabras = texto.split()
        self.todas_las_palabras.update(palabras)
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        """Retorna un diccionario {longitud: [palabras]} a partir del texto."""
        palabras = texto.split()
        self.todas_las_palabras.update(palabras)
        agrupado = {}
        for palabra in palabras:
            agrupado.setdefault(len(palabra), []).append(palabra)
        return agrupado

    def palabras_unicas(self):
        """Retorna el conjunto de todas las palabras únicas vistas hasta ahora."""
        return self.todas_las_palabras


# --- Programa principal / prueba ---
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))

# OTRO EJERCICIO

#Analizador de sufijos e iniciales
#Clase AnalizadorSufijos que: (1) tenga método encontrar_por_sufijo(texto, sufijo)
# que busque palabras que terminen con el sufijo y retorne una lista;
# (2) tenga método agrupar_por_inicial(texto) que
#  retorne un diccionario {inicial: [palabras]}; (3) tenga método palabras_unicas() usando un conjunto
# (en minúsculas).
#Entrada
#texto y sufijo de búsqueda
#Proceso
#split(), filtrar con endswith, agrupar por primera letra, eliminar duplicados
#Salida
#listas, diccionario, conjunto
#Ejemplo de entrada
#asf = AnalizadorSufijos()
#asf.encontrar_por_sufijo("cantar bailar correr saltar", "ar")
#asf.agrupar_por_inicial("el gato y el perro")
#Salida esperada
#['cantar', 'bailar', 'saltar']
#{'e': ['el', 'el'], 'g': ['gato'], 'y': ['y'], 'p': ['perro']}
#Colecciones: todas (lista, diccionario, conjunto) + métodos de string (split, endswith)
class AnalizadorSufijos:
    def __init__(self):
        self.todas_las_palabras = set()  # conjunto: acumula todas las palabras vistas

    def encontrar_por_sufijo(self, texto, sufijo):
        """Retorna las palabras del texto que terminan con el sufijo dado."""
        palabras = texto.split()
        self.todas_las_palabras.update(p.lower() for p in palabras)
        return [p for p in palabras if p.endswith(sufijo)]

    def agrupar_por_inicial(self, texto):
        """Retorna un diccionario {inicial: [palabras]} a partir del texto."""
        palabras = texto.split()
        self.todas_las_palabras.update(p.lower() for p in palabras)
        agrupado = {}
        for palabra in palabras:
            agrupado.setdefault(palabra[0].lower(), []).append(palabra)
        return agrupado

    def palabras_unicas(self):
        """Retorna el conjunto de todas las palabras únicas vistas hasta ahora."""
        return self.todas_las_palabras


# --- Programa principal / prueba ---
asf = AnalizadorSufijos()
print(asf.encontrar_por_sufijo("cantar bailar correr saltar", "ar"))   # -> ['cantar', 'bailar', 'saltar']
print(asf.agrupar_por_inicial("el gato y el perro"))
# {'e': ['el', 'el'], 'g': ['gato'], 'y': ['y'], 'p': ['perro']}
print(sorted(asf.palabras_unicas()))
