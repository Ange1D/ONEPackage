import re

def validarMensaje(message):
    caracteresValidos = re.compile('[a-zñ ]')
    return (message != "" and len(message) > 0 and caracteresValidos.search(message) is not None)
