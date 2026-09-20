#Combinador de listas
# Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) 
# que retorne una lista alternando elementos de ambas; (2) tenga método intercalar_multiples(*listas)
#  que reutilice para varias listas.
# Entrada
# dos o más listas
# Proceso
# alternar elementos con índices, bucles
# Salida
# lista intercalada
# Ejemplo de entrada
#cl = CombinadorListas()
#cl.intercalar([1,2], [3,4])
#Salida esperada
#[1, 3, 2, 4]
# Colecciones: indexación de listas con loops y condicionales

class CombinadorListas:
    def __init__(self):
        """Inicializa la clase, aunque no necesita guardar estado."""
        pass

    def intercalar(self, lista1, lista2):
        """Retorna una lista alternando elementos de lista1 y lista2."""
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        """Reutiliza intercalar para combinar varias listas, de dos en dos."""
        if not listas:
            return []
        resultado = listas[0]
        for lista in listas[1:]:
            resultado = self.intercalar(resultado, lista)
        return resultado


# --- Programa principal / prueba ---
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))   # [1, 3, 2, 4]


# OTRO EJERCICIO
#Fusionador de listas ordenadas
# Clase FusionadorListas que: (1) tenga método fusionar_ordenadas(lista1, lista2)
# que retorne una sola lista ordenada a partir de dos listas ya ordenadas, usando dos índices
# (sin usar sort ni sorted); (2) tenga método fusionar_multiples(*listas)
#  que reutilice el anterior para varias listas.
# Entrada
# dos o más listas ordenadas
# Proceso
# comparar elementos con índices, bucles while y condicionales
# Salida
# lista fusionada y ordenada
# Ejemplo de entrada
# fl = FusionadorListas()
# fl.fusionar_ordenadas([1,4,7], [2,3,9])
#Salida esperada
# [1, 2, 3, 4, 7, 9]
# Colecciones: indexación de listas con while y condicionales

class FusionadorListas:
    def fusionar_ordenadas(self, lista1, lista2):
        """Fusiona dos listas ordenadas en una sola lista ordenada."""
        resultado = []
        i = j = 0
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):      # sobrantes de lista1
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):      # sobrantes de lista2
            resultado.append(lista2[j])
            j += 1
        return resultado

    def fusionar_multiples(self, *listas):
        """Reutiliza fusionar_ordenadas para combinar varias listas, de dos en dos."""
        if not listas:
            return []
        resultado = list(listas[0])
        for lista in listas[1:]:
            resultado = self.fusionar_ordenadas(resultado, lista)
        return resultado


# --- Programa principal / prueba ---
fl = FusionadorListas()
print(fl.fusionar_ordenadas([1, 4, 7], [2, 3, 9]))          # [1, 2, 3, 4, 7, 9]
print(fl.fusionar_multiples([1, 5], [2, 6], [0, 3, 10]))    # [0, 1, 2, 3, 5, 6, 10]
