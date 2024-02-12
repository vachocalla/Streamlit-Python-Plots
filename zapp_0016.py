import streamlit as st
import pyodbc

def conectar_bd():
    server = 'LAPTOP-A7F9UEK5\SQLEXPRESS'
    database = 'personal40'
    username = 'sa'
    password = 'sasa'
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn
    except Exception as e:
        st.error(f'Error al conectar a la base de datos: {e}')
        return None

def ejecutar_consulta(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        st.error(f'Error al ejecutar la consulta: {e}')
        return None

def main():
    st.title('Consulta a Base de Datos SQL Server')
    conn = conectar_bd()
    if conn:
        st.success('Conexión establecida correctamente.')
        query = 'select * from RH_PAIS'
        if st.button('Ejecutar'):
            if query:
                resultados = ejecutar_consulta(conn, query)
                if resultados:
                    st.write('Resultados:')
                    for resultado in resultados:
                        st.write(resultado)
                else:
                    st.warning('No se encontraron resultados para la consulta.')
            else:
                st.warning('Por favor, ingresa una consulta SQL.')
    else:
        st.error('No se pudo establecer conexión con la base de datos.')

if __name__ == '__main__':
    main()