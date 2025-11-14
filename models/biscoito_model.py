import random
from dados import FRASES


class BiscoitoModel:
    def __init__(self):
        self._historico = []
        self._frase_anterior = ""
        self._frases = FRASES


    
    def obter_frase(self) -> str:
        frase_escolhida = None
        tentativas = 0
        MAX_TENTATIVAS = 3

        while tentativas < MAX_TENTATIVAS:
            frase_candidata = random.choice(self._frases)
            
            if frase_candidata != self._frase_anterior:
                frase_escolhida = frase_candidata
                break

            tentativas += 1

        if frase_escolhida is None: 
            frase_escolhida = random.choice(self._frases) 

        self._frase_anterior = frase_escolhida 
        self._historico.append(frase_escolhida)

        return frase_escolhida



    def resetar_historico(self) -> None:
        self._historico = []
        self._frase_anterior = ""



    def get_total_frases(self) -> int:
        return len(self._historico)