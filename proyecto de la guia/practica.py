"""Ejercicios de colecciones (sección 13 de la guía)."""

# ---------- Ejercicio 1 · Quitar duplicados conservando el orden ----------
ciudades = ["Quito", "Guayaquil", "Quito", "Cuenca", "Guayaquil"]

vistas = set()      # CONJUNTO de control: pregunta rápida "¿ya apareció?"
unicas = []         # LISTA de resultado: conserva el orden
for ciudad in ciudades:
    if ciudad not in vistas:
        vistas.add(ciudad)
        unicas.append(ciudad)
print("Ejercicio 1:", unicas)

# ---------- Ejercicio 2 · Contar con un diccionario ----------
conteo = {}
for ciudad in ciudades:
    conteo[ciudad] = conteo.get(ciudad, 0) + 1     # .get evita el KeyError la primera vez
mas_repetida = max(conteo, key=conteo.get)
print("Ejercicio 2:", conteo, "| más repetida:", mas_repetida)

# ---------- Ejercicio 3 · Conjuntos en acción ----------
inscritos_matematica = {"Ana", "Luis", "Sol", "Marco"}
inscritos_ingles = {"Luis", "Marco", "Ruth"}
ambas = inscritos_matematica & inscritos_ingles         # intersección
solo_mate = inscritos_matematica - inscritos_ingles     # diferencia
total = len(inscritos_matematica | inscritos_ingles)    # unión
print("Ejercicio 3:", sorted(ambas), sorted(solo_mate), total)

# ---------- Ejercicio 4 · De lista de diccionarios a índice ----------
clientes = [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}]
indice = {cliente["id"]: cliente for cliente in clientes}
print("Ejercicio 4:", indice[2]["nombre"])   # una sola operación, sin recorrer la lista

# ---------- Ejercicio 5 · Tuplas como registros inmutables ----------
ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)]
total_ventas = sum(monto for _mes, monto in ventas)
mejor_mes, mejor_monto = max(ventas, key=lambda venta: venta[1])
print(f"Ejercicio 5: total {total_ventas} | mejor mes: {mejor_mes} con {mejor_monto}")
for mes, monto in ventas:                    # desempaquetado en el for
    print(f"   {mes:<10} {monto}")

# El ejercicio 6 (clientes_por_ciudad) está dentro de proyecto_clientes/views.py, opción 8 del menú.
