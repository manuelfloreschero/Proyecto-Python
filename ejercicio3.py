# ejercicio3.py

def calcular_retornos(actividades):
    # Usamos map + lambda para recorrer la lista y calcular el retorno
    retornos = list(map(lambda act: {
        "nombre": act["nombre"],
        "presupuesto": act["presupuesto"],
        "tasa": act["tasa"],
        "meses": act["meses"],
        "retorno": act["presupuesto"] * act["tasa"] * act["meses"]
    }, actividades))
    return retornos