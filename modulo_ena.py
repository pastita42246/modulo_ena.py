import streamlit as st

def mostrar_ena():
    st.subheader("Escala Numérica Análoga (ENA) - Dolor")
    
    # El slider para el dolor
    dolor = st.select_slider(
        "¿Cómo califica su nivel de dolor actual?",
        options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        value=0
    )

    # Lógica de colores según el nivel de dolor
    if dolor == 0:
        st.success(f"Nivel {dolor}: Sin dolor")
    elif 1 <= dolor <= 3:
        st.warning(f"Nivel {dolor}: Dolor Leve")
        st.markdown(":green[Color asociado: Verde/Amarillo]")
    elif 4 <= dolor <= 6:
        st.warning(f"Nivel {dolor}: Dolor Moderado")
        st.markdown(":orange[Color asociado: Naranja]")
    else:
        st.error(f"Nivel {dolor}: Dolor Severo")
        st.markdown(":red[Color asociado: Rojo]")

    return dolor
