from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # URL del archivo .txt (sustituye esta por tu URL real)
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"<h3>Error al leer el archivo: {e}</h3>"

    # Procesar el contenido del archivo
    personas_filtradas = []
    lineas = response.text.strip().split('\n')

    for linea in lineas:
        partes = linea.split(',')
        if partes and partes[0][0] in {'3', '4', '5', '7'}:
            personas_filtradas.append(partes)

    # Construir la tabla HTML
    tabla = "<table border='1' cellpadding='5'><tr><th>ID</th><th>Nombre</th><th>Edad</th></tr>"
    for persona in personas_filtradas:
        tabla += f"<tr><td>{persona[0]}</td><td>{persona[1]}</td><td>{persona[2]}</td></tr>"
    tabla += "</table>"

    # Agregar la fecha y la tabla al HTML
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d %B %Y, %H:%M:%S")
    html = f"""
    <h2>¡Hola, Loja, cuna de artistas!</h2>
    <p><b>{fecha_formateada}</b></p>
    <h3>Personas con ID que inicia con 3, 4, 5 o 7:</h3>
    {tabla}
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
