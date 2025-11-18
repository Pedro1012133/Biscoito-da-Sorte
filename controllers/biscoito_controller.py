import flet
from models.biscoito_model import BiscoitoModel


class BiscoitoController:
    def __init__(self, objeto_model):
        self.model = objeto_model
        self.view = None 



    def set_view(self, view_instance):
        self.view = view_instance


        
    def clique_abrir_biscoito(self, e):
        obter_frase = self.model.obter_frase()
        get_total_frases = self.model.get_total_frases()
        
        if self.view:
            self.view.atualizar_frase(obter_frase, get_total_frases)



    def clique_resetar_historico(self, e):
        self.model.resetar_historico()
        get_total_frases = self.model.get_total_frases()

        depois_reset = get_total_frases

        if self.view:
            self.view.resetar(depois_reset)