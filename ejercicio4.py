# ejercicio4.py

class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    def esta_en_presupuesto(self):
        """Verifica si el gasto real está dentro del presupuesto"""
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self):
        """Devuelve un resumen de la actividad"""
        estado = "Dentro del presupuesto" if self.esta_en_presupuesto() else "Excede el presupuesto"
        return {
            "Nombre": self.nombre,
            "Tipo": self.tipo,
            "Presupuesto": self.presupuesto,
            "Gasto Real": self.gasto_real,
            "Estado": estado
        }
