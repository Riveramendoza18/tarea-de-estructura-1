#Gestor de compras con totales
# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio)
#  que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito()
# que retorne la suma de todos los precios; (3) tenga método articulos_por_rango(precio_min, precio_max)
#  que retorne una lista con artículos dentro del rango.
# Entrada
# nombres de artículos y precios
# Proceso
# guardar en diccionario, sumar valores, filtrar por rango
# Salida
# total, artículos en rango
# Ejemplo de entrada
# c = CarroCompras()
# c.agregar_articulo("pan",2.50)
# c.agregar_articulo("leche",3.00)
# c.total_carrito()
# Salida esperada
# 5.50
#  Colecciones: diccionario para almacenar nombre→precio
class CarroCompras:
    def __init__(self):
        self.articulos = {}  # diccionario nombre -> precio

    def agregar_articulo(self, nombre, precio):
        """Guarda el artículo con su precio en el diccionario."""
        self.articulos[nombre] = precio

    def total_carrito(self):
        """Retorna la suma de todos los precios guardados."""
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        """Retorna los nombres de artículos cuyo precio está dentro del rango."""
        return [nombre for nombre, precio in self.articulos.items()
                if precio_min <= precio <= precio_max]


# --- Programa principal / prueba ---
c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
print(c.total_carrito())   #5.5

# otro ejercicio similar pero diferente

#Control de presupuesto de gastos
# Clase Presupuesto que: (1) tenga método agregar_gasto(concepto, monto)
# que guarde en un diccionario {concepto: monto}; (2) tenga método total_gastos()
# que retorne la suma de todos los montos; (3) tenga método gastos_mayores_a(monto_minimo)
# que retorne una lista con los conceptos cuyo monto supere el mínimo.
# Entrada
# conceptos de gasto y montos
# Proceso
# guardar en diccionario, sumar valores, filtrar por monto
# Salida
# total, conceptos filtrados
# Ejemplo de entrada
# p = Presupuesto()
# p.agregar_gasto("transporte", 15.50)
# p.agregar_gasto("comida", 40)
# p.agregar_gasto("internet", 25)
# p.total_gastos()
# p.gastos_mayores_a(20)
# Salida esperada
# 80.5
# ['comida', 'internet']
# Colecciones: diccionario para almacenar concepto→monto
class Presupuesto:
    def __init__(self):
        self.gastos = {}  # diccionario concepto -> monto

    def agregar_gasto(self, concepto, monto):
        """Guarda el gasto con su monto en el diccionario."""
        self.gastos[concepto] = monto

    def total_gastos(self):
        """Retorna la suma de todos los montos guardados."""
        return sum(self.gastos.values())

    def gastos_mayores_a(self, monto_minimo):
        """Retorna los conceptos cuyo monto es mayor que el mínimo."""
        return [concepto for concepto, monto in self.gastos.items() if monto > monto_minimo]


# --- Programa principal / prueba ---
p = Presupuesto()
p.agregar_gasto("transporte", 15.50)
p.agregar_gasto("comida", 40)
p.agregar_gasto("internet", 25)
print(p.total_gastos())         # 80.5
print(p.gastos_mayores_a(20))   # ['comida', 'internet']

