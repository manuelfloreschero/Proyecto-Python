# ejercicio1.py

#Creamos variables y las condicionales
def ejecutar_ejercicio1(presupuesto, gasto):
    diferencia = presupuesto - gasto

    if gasto <= presupuesto:
        mensaje = f"El gasto ({gasto}) está dentro del presupuesto ({presupuesto})."
        detalle = f"Te sobra: {diferencia} unidades."
    else:
        mensaje = f"El gasto ({gasto}) excede el presupuesto ({presupuesto})."
        detalle = f"Te faltan: {-diferencia} unidades."

    return mensaje, detalle
