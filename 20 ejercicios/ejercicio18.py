#Matriz de distancias
#Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) 
# que reciba dos tuplas (x,y) y calcule la distancia;
#  (2) tenga método punto_mas_cercano(referencia, *puntos) 
# que retorne el punto más cercano a referencia;
#  (3) tenga un atributo lista para guardar todas las distancias calculadas.
#Entrada
#tuplas (x, y) como puntos
#Proceso
#calcular distancia con fórmula, comparar, guardar
#Salida
#distancia numérica, punto más cercano
#Ejemplo de entrada
#cd = CalculadorDistancia()
#cd.distancia_euclidiana((0,0), (3,4))
#Salida esperada
#5.0
#Colecciones: tuplas como puntos 2D; lista para guardar resultados
import math


class CalculadorDistancia:
    def __init__(self):
        self.distancias = []  # lista donde se guardan todas las distancias calculadas

    def distancia_euclidiana(self, p1, p2):
        """Calcula la distancia euclidiana entre dos puntos (x, y) y la guarda en la lista."""
        dist = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        self.distancias.append(dist)
        return dist

    def punto_mas_cercano(self, referencia, *puntos):
        """Retorna el punto más cercano a 'referencia', reutilizando distancia_euclidiana."""
        return min(puntos, key=lambda p: self.distancia_euclidiana(referencia, p))


# --- Programa principal / prueba ---
cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))   # 5.0

# OTRO EJERCICIO
#Distancia Manhattan en 3D
#Clase CalculadorManhattan que: (1) tenga método distancia_manhattan(p1, p2)
# que reciba dos tuplas (x,y,z) y calcule la suma de las diferencias absolutas;
#  (2) tenga método punto_mas_lejano(referencia, *puntos)
# que retorne el punto más lejano a referencia;
#  (3) tenga un atributo lista para guardar todas las distancias calculadas.
#Entrada
#tuplas (x, y, z) como puntos
#Proceso
#calcular distancia con abs(), comparar, guardar
#Salida
#distancia numérica, punto más lejano
#Ejemplo de entrada
#cm = CalculadorManhattan()
#cm.distancia_manhattan((0,0,0), (1,2,3))
#Salida esperada
#6
#Colecciones: tuplas como puntos 3D; lista para guardar resultados
class CalculadorManhattan:
    def __init__(self):
        self.distancias = []  # lista 

    def distancia_manhattan(self, p1, p2):
        """Calcula |x1-x2| + |y1-y2| + |z1-z2| y la guarda en la lista."""
        dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
        self.distancias.append(dist)
        return dist

    def punto_mas_lejano(self, referencia, *puntos):
        """Retorna el punto más lejano a 'referencia', reutilizando distancia_manhattan."""
        return max(puntos, key=lambda p: self.distancia_manhattan(referencia, p))


# --- Programa principal / prueba ---
cm = CalculadorManhattan()
print(cm.distancia_manhattan((0, 0, 0), (1, 2, 3)))                       #  6
print(cm.punto_mas_lejano((0, 0, 0), (1, 1, 1), (5, 0, 2), (2, 2, 2)))    #  (5, 0, 2)
print(cm.distancias)                                                      #  [6, 3, 7, 6]
