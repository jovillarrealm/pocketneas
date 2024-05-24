from random import choice

def first(filosofos):
    filosofo = dict(choice(filosofos))
    del filosofo["Imagen"]
    del filosofo["Frase filosófica"]
    return filosofo

def img(filosofos, docker_short_id):
    filosofo = dict(choice(filosofos))
    wanted_keys = set(['Frase filosófica', 'Imagen', "Nombre"])
    filosofo = {k: filosofo[k] for k in filosofo.keys() & wanted_keys}
    filosofo["container_id"] = docker_short_id
    return filosofo