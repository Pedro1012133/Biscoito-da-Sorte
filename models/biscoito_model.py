import random as r
import json
from datetime import datetime
import os
from dados import FRASES


ARQUIVO_HISTORICO = 'historico.json'
FORMATO_DATA_HORA = "%d/%m/%Y %H:%M:%S"


class BiscoitoModel:
    def __init__(self):
        self._historico = []
        self._frase_anterior = ""
        self._frases = FRASES
        self._total_aberturas = 0
        self._id_sequencial = 0
        self._carregar_historico()



    def _carregar_historico(self):
        if not os.path.exists(ARQUIVO_HISTORICO):
            return
        
        try:
            with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._historico = data.get('historico', [])
                self._total_aberturas = data.get('total_aberturas', 0)
                
                if self._historico:
                    self._id_sequencial = self._historico[-1]['id']
                
        except (IOError, json.JSONDecodeError):
            print(f"ERRO: Arquivo {ARQUIVO_HISTORICO} corrompido ou inacessível. Iniciando com histórico vazio.")
            self._historico = []
            self._total_aberturas = 0
            self._id_sequencial = 0



    def salvar_historico(self):
        try:
            dados_para_salvar = {
                "total_aberturas": self._total_aberturas,
                "historico": self._historico
            }
            with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
                json.dump(dados_para_salvar, f, indent=4)
        except IOError:
            print("ERRO: Falha ao salvar o histórico. Verifique permissões de arquivo.")



    def obter_frase(self) -> str:
        frase_escolhida = None
        tentativas = 0
        MAX_TENTATIVAS = 3

        while tentativas < MAX_TENTATIVAS:
            frase_candidata = r.choice(self._frases)
            
            if frase_candidata != self._frase_anterior:
                frase_escolhida = frase_candidata
                break
            tentativas += 1

        if frase_escolhida is None: 
            frase_escolhida = r.choice(self._frases)
        
        self._total_aberturas += 1
        self._id_sequencial += 1
        data_hora_agora = datetime.now().strftime(FORMATO_DATA_HORA)
        
        registro = {
            "id": self._id_sequencial,
            "frase": frase_escolhida,
            "data_hora": data_hora_agora
        }

        self._frase_anterior = frase_escolhida 
        self._historico.append(registro)
        
        self.salvar_historico()

        return frase_escolhida



    def resetar_historico(self) -> None:
        self._historico = []
        self._total_aberturas = 0
        self._id_sequencial = 0
        
        self.salvar_historico()



    def get_total_frases(self) -> int:
        return self._total_aberturas
        

        
    def exportar_historico_para_texto(self) -> tuple[str, str]:
        data_atual = datetime.now().strftime("%d%m%Y")
        nome_arquivo = f"biscoito_historico_{data_atual}.txt"
        
        conteudo = f"--- HISTÓRICO COMPLETO DE BISCOITOS DA SORTE ---\n"
        conteudo += f"Total de Biscoitos Abertos: {self._total_aberturas}\n"
        conteudo += "----------------------------------------------------\n\n"
        
        for item in self._historico:
            conteudo += f"ID: {item['id']} | Data/Hora: {item['data_hora']} | Frase: {item['frase']}\n"
            
        return conteudo, nome_arquivo
        