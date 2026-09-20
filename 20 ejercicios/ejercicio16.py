#Codificador/Decodificador
#Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) 
# que retorne la letra desplazada en el alfabeto (usar operador %);
#  (2) tenga método codificar_palabra(palabra, desplazamiento) 
# que reutilice para toda la palabra; (3) tenga un diccionario como atributo para historial de codificaciones.
#Entrada
#letra/palabra y desplazamiento (1-25)
#Proceso
#convertir a código ASCII, desplazar con %, guardar historial
#Salida
#palabra codificada
#Ejemplo de entrada
#cc = CodificadorCesar()
#cc.codificar_palabra("hola", 3)
#Salida esperada
#"kroc" (aprox, solo ejemplo)
#Colecciones: diccionario para historial; ord() y chr() para conversión
class CodificadorCesar:
    def __init__(self):
        self.historial = {}  # diccionario: palabra_original -> palabra_codificada

    def codificar_letra(self, letra, desplazamiento):
        """Desplaza una letra 'desplazamiento' posiciones en el alfabeto (usando %)."""
        if not letra.isalpha():
            return letra  # los caracteres que no son letras se dejan igual
        base = ord('A') if letra.isupper() else ord('a')
        return chr((ord(letra) - base + desplazamiento) % 26 + base)

    def codificar_palabra(self, palabra, desplazamiento):
        """Codifica cada letra de la palabra reutilizando codificar_letra, y guarda el historial."""
        codificada = "".join(self.codificar_letra(letra, desplazamiento) for letra in palabra)
        self.historial[palabra] = codificada
        return codificada


# --- Programa principal / prueba ---
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))   # "krod"

# OTRO EJERCICIO
#Codificador Atbash
#Clase CodificadorAtbash que: (1) tenga método codificar_letra(letra)
# que retorne la letra "espejo" del alfabeto (a↔z, b↔y, c↔x, ...) usando ord() y chr();
#  (2) tenga método codificar_palabra(palabra) que reutilice el anterior para toda la palabra
# y guarde el resultado en un diccionario como historial; (3) tenga método decodificar_palabra(palabra)
# que devuelva el texto original.
#Entrada
#letra o palabra
#Proceso
#convertir a código ASCII, calcular la posición espejo (25 - posición), guardar historial
#Salida
#palabra codificada / decodificada
#Ejemplo de entrada
#ca = CodificadorAtbash()
#ca.codificar_palabra("hola")
#Salida esperada
#"sloz"
#Colecciones: diccionario para historial; ord() y chr() para conversión
class CodificadorAtbash:
    def __init__(self):
        self.historial = {}  # diccionario: palabra_original -> palabra_codificada

    def codificar_letra(self, letra):
        """Retorna la letra espejo del alfabeto (a<->z). Lo que no es letra se deja igual."""
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        posicion = ord(letra) - base
        return chr(base + (25 - posicion))

    def codificar_palabra(self, palabra):
        """Codifica cada letra reutilizando codificar_letra y guarda el historial."""
        codificada = "".join(self.codificar_letra(letra) for letra in palabra)
        self.historial[palabra] = codificada
        return codificada

    def decodificar_palabra(self, palabra):
        """Atbash es simétrico: aplicarlo de nuevo devuelve el texto original."""
        return "".join(self.codificar_letra(letra) for letra in palabra)


# --- Programa principal / prueba ---
ca = CodificadorAtbash()
print(ca.codificar_palabra("hola"))       #  "sloz"
print(ca.decodificar_palabra("sloz"))      # "hola"
print(ca.historial)                       #{'hola': 'sloz'}
