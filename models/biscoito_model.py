import random
from dados import FRASES


class BiscoitoModel:
    def __init__(self):
        self._historico = []
        self._frase_anterior = ""
        self._frases = FRASES