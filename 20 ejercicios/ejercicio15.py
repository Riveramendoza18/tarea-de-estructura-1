#Divisores de un número
#Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) 
# que retorne una tupla con todos los divisores; (2) tenga método es_perfecto(numero) 
# que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; (3) 
# tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
#Entrada
#uno o varios números
#Proceso
#encontrar divisores con bucles, verificar suma
#Salida
#tuplas, booleano, diccionario
#Ejemplo de entrada
#df = DivisorFinder()
#df.encontrar_divisores(12)
#Salida esperada
#(1, 2, 3, 4, 6, 12)
#Colecciones: tuplas (inmutables), diccionario como almacén
class DivisorFinder:
    def __init__(self):
        """Inicializa la clase, aunque no necesita guardar estado."""
        pass

    def encontrar_divisores(self, numero):
        """Retorna una tupla con todos los divisores del número (incluyéndolo a él mismo)."""
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        """Retorna True si la suma de sus divisores (sin contarlo a él mismo) es igual al número."""
        divisores = self.encontrar_divisores(numero)   # reutiliza el método base
        return sum(d for d in divisores if d != numero) == numero

    def encontrar_multiples_divisores(self, *numeros):
        """Recibe varios números y retorna un diccionario {número: tupla_de_divisores}."""
        return {n: self.encontrar_divisores(n) for n in numeros}


# --- Programa principal / prueba ---
df = DivisorFinder()
print(df.encontrar_divisores(12))   #  (1, 2, 3, 4, 6, 12)


# OTRO EJERCICIO
#Números primos
#Clase PrimosFinder que: (1) tenga método es_primo(numero)
# que retorne True si el número es primo; (2) tenga método primos_en_rango(inicio, fin)
# que retorne una tupla con todos los primos del rango (inclusive) reutilizando es_primo; (3)
# tenga método analizar_multiples(*numeros) que retorne un diccionario {número: True/False}.
#Entrada
#uno o varios números, o un rango
#Proceso
#probar divisibilidad con bucles hasta la raíz cuadrada
#Salida
#booleano, tuplas, diccionario
#Ejemplo de entrada
#pf = PrimosFinder()
#pf.primos_en_rango(10, 30)
#Salida esperada
#(11, 13, 17, 19, 23, 29)
#Colecciones: tuplas (inmutables), diccionario como almacén
class PrimosFinder:
    def es_primo(self, numero):
        """Retorna True si el número es primo (mayor que 1 y sin divisores propios)."""
        if numero < 2:
            return False
        i = 2
        while i * i <= numero:
            if numero % i == 0:
                return False
            i += 1
        return True

    def primos_en_rango(self, inicio, fin):
        """Retorna una tupla con los números primos entre inicio y fin (inclusive)."""
        primos = []
        for n in range(inicio, fin + 1):
            if self.es_primo(n):   # reutiliza el método base
                primos.append(n)
        return tuple(primos)

    def analizar_multiples(self, *numeros):
        """Recibe varios números y retorna un diccionario {número: es_primo}."""
        return {n: self.es_primo(n) for n in numeros}


# --- Programa principal / prueba ---
pf = PrimosFinder()
print(pf.primos_en_rango(10, 30))          #  (11, 13, 17, 19, 23, 29)
print(pf.analizar_multiples(7, 9, 1, 13))  #  {7: True, 9: False, 1: False, 13: True}
