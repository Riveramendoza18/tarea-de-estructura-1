#Contador de palabras únicas
#Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra)
#  que agregue la palabra a un conjunto (para evitar duplicados)
#  y a una lista (para el orden); (2) tenga método contar_palabras() 
# que retorne cuántas palabras únicas hay; (3) tenga método agregar_multiples(*args)
#  que reutilice agregar_palabra para varios.
# Entrada
# palabras individuales o en lotes
# Proceso
# guardar en conjunto y lista, contar únicas
# Salida
# cantidad de palabras únicas
# Ejemplo de entrada
# at = AnalizadorTexto()
# at.agregar_multiples("hola","mundo","hola")
# at.contar_palabras()
# Salida esperada
# 2
# Colecciones: conjunto (para unicidad) + lista (para orden)
class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()   # conjunto: evita duplicados automáticamente
        self.palabras_orden = []       # lista: conserva el orden de llegada

    def agregar_palabra(self, palabra):
        """Agrega la palabra al conjunto y a la lista."""
        self.palabras_unicas.add(palabra)
        self.palabras_orden.append(palabra)

    def contar_palabras(self):
        """Retorna cuántas palabras únicas hay."""
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        """Recibe varias palabras y reutiliza agregar_palabra para cada una."""
        for palabra in args:
            self.agregar_palabra(palabra)


# --- Programa principal / prueba ---
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())   # 2

# otro ejercicio
#Catálogo de etiquetas únicas
#Clase CatalogoEtiquetas que: (1) tenga método agregar_etiqueta(etiqueta) que normalice la etiqueta
# (minúsculas y sin espacios en los extremos) y la agregue a un conjunto (para evitar duplicados)
# y a una lista (solo si es nueva, para conservar el orden de llegada); (2) tenga método contar_etiquetas()
# que retorne cuántas etiquetas únicas hay; (3) tenga método agregar_multiples(*args)
# que reutilice agregar_etiqueta para varias.
# Entrada
# etiquetas individuales o en lotes
# Proceso
# normalizar, guardar en conjunto y lista, contar únicas
# Salida
# cantidad de etiquetas únicas y lista ordenada de etiquetas
# Ejemplo de entrada
# ce = CatalogoEtiquetas()
# ce.agregar_multiples("Python", "java", "python", "  JAVA ", "c")
# ce.contar_etiquetas()
# ce.etiquetas_orden
# Salida esperada
# 3
# ['python', 'java', 'c']
# Colecciones: conjunto (para unicidad) + lista (para orden)
class CatalogoEtiquetas:
    def __init__(self):
        self.etiquetas_unicas = set()   # conjunto: evita duplicados automáticamente
        self.etiquetas_orden = []       # lista: conserva el orden de la primera aparición

    def agregar_etiqueta(self, etiqueta):
        """Normaliza la etiqueta y la agrega si aún no existe."""
        etiqueta = etiqueta.strip().lower()
        if etiqueta not in self.etiquetas_unicas:
            self.etiquetas_unicas.add(etiqueta)
            self.etiquetas_orden.append(etiqueta)

    def contar_etiquetas(self):
        """Retorna cuántas etiquetas únicas hay."""
        return len(self.etiquetas_unicas)

    def agregar_multiples(self, *args):
        """Recibe varias etiquetas y reutiliza agregar_etiqueta para cada una."""
        for etiqueta in args:
            self.agregar_etiqueta(etiqueta)


# --- Programa principal / prueba ---
ce = CatalogoEtiquetas()
ce.agregar_multiples("Python", "java", "python", "  JAVA ", "c")
print(ce.contar_etiquetas())   #  3
print(ce.etiquetas_orden)      # ['python', 'java', 'c']
