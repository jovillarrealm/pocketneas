from flask import Flask
from random import choice

import socket
docker_short_id = socket.gethostname()


app = Flask(__name__)


@app.route("/")
def filosofo():
    filosofo = dict(choice(filosofos))
    del filosofo["Imagen"]
    del filosofo["Frase filosófica"]
    return filosofo

@app.route("/")
def second():
    filosofo = dict(choice(filosofos))
    wanted_keys = set(['Frase filosófica', 'Imagen'])
    filosofo = {k: filosofo[k] for k in filosofo.keys() & wanted_keys}
    filosofo["container_id"] = docker_short_id
    return filosofo
    



filosofos = [
    {
        "Id": 1,
        "Nombre": "Sócrates",
        "Altura": 1.75,
        "Habilidad": "Mayéutica",
        "Imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/133.png",
        "Frase filosófica": "Solo sé que no sé nada."
    },
    {
        "Id": 2,
        "Nombre": "Platón",
        "Altura": 1.80,
        "Habilidad": "Teoría de las Ideas",
        "Imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/094.png",
        "Frase filosófica": "La mayor declaración de amor es la que no se hace; el hombre que siente mucho, habla poco."
    },
    {
        "Id": 3,
        "Nombre": "Aristóteles",
        "Altura": 1.78,
        "Habilidad": "Lógica",
        "Imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/004.png",
        "Frase filosófica": "La amistad es un alma que habita en dos cuerpos; un corazón que habita en dos almas."
    },
    {
        "Id": 4,
        "Nombre": "Immanuel Kant",
        "Altura": 1.65,
        "Habilidad": "Crítica de la Razón Pura",
        "Imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/931.png",
        "Frase filosófica": "El sabio puede cambiar de opinión. El necio, nunca."
    },
    {
        "Id": 5,
        "Nombre": "Friedrich Nietzsche",
        "Altura": 1.73,
        "Habilidad": "Perspectivismo",
        "Imagen": "https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/197.png",
        "Frase filosófica": "Dios ha muerto. Dios sigue muerto. Y nosotros lo hemos matado."
    },
    {
        "Id": 6,
        "Nombre": "Pitágoras",
        "Altura": 1.70,  # Altura estimada
        "Habilidad": "Teorema de Pitágoras, geometría",
        "Imagen": "https://www.shutterstock.com/es/search/pit%C3%A1goras",
        "Frase filosófica": "El número es la esencia de todas las cosas."
    },
    {
        "Id": 7,
        "Nombre": "Euclides",
        "Altura": 1.67,  # Altura estimada
        "Habilidad": "Geometría, axiomas",
        "Imagen": "https://www.gettyimages.es/fotos/euclides-matem%C3%A1tico",
        "Frase filosófica": "No hay camino real para la geometría."
    },
    {
        "Id": 8,
        "Nombre": "Arquímedes",
        "Altura": 1.75,  # Altura estimada
        "Habilidad": "Hidrostática, mecánica, inventos",
        "Imagen": "https://www.shutterstock.com/es/search/arqu%C3%ADmedes",
        "Frase filosófica": "Dadme un punto de apoyo y moveré la Tierra."
    },
    {
        "Id": 9,
        "Nombre": "Pierre de Fermat",
        "Altura": 1.65,  # Altura estimada
        "Habilidad": "Teoría de números, último teorema de Fermat",
        "Imagen": "https://www.gettyimages.com.mx/fotos/pierre-de-fermat",
        "Frase filosófica": "He encontrado una prueba maravillosa de este teorema, pero este margen es demasiado pequeño para contenerla."
    },
    {
        "Id": 10,
        "Nombre": "Carl Friedrich Gauss",
        "Altura": 1.80,
        "Habilidad": "Teoría de números, análisis matemático",
        "Imagen": "https://www.gettyimages.es/fotos/carl-friedrich-gauss",
        "Frase filosófica": "Las matemáticas son la reina de las ciencias - y el álgebra es su reina."
    },
    # Puedes agregar más matemáticos a la lista como este
]
