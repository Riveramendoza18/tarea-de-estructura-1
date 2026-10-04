"""
MODELO (Model)
Define QUÉ es un estudiante. No lee archivos, no pide datos, no imprime.
"""
import json

# TUPLA de campos editables: el orden y los nombres son fijos, nadie debe
# modificarlos en tiempo de ejecución. La usan el Controlador y la Vista.
CAMPOS_ESTUDIANTE = ("nombre", "apellido", "email", "carnet")


class Estudiante:
    """MODELO: representa a un estudiante. Usa las cuatro colecciones."""

    def __init__(self, id_estudiante, nombre, apellido, email, carnet, notas=None, materias=None):
        self.id = id_estudiante          # no usamos 'id' como parámetro: es una función de Python
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet             # ej: EST2026001
        # DICCIONARIO DE LISTAS: {"Matemática": [18, 19], "Inglés": [17]}
        # dict porque cada materia (clave) tiene su propia lista de notas (valor).
        self.notas = notas if notas else {}
        # CONJUNTO: materias inscritas. set porque una materia no puede repetirse.
        self.materias = set(materias) if materias else set()

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def inscribir_materia(self, materia):
        # add() no duplica: si ya estaba inscrito, no pasa nada
        self.materias.add(materia)

    def agregar_nota(self, materia, nota):
        self.inscribir_materia(materia)
        # setdefault crea la LISTA vacía la primera vez que aparece la materia
        self.notas.setdefault(materia, []).append(nota)

    def obtener_promedio(self):
        # LISTA acumuladora con todas las notas de todas las materias
        todas = []
        for lista_notas in self.notas.values():
            todas.extend(lista_notas)
        if not todas:
            return 0
        return round(sum(todas) / len(todas), 2)

    def promedio_por_materia(self):
        # Comprensión de DICCIONARIO: {materia: promedio}
        return {
            materia: round(sum(lista) / len(lista), 2)
            for materia, lista in self.notas.items() if lista
        }

    def materias_en_comun(self, otro_estudiante):
        # INTERSECCIÓN de conjuntos: qué materias comparten dos estudiantes
        return self.materias & otro_estudiante.materias

    def a_diccionario(self):
        # Objeto -> diccionario (listo para JSON)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "carnet": self.carnet,
            "notas": self.notas,
            # JSON no sabe guardar un set: lo convertimos a lista ordenada
            "materias": sorted(self.materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        # Diccionario -> objeto. Se usa así: Estudiante.desde_diccionario({...})
        return cls(
            datos["id"], datos["nombre"], datos["apellido"], datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),
            # al leer, la lista del JSON vuelve a ser un set
            materias=set(datos.get("materias", [])),
        )

    def a_json(self):
        return json.dumps(self.a_diccionario(), ensure_ascii=False)

    def __str__(self):
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {self.obtener_promedio()}"
