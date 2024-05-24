from flask import Flask

from data import filosofos, html_code
from selectorss import img, first
import socket

docker_short_id = socket.gethostname()


app = Flask(__name__)


@app.route("/")
def filosofo():
    filosofo = first(filosofos)
    return filosofo


@app.route("/a")
def second():
    filosofo = img(filosofos, docker_short_id)
    return (
        html_code.replace("IMAGE_PATH", filosofo["Imagen"])
        .replace("PHRASE_FILOSOFICA", filosofo["Frase filosófica"])
        .replace("NAME", filosofo["Nombre"])
        .replace("CONTAINER_ID", filosofo["container_id"])
    )
