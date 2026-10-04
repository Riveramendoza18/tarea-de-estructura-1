"""
VISTA (View)
Solo muestra el menú, pide datos con input() y muestra resultados con print().
No abre el JSON, no calcula promedios, no valida reglas del negocio.
"""
from models import CAMPOS_ESTUDIANTE
from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info, confirmar
)
from views import (
    crear_estudiante, obtener_todos, obtener_por_id, buscar_estudiantes,
    actualizar_estudiante, eliminar_estudiante, agregar_nota, ver_promedio,
    materias_ofertadas, estudiantes_en_comun, estadisticas
)


def pausa():
    input("\nPresione Enter para continuar...")


def mostrar_resultado(exito, mensaje):
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)


def pedir_id(texto="Id del estudiante: "):
    """Devuelve el id como entero, o None si el usuario no escribió un número."""
    try:
        return int(input(texto))
    except ValueError:
        imprimir_error("El id debe ser un número entero")
        return None


def mostrar_tabla(estudiantes):
    print(f"{'ID':<5}{'CARNET':<13}{'NOMBRE':<25}{'EMAIL':<28}{'MATERIAS':<10}{'PROMEDIO':<8}")
    print("-" * 89)
    for e in estudiantes:
        print(f"{e.id:<5}{e.carnet:<13}{e.obtener_nombre_completo():<25}"
              f"{e.email:<28}{len(e.materias):<10}{e.obtener_promedio():<8}")
    print("-" * 89)
    imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")


# ---------- C · CREAR ----------
def opcion_crear():
    imprimir_titulo("CREAR NUEVO ESTUDIANTE")
    # Recorro la TUPLA de campos: si mañana agrego un campo al Modelo,
    # este formulario se actualiza solo.
    datos = {}
    for campo in CAMPOS_ESTUDIANTE:
        datos[campo] = input(f"{campo.capitalize()}: ")

    exito, mensaje = crear_estudiante(datos)       # desempaqueto la TUPLA
    mostrar_resultado(exito, mensaje)
    pausa()


# ---------- R · LEER TODOS ----------
def opcion_ver_todos():
    imprimir_titulo("LISTA DE ESTUDIANTES")
    estudiantes = obtener_todos()
    if not estudiantes:
        imprimir_info("Todavía no hay estudiantes. Use la opción 1 para crear el primero.")
    else:
        mostrar_tabla(estudiantes)
    pausa()


# ---------- S · BUSCAR ----------
def opcion_buscar():
    imprimir_titulo("BUSCAR ESTUDIANTE")
    termino = input("Nombre, apellido, email, carnet o materia: ")
    encontrados = buscar_estudiantes(termino)

    if not encontrados:
        imprimir_info(f"Ningún estudiante coincide con '{termino}'.")
    else:
        mostrar_tabla(encontrados)
    pausa()


# ---------- R · LEER UNO ----------
def opcion_ver_por_id():
    imprimir_titulo("VER ESTUDIANTE POR ID")
    id_estudiante = pedir_id()
    if id_estudiante is None:
        return pausa()

    estudiante = obtener_por_id(id_estudiante)
    if not estudiante:
        imprimir_error(f"No existe un estudiante con id {id_estudiante}")
    else:
        # Recorro el DICCIONARIO del estudiante: clave y valor a la vez
        for clave, valor in estudiante.a_diccionario().items():
            if clave == "materias":
                valor = ", ".join(valor) or "ninguna"
            elif clave == "notas":
                valor = "; ".join(f"{m}: {n}" for m, n in valor.items()) or "sin notas"
            print(f"  {clave.capitalize():<12}: {valor}")
    pausa()


# ---------- U · ACTUALIZAR ----------
def opcion_actualizar():
    imprimir_titulo("ACTUALIZAR ESTUDIANTE")
    id_estudiante = pedir_id()
    if id_estudiante is None:
        return pausa()

    estudiante = obtener_por_id(id_estudiante)
    if not estudiante:
        imprimir_error(f"No existe un estudiante con id {id_estudiante}")
        return pausa()

    imprimir_info(f"Editando a {estudiante.obtener_nombre_completo()}")
    print("Deje en blanco el campo que no quiera cambiar.\n")

    # DICCIONARIO solo con lo que el usuario escribió
    cambios = {}
    for campo in CAMPOS_ESTUDIANTE:
        actual = getattr(estudiante, campo)
        nuevo = input(f"{campo.capitalize()} [{actual}]: ").strip()
        if nuevo:
            cambios[campo] = nuevo

    mostrar_resultado(*actualizar_estudiante(id_estudiante, cambios))
    pausa()


# ---------- D · ELIMINAR ----------
def opcion_eliminar():
    imprimir_titulo("ELIMINAR ESTUDIANTE")
    id_estudiante = pedir_id()
    if id_estudiante is None:
        return pausa()

    estudiante = obtener_por_id(id_estudiante)
    if not estudiante:
        imprimir_error(f"No existe un estudiante con id {id_estudiante}")
        return pausa()

    imprimir_info(f"Se eliminará: {estudiante}")
    if confirmar("¿Confirma la eliminación?"):
        mostrar_resultado(*eliminar_estudiante(id_estudiante))
    else:
        imprimir_info("Operación cancelada")
    pausa()


# ---------- AGREGAR NOTA ----------
def opcion_agregar_nota():
    imprimir_titulo("AGREGAR NOTA")
    id_estudiante = pedir_id()
    if id_estudiante is None:
        return pausa()

    ofertadas = materias_ofertadas()
    if ofertadas:
        imprimir_info(f"Materias existentes: {', '.join(sorted(ofertadas))}")

    materia = input("Materia: ")
    nota = input("Nota (0 a 20): ")
    mostrar_resultado(*agregar_nota(id_estudiante, materia, nota))
    pausa()


# ---------- VER PROMEDIO ----------
def opcion_ver_promedio():
    imprimir_titulo("VER PROMEDIO")
    id_estudiante = pedir_id()
    if id_estudiante is None:
        return pausa()

    exito, resultado = ver_promedio(id_estudiante)
    if not exito:
        imprimir_error(resultado)
        return pausa()

    imprimir_info(f"{resultado['estudiante']} ({resultado['carnet']})")
    if not resultado["por_materia"]:
        imprimir_info("Todavía no tiene notas registradas.")
    else:
        print(f"\n  {'MATERIA':<18}{'NOTAS':<22}{'PROMEDIO'}")
        print("  " + "-" * 48)
        for materia, promedio in resultado["por_materia"].items():
            notas = ", ".join(str(n) for n in resultado["notas"][materia])
            print(f"  {materia:<18}{notas:<22}{promedio}")
        print("  " + "-" * 48)
        imprimir_exito(f"Promedio general: {resultado['general']}")
    pausa()


# ---------- MATERIAS EN COMÚN ----------
def opcion_materias_comun():
    imprimir_titulo("MATERIAS EN COMÚN")
    id_a = pedir_id("Id del primer estudiante: ")
    if id_a is None:
        return pausa()
    id_b = pedir_id("Id del segundo estudiante: ")
    if id_b is None:
        return pausa()

    exito, resultado = estudiantes_en_comun(id_a, id_b)
    if not exito:
        imprimir_error(resultado)
    elif not resultado["comunes"]:
        imprimir_info(f"{resultado['a']} y {resultado['b']} no comparten materias.")
    else:
        imprimir_exito(f"{resultado['a']} y {resultado['b']} comparten "
                       f"{len(resultado['comunes'])} materia(s):")
        for materia in sorted(resultado["comunes"]):   # un set se ordena para mostrarlo
            print(f"  • {materia}")
    pausa()


# ---------- EXTRA · ESTADÍSTICAS ----------
def opcion_estadisticas():
    imprimir_titulo("ESTADÍSTICAS")
    datos = estadisticas()
    print(f"  Estudiantes registrados : {datos['total']}")
    print(f"  Materias ofertadas      : {len(datos['materias'])} -> {', '.join(datos['materias'])}")
    print(f"  Sin notas               : {len(datos['sin_notas'])}")
    print(f"  Mejor promedio          : {datos['mejor']}")
    pausa()


def salir():
    imprimir_info("¡Hasta luego! 👋")
    return "salir"


# DICCIONARIO de opciones: tecla -> TUPLA (texto del menú, función)
OPCIONES = {
    "1": ("Crear estudiante", opcion_crear),
    "2": ("Ver todos", opcion_ver_todos),
    "3": ("Buscar", opcion_buscar),
    "4": ("Ver por id", opcion_ver_por_id),
    "5": ("Actualizar", opcion_actualizar),
    "6": ("Eliminar", opcion_eliminar),
    "7": ("Agregar nota", opcion_agregar_nota),
    "8": ("Ver promedio", opcion_ver_promedio),
    "9": ("Materias en común", opcion_materias_comun),
    "10": ("Estadísticas", opcion_estadisticas),
    "0": ("Salir", salir),
}


def mostrar_menu():
    imprimir_titulo("SISTEMA DE GESTIÓN DE ESTUDIANTES")
    for tecla, (texto, _funcion) in OPCIONES.items():
        print(f"  {tecla:>2}. {texto}")
    print()


def main():
    while True:
        mostrar_menu()
        tecla = input("Seleccione una opción: ").strip()

        if tecla not in OPCIONES:          # búsqueda instantánea por clave
            imprimir_error("Opción no válida")
            pausa()
            continue

        _texto, funcion = OPCIONES[tecla]
        if funcion() == "salir":
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
