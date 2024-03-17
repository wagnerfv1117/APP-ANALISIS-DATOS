#importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

#título de la app
st.title('Visualización de Serie de Tiempo Termohigrometros')

#cargar datos desde .CSV  
archivo = st.file_uploader("Cargar archivo CSV", type=['csv'])
if archivo is not None:
    datos = pd.read_csv(archivo)#se crear un condicional

    #mostrar datos como tabla
    st.write('**Datos de Temperatura:**')
    st.write(datos)

    #grafica serie de tiempo 
    st.write('**Análisis de la temperatura:**')
    fig = px.line(datos, x='Fecha', y='Temperatura', title='Serie de Tiempo de Temperatura')
    st.plotly_chart(fig)
else:
    st.write('Por favor, subir un archivo CSV para empezar.')
