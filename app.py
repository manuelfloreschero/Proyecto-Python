import streamlit as st
from ejercicio1 import ejecutar_ejercicio1
from ejercicio2 import agregar_actividad, obtener_actividades
from ejercicio3 import calcular_retornos
from ejercicio4 import Actividad


# Crear menú lateral
opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["INICIO", "EJERCICIO1", "EJERCICIO2", "EJERCICIO3", "EJERCICIO4"]
)

# Mostrar contenido según la opción elegida
if opcion == "INICIO":
    st.header("**PROYECTO:** Proyecto Aplicado en Streamlit")
    st.write("**Nombre de Alumno:** Flores Chero Luiguin Manuel")
    st.write("**Curso:** Modulo 1: Python Fundamentals")
    st.write("**Año:** 2026")
    st.write("**Objetivos del Proyecto:** ")
    st.write("""
    - Aplicar conceptos básicos de programación en Python (condicionales, listas, funciones, POO).
    - Usar Streamlit para crear una interfaz interactiva.
    - Desarrollar habilidades prácticas en programación funcional y orientada a objetos.
    """)
    st.write("**Tecnologías:** ")
    st.write("""
    - **Python**: lenguaje de programación principal.
    - **Streamlit**: para la interfaz gráfica interactiva.
    """)


elif opcion == "EJERCICIO1":
    st.title("Bienvenido al Ejercicio °1")
    st.write("Aquí puedes validar si tu gasto se ajusta o no a tu presupuesto.")
    st.header("Validador de Presupuesto vs Gasto")

    presupuesto = st.number_input("Ingresa tu presupuesto:", min_value=0.0, step=100.0)
    gasto = st.number_input("Ingresa tu gasto:", min_value=0.0, step=50.0)

    if st.button("Validar"):
        mensaje, detalle = ejecutar_ejercicio1(presupuesto, gasto)

        # Mostrar resultados
        if gasto <= presupuesto:
            st.success(mensaje)
        else:
            st.warning(mensaje)

        st.write(detalle)

elif opcion == "EJERCICIO2":
    st.title("Bienvenido al Ejercicio °2")
    st.write("Aquí validaremos si actividades financieras cumplen con sus requisitos")
    st.header("Ejercicio 2: Actividades Financieras")

    # Inputs para nueva actividad
    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Ingreso", "Gasto"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=100.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0, step=50.0)

    if st.button("Agregar actividad"):
        agregar_actividad(nombre, tipo, presupuesto, gasto_real)
        st.success("Actividad agregada correctamente.")

    # Mostrar actividades registradas en formato tabla
    st.subheader("Lista de actividades")
    actividades = obtener_actividades()
    if actividades:
        st.dataframe(actividades)  # Mostrar como tabla
    else:
        st.write("No hay actividades registradas aún.")


elif opcion == "EJERCICIO3":
    st.title("Bienvenido al Ejercicio °3")
    st.write("Aquí calcularemos el retorno de un presupuesto")
    st.title("Retorno Esperado")

    # Lista para almacenar actividades ingresadas
    if "actividades" not in st.session_state:
        st.session_state["actividades"] = []

    # Inputs para nueva actividad
    nombre = st.text_input("Nombre de la actividad")
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=100.0)
    tasa = st.number_input("Tasa (ejemplo: 0.05 para 5%)", min_value=0.0, step=0.01)
    meses = st.number_input("Meses", min_value=1, step=1)

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "presupuesto": presupuesto,
            "tasa": tasa,
            "meses": meses
        }
        st.session_state["actividades"].append(actividad)
        st.success("Actividad agregada correctamente.")

    # Calcular retornos
    if st.button("Calcular retornos"):
        resultados = calcular_retornos(st.session_state["actividades"])
        st.subheader("Resultados con retorno esperado")
        st.dataframe(resultados)  # Mostrar como tabla interactiva


elif opcion == "EJERCICIO4":
    st.title("Ejercicio °4")
    st.write("Aquí validaremos un presupuesto aplicando POO")
    st.header("Clase Actividad Financiera")

    # Inputs para crear una actividad
    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Ingreso", "Gasto"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0, step=100.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0, step=50.0)

    if st.button("Crear actividad"):
        actividad = Actividad(nombre, tipo, presupuesto, gasto_real)
        info = actividad.mostrar_info()

        # Retroalimentación visual según el estado
        if actividad.esta_en_presupuesto():
            st.success(f"La actividad '{actividad.nombre}' está dentro del presupuesto.")
        else:
            st.warning(f"La actividad '{actividad.nombre}' excede el presupuesto.")

        # Mostrar resumen en tabla
        st.subheader("Resumen de la actividad")
        st.dataframe([info])  # Convertimos el dict en lista para mostrarlo como tabla


























