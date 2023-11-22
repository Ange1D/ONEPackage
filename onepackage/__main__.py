import logging
from onepackage import cifrar, descifrar

if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    
    logging.debug(cifrar("gato"))

    logging.debug('>>> Estamos finalizando la ejecución del paquete.')