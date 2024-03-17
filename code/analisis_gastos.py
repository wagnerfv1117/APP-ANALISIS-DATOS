import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Analisis de gastos mensuales en casa')# titulo de la app

archivo = st.file_uploader("Cargar archivo CSV", type=['csv'])

#definir condicional para la ubiación de la tabla de datos y graficas
if archivo is not None:
    datos = pd.read_csv(archivo)

    #st.write('**Análisis de los gastos ejecutados:**') # por si se desea colocar texto en la parte superior de la app
    # División del espacio para colocar gráficas arriba y tabla de datos abajo
    
    col1, col2 = st.columns(2)
    
    #grafica de torta a la izquierda de la aplicación
    with col1:
        
        fig_pie = px.pie(datos, names='fecha', title='Distribución de gastos analizando la fecha')
        st.plotly_chart(fig_pie, use_container_width=True)

    
    #grafica de torta a la derecha de la aplicación
    with col2:
        
        fig_line = px.line(datos, x='fecha', y='monto', title='Gastos en mercado')
        st.plotly_chart(fig_line, use_container_width=True)
    
    
    st.write('**Tabla con los datos cargados:**')
    st.write(datos)
else:
    st.write('Por favor subir un archivo .CSV para visualizar')


st.write('**Desarrollado por: Wagner Fernández V.**')