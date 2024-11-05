import streamlit as st
import random

# Título de la aplicación
st.title("🎉 Aplicación de Sorteo 🎉")
st.markdown("Bienvenido a la aplicación de sorteo. Ingresa los nombres y selecciona al ganador.")

# Ingreso de nombres
nombres = st.text_area("📝 Ingresa los nombres (uno por línea):", height=150)
nombres_lista = [nombre.strip() for nombre in nombres.splitlines() if nombre.strip()]

# Eliminar nombres duplicados
nombres_unicos = list(set(nombres_lista))

# Solo establecer max_value si hay nombres únicos
if len(nombres_unicos) > 0:
    num_ganadores = st.number_input("👥 Selecciona el número de ganadores:", 
                                    min_value=1,
                                    max_value=len(nombres_unicos),
                                    value=1)
else:
    num_ganadores = 1  # Valor por defecto si no hay nombres

# Botón para realizar el sorteo
if st.button("🎲 Realizar Sorteo", key="sorteo_button"):
    if len(nombres_unicos) > 0:
        ganadores = random.sample(nombres_unicos, num_ganadores)
        st.success(f"🏆 Los ganadores son: {', '.join(ganadores)}")
    else:
        st.error("⚠️ Por favor ingresa al menos un nombre.")

# Mostrar la lista de nombres únicos de forma clara
st.subheader("📋 Nombres ingresados sin duplicados:")
if nombres_unicos:
    st.write("Lista de nombres únicos:")
    for i, nombre in enumerate(sorted(nombres_unicos)):
        st.write(f"{i+1}. {nombre}")
else:
    st.write("No se han ingresado nombres.")