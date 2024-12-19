import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('concrete.csv')

# Configuración de la aplicación
st.set_page_config(page_title="Portafolio de Juan Diego Trujillo Sánchez", layout="wide")

# Título y presentación
st.title("Portafolio de Análisis de Datos - Juan Diego Trujillo Sánchez")
st.markdown("""
    **Ingeniero Civil - https://www.linkedin.com/in/juan-diego-trujillo-sanchez-92b08b19a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app**  
    Bienvenido a mi portafolio interactivo de análisis de datos. 
    En esta aplicación, exploramos diferentes relaciones en los datos de resistencia del concreto. 
    Selecciona un gráfico del menú desplegable para ver las visualizaciones.
""")

# Opciones de gráficos disponibles
graph_options = {
    "Relación entre Edad del Concreto y Resistencia": ("age", "strength", "Edad del Concreto (días)", "Resistencia (MPa)"),
    "Relación entre Cemento y Resistencia": ("cement", "strength", "Cemento (kg/m³)", "Resistencia (MPa)"),
    "Relación entre Agua y Resistencia": ("water", "strength", "Agua (kg/m³)", "Resistencia (MPa)"),
    "Relación entre Cemento y Agua": ("cement", "water", "Cemento (kg/m³)", "Agua (kg/m³)")
}

selected_graph = st.selectbox("Seleccione el gráfico a visualizar", list(graph_options.keys()))

# Crear gráficos según la selección del usuario
try:
    x_col, y_col, x_label, y_label = graph_options[selected_graph]
    fig, ax = plt.subplots()

    # Crear gráfico de barras según la relación seleccionada
    if selected_graph == "Relación entre Cemento y Agua":
        ax.bar(df[x_col], df[y_col], color="purple", label=f"{x_label} vs {y_label}")
    else:
        ax.bar(df[x_col], df[y_col], color="blue", label=f"{x_label} vs {y_label}")

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(selected_graph)
    ax.grid(True)
    ax.legend()

    # Mostrar gráfico en Streamlit
    st.pyplot(fig)

    # Resumen explicativo del gráfico
    if selected_graph == "Relación entre Edad del Concreto y Resistencia":
        st.write("""
            **Resumen Detallado**: Este gráfico muestra cómo la resistencia del concreto (en megapascales, MPa) varía con la edad del concreto (en días).
            En la mayoría de los casos, a medida que el concreto envejece, su resistencia aumenta debido a la hidratación continua del cemento. 
            Este proceso es crucial, ya que un concreto con mayor resistencia es más adecuado para soportar cargas estructurales. 
            Sin embargo, el aumento de la resistencia disminuye con el tiempo, alcanzando una estabilización después de cierto periodo.
        """)
    elif selected_graph == "Relación entre Cemento y Resistencia":
        st.write("""
            **Resumen Detallado**: Este gráfico muestra la relación entre la cantidad de cemento (en kg/m³) utilizada en la mezcla y la resistencia del concreto.
            Un mayor contenido de cemento generalmente mejora la resistencia del concreto, ya que el cemento es el principal agente aglutinante en la mezcla.
            Sin embargo, un exceso de cemento puede aumentar los costos y puede afectar negativamente la trabajabilidad de la mezcla. Es crucial encontrar el balance adecuado para optimizar la relación costo-beneficio.
        """)
    elif selected_graph == "Relación entre Agua y Resistencia":
        st.write("""
            **Resumen Detallado**: Este gráfico ilustra cómo la cantidad de agua (en kg/m³) afecta la resistencia del concreto. El agua es esencial para la reacción de hidratación, 
            pero un exceso de agua en la mezcla puede disminuir la resistencia del concreto, ya que provoca una mayor porosidad y menor densidad. 
            Por otro lado, una cantidad insuficiente de agua puede dificultar el proceso de hidratación, también afectando negativamente la resistencia.
        """)
    elif selected_graph == "Relación entre Cemento y Agua":
        st.write("""
            **Resumen Detallado**: Este gráfico muestra la relación entre el contenido de cemento y la cantidad de agua en la mezcla. 
            El balance correcto entre estos dos ingredientes es fundamental para obtener un concreto con buena resistencia y durabilidad. 
            Un exceso de agua o cemento en relación con el otro puede afectar negativamente las propiedades mecánicas del concreto, por lo que se deben ajustar según las necesidades específicas del proyecto.
        """)

except Exception as e:
    st.error(f"Se produjo un error al generar el gráfico: {e}")

# Mostrar tabla de datos en la aplicación
st.write("### Dataset Utilizado")
st.dataframe(df)

# Agregar resumen estadístico
st.write("### Resumen Estadístico")

try:
    # Crear gráfico de calor del resumen estadístico
    summary = df.describe()
    fig_summary, ax_summary = plt.subplots(figsize=(12, 8))
    sns.heatmap(summary.transpose(), annot=True, fmt=".2f", cmap="YlGnBu", cbar=True, linewidths=0.5, ax=ax_summary)
    ax_summary.set_title("Resumen Estadístico (Visualización Gráfica)")

    # Mostrar gráfico de resumen estadístico en Streamlit
    st.pyplot(fig_summary)

    # Resumen explicativo del gráfico de resumen estadístico
    st.write("""
        **Resumen Detallado del Resumen Estadístico**: Este gráfico de calor muestra un análisis estadístico de las principales variables del conjunto de datos. 
        Las métricas clave incluyen:
        - **Media**: El valor promedio de cada variable, útil para obtener una idea general del comportamiento de la variable.
        - **Desviación estándar**: Mide la dispersión de los datos alrededor de la media, indicando la variabilidad.
        - **Mínimo y Máximo**: Los valores más bajos y más altos observados, que ayudan a identificar el rango de variabilidad.
        - **Percentiles**: Los valores que dividen el conjunto de datos en intervalos, proporcionando información sobre la distribución.
        
        El gráfico de calor utiliza un mapa de colores (más oscuro indica valores más altos) para representar visualmente estas métricas. 
        Esto facilita la identificación de características clave de las variables, como la variabilidad de la cantidad de cemento y agua, o la resistencia promedio del concreto.
    """)

except Exception as e:
    st.error(f"Se produjo un error al generar el gráfico del resumen estadístico: {e}")