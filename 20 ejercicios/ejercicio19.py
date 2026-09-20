#Inventario de productos
#Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) 
# que guarde en un diccionario; (2) tenga método restar_stock(producto, cantidad)
#  que disminuya y retorne True si hay suficiente; (3) tenga método productos_bajo_stock(minimo) 
# que retorne una lista de productos con cantidad < minimo.
#Entrada
#productos y cantidades
#Proceso
#guardar/actualizar diccionario, validar, filtrar
#Salida
#True/False, lista de productos
#Ejemplo de entrada
#inv = Inventario()
#inv.agregar_stock("pan", 50)
#inv.restar_stock("pan", 30)
#inv.productos_bajo_stock(15)
#Salida esperada
# True
#["pan"]
#Colecciones: diccionario como base de datos simple
class Inventario:
    def __init__(self):
        self.stock = {}  # diccionario: producto -> cantidad

    def agregar_stock(self, producto, cantidad):
        """Suma cantidad al stock del producto (o lo crea si no existía)."""
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        """Resta cantidad del stock si hay suficiente; retorna True/False."""
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        """Retorna los productos cuya cantidad es menor que el mínimo dado."""
        return [p for p, cant in self.stock.items() if cant < minimo]


# --- Programa principal / prueba ---
inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))       #  True
print(inv.productos_bajo_stock(15))      # []

# OTRO EJERCICIO

#Control de préstamos de biblioteca
#Clase Biblioteca que: (1) tenga método agregar_ejemplares(libro, cantidad)
# que guarde en un diccionario; (2) tenga método prestar_libro(libro)
#  que disminuya en 1 y retorne True si hay ejemplares disponibles, y devolver_libro(libro) que aumente en 1;
# (3) tenga método libros_agotados() que retorne una lista de libros con cantidad igual a 0.
#Entrada
#libros y cantidades
#Proceso
#guardar/actualizar diccionario, validar, filtrar
#Salida
#True/False, lista de libros
#Ejemplo de entrada
#b = Biblioteca()
#b.agregar_ejemplares("Python", 1)
#b.prestar_libro("Python")
#b.prestar_libro("Python")
#b.libros_agotados()
#Salida esperada
# True
# False
#['Python']
#Colecciones: diccionario como base de datos simple
class Biblioteca:
    def __init__(self):
        self.libros = {}  # diccionario: libro -> ejemplares disponibles

    def agregar_ejemplares(self, libro, cantidad):
        """Suma ejemplares al libro (o lo crea si no existía)."""
        self.libros[libro] = self.libros.get(libro, 0) + cantidad

    def prestar_libro(self, libro):
        """Presta un ejemplar si hay disponibles; retorna True/False."""
        if self.libros.get(libro, 0) > 0:
            self.libros[libro] -= 1
            return True
        return False

    def devolver_libro(self, libro):
        """Devuelve un ejemplar a la biblioteca."""
        self.libros[libro] = self.libros.get(libro, 0) + 1

    def libros_agotados(self):
        """Retorna los libros que no tienen ejemplares disponibles."""
        return [libro for libro, cant in self.libros.items() if cant == 0]


# --- Programa principal / prueba ---
b = Biblioteca()
b.agregar_ejemplares("Python", 1)
print(b.prestar_libro("Python"))    #  True
print(b.prestar_libro("Python"))    #  False
print(b.libros_agotados())          # ['Python']
b.devolver_libro("Python")
print(b.libros_agotados())          # []
