# ejercicio2.py

# Lista que almacenará todas las actividades
actividades = []

def agregar_actividad(nombre, tipo, presupuesto, gasto_real):
    # Calcular diferencia y estado
    diferencia = presupuesto - gasto_real
    if gasto_real <= presupuesto:
        estado = "Dentro del presupuesto"
    else:
        estado = "Excede el presupuesto"

    actividad = {
        "nombre": nombre,
        "tipo": tipo,
        "presupuesto": presupuesto,
        "gasto_real": gasto_real,
        "diferencia": diferencia,
        "estado": estado
    }
    actividades.append(actividad)

def obtener_actividades():
    return actividades
