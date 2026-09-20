#Inversor de secuencias
#Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) 
# que retorne la lista invertida sin usar reversed() 
# (usa manual con bucles); (2) tenga método invertir_multiples(*listas) 
# que reutilice el anterior para invertir varias listas y retorne un diccionario 
# {lista_original: lista_invertida}.
#Entrada
# lista o varias listas
#Proceso
# invertir manualmente, guardar en diccionario
#Salida
# lista invertida o diccionario
#Ejemplo de entrada
# inv = InversorSecuencia()
# inv.invertir_lista([1,2,3])
# Salida esperada
# [3, 2, 1]
# Colecciones: listas y diccionarios con tuplas como claves
class InversorSecuencia:
    def __init__(self):
        """Inicializa la clase, aunque no necesita guardar estado."""
        pass

    def invertir_lista(self, lista):
        """Retorna la lista invertida, recorriéndola manualmente de atrás hacia adelante."""
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        """Recibe varias listas y reutiliza invertir_lista para cada una."""
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)  # tuple: la lista original como clave
        return resultado


# --- Programa principal / prueba ---
inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))   # [3, 2, 1]

# OTRO EJERCICIO

#Rotador de secuencias
#Clase RotadorSecuencia que: (1) tenga método rotar_lista(lista, k)
# que retorne la lista rotada k posiciones hacia la derecha sin usar slicing
# (usa manual con bucles y el operador %); (2) tenga método rotar_multiples(k, *listas)
# que reutilice el anterior para rotar varias listas y retorne un diccionario
# {tupla_original: lista_rotada}.
#Entrada
# una lista y k, o varias listas
#Proceso
# calcular la nueva posición de cada elemento con %, guardar en diccionario
#Salida
# lista rotada o diccionario
#Ejemplo de entrada
# rot = RotadorSecuencia()
# rot.rotar_lista([1,2,3,4,5], 2)
# Salida esperada
# [4, 5, 1, 2, 3]
# Colecciones: listas y diccionarios con tuplas como claves
class RotadorSecuencia:
    def rotar_lista(self, lista, k):
        """Retorna la lista rotada k posiciones a la derecha, sin slicing."""
        n = len(lista)
        if n == 0:
            return []
        resultado = [None] * n
        for i in range(n):
            resultado[(i + k) % n] = lista[i]   # nueva posición usando %
        return resultado

    def rotar_multiples(self, k, *listas):
        """Recibe varias listas y reutiliza rotar_lista para cada una."""
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.rotar_lista(lista, k)   # tuple: la lista original como clave
        return resultado


# --- Programa principal / prueba ---
rot = RotadorSecuencia()
print(rot.rotar_lista([1, 2, 3, 4, 5], 2))            # [4, 5, 1, 2, 3]
print(rot.rotar_multiples(1, [1, 2, 3], ["a", "b"]))  # {(1, 2, 3): [3, 1, 2], ('a', 'b'): ['b', 'a']}
