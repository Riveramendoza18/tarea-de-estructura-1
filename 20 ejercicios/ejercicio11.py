#Contador de frecuencia
# Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) 
# que guarde en un diccionario contando repeticiones; (2) tenga método elemento_mas_frecuente()
# que retorne el elemento con mayor frecuencia; (3) tenga método frecuencia_elemento(elemento)
#  que retorne cuántas veces aparece.
# Entrada
# elementos individuales o en lote
# Proceso
# guardar en diccionario, contar, encontrar máximo
# Salida
# elemento más frecuente y su conteo
# Ejemplo de entrada
#cf = ContadorFrecuencia()
#cf.agregar_elemento("a")
#cf.agregar_elemento("b")
#cf.agregar_elemento("a")
#cf.elemento_mas_frecuente()
#Salida esperada
#"a"
# Colecciones: diccionario como contador (patrón común)
class ContadorFrecuencia:
    def __init__(self):
        self.conteo = {}  # diccionario: elemento -> cantidad de veces que aparece

    def agregar_elemento(self, elemento):
        """Suma 1 al contador del elemento, o lo crea con 1 si es la primera vez."""
        self.conteo[elemento] = self.conteo.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        """Retorna el elemento con mayor frecuencia registrada."""
        return max(self.conteo, key=self.conteo.get)

    def frecuencia_elemento(self, elemento):
        """Retorna cuántas veces ha aparecido un elemento (0 si nunca se agregó)."""
        return self.conteo.get(elemento, 0)


# --- Programa principal / prueba ---
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())   # "a"

# OTRO EJERCICIO
#Contador de votos
# Clase ContadorVotos que: (1) tenga método registrar_voto(candidato)
# que guarde en un diccionario contando los votos; (2) tenga método candidato_ganador()
# que retorne una tupla (candidato, votos) con el más votado; (3) tenga método votos_de(candidato)
#  que retorne cuántos votos tiene.
# Entrada
# votos individuales
# Proceso
# guardar en diccionario, contar, encontrar máximo
# Salida
# candidato ganador con su conteo, votos de un candidato
# Ejemplo de entrada
# cv = ContadorVotos()
# for v in ["Angel", "Lorena", "Angel", "Angel", "Lorena"]:
#     cv.registrar_voto(v)
# cv.candidato_ganador()
#Salida esperada
# ('Angel', 3)
# Colecciones: diccionario como contador (patrón común)
class ContadorVotos:
    def __init__(self):
        self.votos = {}  # diccionario: candidato -> cantidad de votos

    def registrar_voto(self, candidato):
        """Suma 1 al contador del candidato, o lo crea con 1 si es su primer voto."""
        self.votos[candidato] = self.votos.get(candidato, 0) + 1

    def candidato_ganador(self):
        """Retorna la tupla (candidato, votos) del más votado."""
        ganador = max(self.votos, key=self.votos.get)
        return (ganador, self.votos[ganador])

    def votos_de(self, candidato):
        """Retorna cuántos votos tiene un candidato (0 si nunca recibió uno)."""
        return self.votos.get(candidato, 0)


# --- Programa principal / prueba ---
cv = ContadorVotos()
for v in ["Angel", "Lorena", "Angel", "Angel", "Lorena"]:
    cv.registrar_voto(v)
print(cv.candidato_ganador())   #  ('Angel', 3)
print(cv.votos_de("Lorena"))      #  2
