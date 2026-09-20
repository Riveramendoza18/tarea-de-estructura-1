#Validador de caracteres
# Clase AnalizadorString que: (1) tenga método solo_vocales(letra) 
# que retorne True si es vocal; (2) tenga método contar_por_tipo(texto) 
# que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} 
# reutilizando métodos; (3) tenga atributo que guarde el texto más largo analizado.
#Entrada
#textos para analizar
#Proceso
#recorrer carácter a carácter, clasificar
#Salida
#diccionario con conteos
#Ejemplo de entrada
#astr = AnalizadorString()
#astr.contar_por_tipo("Hola123")
#Salida esperada
#{'vocales':2, 'consonantes':2, 'digitos':3}
#Colecciones: diccionario para contar tipos
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""  # atributo 

    def solo_vocales(self, letra):
        """Retorna True si la letra es una vocal (a, e, i, o, u), mayúscula o minúscula."""
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        """Cuenta vocales, consonantes y dígitos en el texto, reutilizando solo_vocales."""
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = consonantes = digitos = 0
        for caracter in texto:
            if caracter.isdigit():
                digitos += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):   # se reutiliza
                    vocales += 1
                else:
                    consonantes += 1
        return {"vocales": vocales, "consonantes": consonantes, "digitos": digitos}


# --- Programa principal / prueba ---
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))   # {'vocales': 2, 'consonantes': 2, 'digitos': 3}

# OTRO EJERCICIO

#Analizador de contraseñas
# Clase AnalizadorClave que: (1) tenga método es_simbolo(caracter)
# que retorne True si no es letra, ni dígito, ni espacio; (2) tenga método contar_por_tipo(texto)
# que retorne un diccionario {'mayusculas': cant, 'minusculas': cant, 'digitos': cant, 'simbolos': cant}
# reutilizando métodos; (3) tenga atributo que lleve la cuenta de cuántos textos se han analizado.
#Entrada
# textos (contraseñas) para analizar
#Proceso
# recorrer carácter a carácter, clasificar
#Salida
# diccionario con conteos
#Ejemplo de entrada
# ac = AnalizadorClave()
# ac.contar_por_tipo("Hola#2026")
#Salida esperada
# {'mayusculas': 1, 'minusculas': 3, 'digitos': 4, 'simbolos': 1}
#Colecciones: diccionario para contar tipos
class AnalizadorClave:
    def __init__(self):
        self.total_analizados = 0  # atributo: cantidad de textos analizados

    def es_simbolo(self, caracter):
        """Retorna True si el carácter no es letra, dígito ni espacio."""
        return not caracter.isalnum() and not caracter.isspace()

    def contar_por_tipo(self, texto):
        """Cuenta mayúsculas, minúsculas, dígitos y símbolos, reutilizando es_simbolo."""
        self.total_analizados += 1
        conteo = {"mayusculas": 0, "minusculas": 0, "digitos": 0, "simbolos": 0}
        for caracter in texto:
            if caracter.isdigit():
                conteo["digitos"] += 1
            elif caracter.isupper():
                conteo["mayusculas"] += 1
            elif caracter.islower():
                conteo["minusculas"] += 1
            elif self.es_simbolo(caracter):   # reutiliza el método base
                conteo["simbolos"] += 1
        return conteo

