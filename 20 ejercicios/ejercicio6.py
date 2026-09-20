#Estadísticas de temperatura
#Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp)
#  que guarde en una lista; (2) tenga método minima()`, `maxima()`, `promedio() 
# que calculen estadísticas; (3) tenga método registrar_multiples(*temps)
#  que reutilice el registro para varias temperaturas.
#Entrada
#temperaturas individuales o en lote
#Proceso
#guardar, calcular mín, máx, promedio
#Salida
#valores estadísticos
#Ejemplo de entrada
#gt = GestorTemperatura()
#gt.registrar_multiples(20,25,18,30)
#gt.promedio()
#Salida esperada
#23.25
#Colecciones: lista de números + funciones built-in min/max
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []  # lista donde se guardan todas las temperaturas registradas

    def registrar_temperatura(self, temp):
        """Guarda una temperatura en la lista."""
        self.temperaturas.append(temp)

    def minima(self):
        """Retorna la temperatura más baja registrada."""
        return min(self.temperaturas)

    def maxima(self):
        """Retorna la temperatura más alta registrada."""
        return max(self.temperaturas)

    def promedio(self):
        """Retorna el promedio de las temperaturas registradas."""
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        """Recibe varias temperaturas y reutiliza registrar_temperatura para cada una."""
        for t in temps:
            self.registrar_temperatura(t)


# --- Programa principal / prueba ---
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.promedio())   # -> 23.25

# OTRO EJERCICIO
#Estadísticas de pesos
#Clase RegistroPesos que: (1) tenga método registrar_peso(peso)
# que guarde en una lista; (2) tenga métodos minimo(), maximo() y mediana()
# que calculen estadísticas (la mediana requiere ordenar la lista); (3) tenga método registrar_multiples(*pesos)
# que reutilice el registro para varios pesos.
#Entrada
# pesos individuales o en lote
#Proceso
# guardar, calcular mín, máx, mediana
#Salida
# valores estadísticos
#Ejemplo de entrada
# rp = RegistroPesos()
# rp.registrar_multiples(70, 65, 80, 75)
# rp.mediana()
#Salida esperada
# 72.5
#Colecciones: lista de números + sorted() y funciones built-in min/max
class RegistroPesos:
    def __init__(self):
        self.pesos = []  # lista de los valores registrados
    def registrar_peso(self, peso):
        """Guarda un peso en la lista."""
        self.pesos.append(peso)

    def minimo(self):
        """Retorna el peso más bajo registrado."""
        return min(self.pesos)

    def maximo(self):
        """Retorna el peso más alto registrado."""
        return max(self.pesos)

    def mediana(self):
        """Retorna el valor central de los pesos ordenados (promedio de los dos centrales si es par)."""
        ordenados = sorted(self.pesos)
        n = len(ordenados)
        mitad = n // 2
        if n % 2 == 1:
            return ordenados[mitad]
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2

    def registrar_multiples(self, *pesos):
        """Recibe varios pesos y reutiliza registrar_peso para cada uno."""
        for p in pesos:
            self.registrar_peso(p)


# --- Programa principal / prueba ---
rp = RegistroPesos()
rp.registrar_multiples(70, 65, 80, 75)
print(rp.mediana())   # 72.5
print(rp.minimo(), rp.maximo())   # 65 80