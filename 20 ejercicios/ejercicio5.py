#Detector de números pares e impares
#Clase AnalizadorNumeros que: (1) tenga método es_par(numero) 
# que retorne True/False; (2) tenga método separar(*numeros) 
# que retorne un diccionario {'pares': [...], 'impares': [...]} 
# reutilizando es_par; (3) tenga método cantidad_pares_impares() 
# que retorne una tupla (cant_pares, cant_impares).
# Entrada
# números en lote
# Proceso
# clasificar pares e impares con operador %
# Salida
# diccionario y tupla con cantidades
# Ejemplo de entrada
# an = AnalizadorNumeros()
# an.separar(1,2,3,4,5)
# Salida esperada
# {'pares':[2,4], 'impares':[1,3,5]}
# Colecciones: diccionario con claves string y valores list

class AnalizadorNumeros:
    def __init__(self):
        self.numeros = {"pares": [], "impares": []}

    def es_par(self, numero):
        """Retorna True si el numero es par y False en caso contrario."""
        return numero % 2 == 0

    def separar(self, *numeros):
        """Clasifica numeros en pares e impares reutilizando es_par."""
        self.numeros = {"pares": [], "impares": []}
        for numero in numeros:
            if self.es_par(numero):
                self.numeros["pares"].append(numero)
            else:
                self.numeros["impares"].append(numero)
        return self.numeros

    def cantidad_pares_impares(self):
        """Retorna (cantidad de pares, cantidad de impares)."""
        return (len(self.numeros["pares"]), len(self.numeros["impares"]))


# Programa principal / prueba
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())  # (2, 3)

# OTRO EJERCICIO
#Clasificador de números por signo
#Clase AnalizadorSigno que: (1) tenga método es_positivo(numero)
# que retorne True/False; (2) tenga método separar(*numeros)
# que retorne un diccionario {'positivos': [...], 'negativos': [...], 'ceros': [...]} reutilizando es_positivo;
# (3) tenga método cantidad_por_signo() que retorne una tupla (cant_positivos, cant_negativos, cant_ceros)
# con base en la última separación realizada.
#Entrada
# números en lote
#Proceso
# clasificar con comparaciones (>, <), guardar en listas
#Salida
# diccionario y tupla con cantidades
#Ejemplo de entrada
# an = AnalizadorSigno()
# an.separar(3, -1, 0, 7, -8)
# an.cantidad_por_signo()
#Salida esperada
# {'positivos': [3, 7], 'negativos': [-1, -8], 'ceros': [0]}
# (2, 2, 1)
#Colecciones: diccionario con claves string y valores list
class AnalizadorSigno:
    def __init__(self):
        self.clasificados = {"positivos": [], "negativos": [], "ceros": []}

    def es_positivo(self, numero):
        """Retorna True si el número es mayor que cero."""
        return numero > 0

    def separar(self, *numeros):
        """Clasifica los números en positivos, negativos y ceros."""
        self.clasificados = {"positivos": [], "negativos": [], "ceros": []}
        for n in numeros:
            if self.es_positivo(n):        # reutilizamos el método a una base
                self.clasificados["positivos"].append(n)
            elif n < 0:
                self.clasificados["negativos"].append(n)
            else:
                self.clasificados["ceros"].append(n)
        return self.clasificados

    def cantidad_por_signo(self):
        """Retorna (cant_positivos, cant_negativos, cant_ceros) de la última separación."""
        return (len(self.clasificados["positivos"]),
                len(self.clasificados["negativos"]),
                len(self.clasificados["ceros"]))


# --- Programa principal / prueba ---
an = AnalizadorSigno()
print(an.separar(3, -1, 0, 7, -8))   # {'positivos': [3, 7], 'negativos': [-1, -8], 'ceros': [0]}
print(an.cantidad_por_signo())       # (2, 2, 1)
