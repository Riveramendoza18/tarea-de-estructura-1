"""
CONTROLADOR
Aquí viven las reglas: validar, buscar, decidir y guardar.
Regla de oro: este archivo nunca imprime en pantalla ni pide datos al usuario.
Toda función devuelve datos o una TUPLA (exito, mensaje/resultado).
"""
from models import Estudiante, CAMPOS_ESTUDIANTE
from shared.json_manager import GestorJSON
from shared.herramientas import es_email_valido

gestor = GestorJSON("data/estudiantes.json")

# TUPLAS de configuración: valores fijos, nadie los modifica en ejecución
CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")
NOTA_MINIMA, NOTA_MAXIMA = 0, 20          # desempaquetado de una tupla


# ===================== AYUDAS INTERNAS =====================

def emails_registrados(excepto_id=None):
    """CONJUNTO con los emails ya usados: detectar duplicados es instantáneo."""
    return {
        registro["email"].lower()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def carnets_registrados(excepto_id=None):
    """CONJUNTO con los carnets ya usados. Igual que con el email."""
    return {
        registro["carnet"].upper()
        for registro in gestor.leer()
        if registro["id"] != excepto_id
    }


def siguiente_id():
    # LISTA de ids; caso explícito para cuando todavía no hay registros
    ids = [registro["id"] for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1


def buscar_posicion(registros, id_estudiante):
    """Devuelve el índice del registro en la LISTA, o None si no existe."""
    for indice, registro in enumerate(registros):     # enumerate: índice y valor
        if registro["id"] == id_estudiante:
            return indice
    return None


def normalizar(datos):
    """DICCIONARIO limpio: sin espacios, email en minúsculas, carnet en mayúsculas."""
    valores = {campo: str(valor).strip() for campo, valor in datos.items()}
    if "email" in valores:
        valores["email"] = valores["email"].lower()
    if "carnet" in valores:
        valores["carnet"] = valores["carnet"].upper()
    return valores


# ===================== C · CREATE =====================

def crear_estudiante(datos):
    """datos: diccionario con las claves de CAMPOS_ESTUDIANTE. Devuelve (exito, mensaje)."""
    try:
        # 1) Normalizo: un diccionario con todos los campos
        valores = normalizar({campo: datos.get(campo, "") for campo in CAMPOS_ESTUDIANTE})

        # 2) Obligatorios: recorro la TUPLA y armo una LISTA de faltantes
        faltantes = [campo for campo in CAMPOS_OBLIGATORIOS if not valores[campo]]
        if faltantes:
            return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

        # 3) Formato del email
        if not es_email_valido(valores["email"]):
            return False, f"El email '{valores['email']}' no tiene un formato válido"

        # 4) Duplicados: búsqueda instantánea dentro de los CONJUNTOS
        if valores["carnet"] in carnets_registrados():
            return False, f"El carnet {valores['carnet']} ya está registrado"
        if valores["email"] in emails_registrados():
            return False, "Ese email ya está registrado"

        # 5) Creo el objeto del Modelo. ** convierte el diccionario en argumentos
        estudiante = Estudiante(siguiente_id(), **valores)

        # 6) Agrego a la LISTA y guardo
        registros = gestor.leer()
        registros.append(estudiante.a_diccionario())
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"

        return True, f"Estudiante {estudiante.obtener_nombre_completo()} creado con id {estudiante.id}"

    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== R · READ =====================

def obtener_todos():
    """LISTA de objetos Estudiante."""
    return [Estudiante.desde_diccionario(registro) for registro in gestor.leer()]


def obtener_por_id(id_estudiante):
    for estudiante in obtener_todos():
        if estudiante.id == id_estudiante:
            return estudiante
    return None


# ===================== S · SEARCH =====================

def buscar_estudiantes(termino):
    """Búsqueda lineal: revisa registro por registro los campos buscables y las materias."""
    termino = termino.strip().lower()
    if not termino:
        return []

    encontrados = []
    for registro in gestor.leer():
        # TUPLA de campos + LISTA de materias: busco en todos los textos del registro
        textos = [str(registro.get(campo, "")) for campo in CAMPOS_BUSCABLES]
        textos.extend(registro.get("materias", []))
        if any(termino in texto.lower() for texto in textos):
            encontrados.append(Estudiante.desde_diccionario(registro))
    return encontrados


# ===================== U · UPDATE =====================

def actualizar_estudiante(id_estudiante, cambios):
    """cambios: diccionario solo con los campos que se quieren modificar."""
    try:
        if not cambios:
            return False, "No se indicó ningún cambio"

        # DIFERENCIA DE CONJUNTOS: ¿mandaron algún campo que no existe?
        desconocidos = set(cambios) - set(CAMPOS_ESTUDIANTE)
        if desconocidos:
            return False, f"Campos no válidos: {', '.join(sorted(desconocidos))}"

        cambios = normalizar(cambios)
        vacios = [campo for campo, valor in cambios.items() if not valor]
        if vacios:
            return False, f"Estos campos no pueden quedar vacíos: {', '.join(vacios)}"

        if "email" in cambios:
            if not es_email_valido(cambios["email"]):
                return False, "El email no tiene un formato válido"
            if cambios["email"] in emails_registrados(excepto_id=id_estudiante):
                return False, "Ese email ya lo usa otro estudiante"

        if "carnet" in cambios and cambios["carnet"] in carnets_registrados(excepto_id=id_estudiante):
            return False, f"El carnet {cambios['carnet']} ya lo usa otro estudiante"

        registros = gestor.leer()
        posicion = buscar_posicion(registros, id_estudiante)
        if posicion is None:
            return False, f"No existe un estudiante con id {id_estudiante}"

        registros[posicion].update(cambios)        # actualizo el diccionario en su lugar
        if not gestor.guardar(registros):
            return False, "No se pudo escribir el archivo"
        return True, f"Estudiante {id_estudiante} actualizado ({len(cambios)} campo/s)"

    except Exception as error:
        return False, f"Error inesperado: {error}"


# ===================== D · DELETE =====================

def eliminar_estudiante(id_estudiante):
    registros = gestor.leer()
    # LISTA NUEVA sin ese registro: nunca borro mientras recorro
    quedan = [registro for registro in registros if registro["id"] != id_estudiante]

    if len(quedan) == len(registros):
        return False, f"No existe un estudiante con id {id_estudiante}"

    if not gestor.guardar(quedan):
        return False, "No se pudo escribir el archivo"
    return True, f"Estudiante {id_estudiante} eliminado"


# ===================== NOTAS Y MATERIAS =====================

def agregar_nota(id_estudiante, materia, nota):
    """Registra una nota entre 0 y 20. Devuelve (exito, mensaje)."""
    materia = str(materia).strip().title()
    if not materia:
        return False, "La materia es obligatoria"

    try:
        nota = float(str(nota).replace(",", "."))
    except ValueError:
        return False, f"La nota '{nota}' no es un número"

    if not NOTA_MINIMA <= nota <= NOTA_MAXIMA:
        return False, f"La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}"

    # 18.0 se guarda como 18 para que el JSON quede limpio
    nota = int(nota) if nota.is_integer() else round(nota, 2)

    registros = gestor.leer()
    posicion = buscar_posicion(registros, id_estudiante)
    if posicion is None:
        return False, f"No existe un estudiante con id {id_estudiante}"

    # Uso el Modelo para que la regla de inscribir + agregar nota esté en un solo lugar
    estudiante = Estudiante.desde_diccionario(registros[posicion])
    estudiante.agregar_nota(materia, nota)
    registros[posicion] = estudiante.a_diccionario()

    if not gestor.guardar(registros):
        return False, "No se pudo escribir el archivo"
    return True, f"Nota {nota} registrada en {materia} para {estudiante.obtener_nombre_completo()}"


def ver_promedio(id_estudiante):
    """Devuelve (exito, resultado). resultado es un DICCIONARIO con el detalle o un mensaje."""
    estudiante = obtener_por_id(id_estudiante)
    if not estudiante:
        return False, f"No existe un estudiante con id {id_estudiante}"
    return True, {
        "estudiante": estudiante.obtener_nombre_completo(),
        "carnet": estudiante.carnet,
        "por_materia": estudiante.promedio_por_materia(),
        "notas": estudiante.notas,
        "general": estudiante.obtener_promedio(),
    }


def materias_ofertadas():
    """CONJUNTO con todas las materias inscritas por todos los estudiantes, sin repetir."""
    todas = set()
    for estudiante in obtener_todos():
        todas |= estudiante.materias          # UNIÓN de conjuntos
    return todas


def estudiantes_en_comun(id_a, id_b):
    """Materias que comparten dos estudiantes (INTERSECCIÓN). Devuelve (exito, resultado)."""
    if id_a == id_b:
        return False, "Debe elegir dos estudiantes distintos"

    estudiante_a = obtener_por_id(id_a)
    estudiante_b = obtener_por_id(id_b)
    if not estudiante_a:
        return False, f"No existe un estudiante con id {id_a}"
    if not estudiante_b:
        return False, f"No existe un estudiante con id {id_b}"

    return True, {
        "a": estudiante_a.obtener_nombre_completo(),
        "b": estudiante_b.obtener_nombre_completo(),
        "comunes": estudiante_a.materias_en_comun(estudiante_b),
    }


# ===================== EXTRA: estadísticas =====================

def estadisticas():
    """DICCIONARIO de resumen."""
    estudiantes = obtener_todos()
    con_notas = [e for e in estudiantes if e.notas]
    mejor = max(con_notas, key=lambda e: e.obtener_promedio()) if con_notas else None

    return {
        "total": len(estudiantes),
        "materias": sorted(materias_ofertadas()),
        "sin_notas": [e.obtener_nombre_completo() for e in estudiantes if not e.notas],
        "mejor": str(mejor) if mejor else "Sin datos",
    }
