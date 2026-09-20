#Selector de rango con tuplas
# Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) 
# que retorne una tupla con números en ese rango; (2) 
# tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin)
#  y retorne una lista combinada sin duplicados usando un conjunto.
# Entrada
# pares (inicio, fin) para varios rangos
# Proceso
# crear rangos como tuplas, unir sin duplicados
# Salida
# lista de elementos únicos
# Ejemplo de entrada
#sr = SelectorRango()
#sr.elementos_en_multiples_rangos((1,3), (2,4))
#Salida esperada
#[1, 2, 3, 4]
#Colecciones: tuplas como parámetros + conjuntos para eliminar duplicados
class SelectorRango:
    def __init__(self):
        """Inicializa la clase, aunque no necesita guardar estado."""
        pass

    def crear_rango(self, inicio, fin):
        """Retorna una tupla con todos los números desde inicio hasta fin (inclusive)."""
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        """Recibe varios pares (inicio, fin) y retorna una lista única combinando todos."""
        combinados = set()
        for inicio, fin in rangos:
            combinados.update(self.crear_rango(inicio, fin))   # se reutiliza crear_rango
        return sorted(combinados)


# --- Programa principal / prueba ---
sr = SelectorRango()
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))    [1, 2, 3, 4]


# OTRO EJERCICIO
#Intersección de rangos con tuplas
# Clase RangosComunes que: (1) tenga método crear_rango(inicio, fin, paso=1)
# que retorne una tupla con los números desde inicio hasta fin (inclusive) saltando de 'paso' en 'paso'; (2)
# tenga método elementos_comunes(*rangos) que reciba múltiples tuplas (inicio, fin)
#  y retorne una lista ordenada con los números que aparecen en TODOS los rangos, usando conjuntos.
# Entrada
# pares (inicio, fin) para varios rangos
# Proceso
# crear rangos como tuplas, intersectar conjuntos
# Salida
# lista de elementos comunes
# Ejemplo de entrada
# rc = RangosComunes()
# rc.elementos_comunes((1,6), (4,9))
#Salida esperada
# [4, 5, 6]
#Colecciones: tuplas como parámetros + conjuntos con intersección (&)
class RangosComunes:
    def crear_rango(self, inicio, fin, paso=1):
        """Retorna una tupla con los números de inicio a fin (inclusive) de 'paso' en 'paso'."""
        return tuple(range(inicio, fin + 1, paso))

    def elementos_comunes(self, *rangos):
        """Retorna la lista ordenada de números presentes en todos los rangos."""
        if not rangos:
            return []
        comunes = set(self.crear_rango(*rangos[0]))     # reutiliza crear_rango
        for inicio, fin in rangos[1:]:
            comunes &= set(self.crear_rango(inicio, fin))
        return sorted(comunes)


# --- Programa principal / prueba ---
rc = RangosComunes()
print(rc.elementos_comunes((1, 6), (4, 9)))                #  [4, 5, 6]
print(rc.elementos_comunes((1, 10), (5, 15), (8, 20)))     #  [8, 9, 10]
print(rc.crear_rango(0, 10, 5))                            #  (0, 5, 10)
