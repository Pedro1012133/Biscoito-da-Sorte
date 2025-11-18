import flet
import os
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

        if self.view:
            self.view.resetar(get_total_frases)
            self.view.exibir_mensagem_sucesso("Histórico de aberturas limpo!")



    def buscar_e_atualizar_contador(self):
        get_total_frases = self.model.get_total_frases()

        if self.view:
            self.view.exibir_contador(get_total_frases)



    def clique_exportar_historico(self, e):
        conteudo, nome_arquivo = self.model.exportar_historico_para_texto()
        
        caminho_completo = os.path.join(os.getcwd(), nome_arquivo)
        
        try:
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
                
            if self.view:
                self.view.exibir_mensagem_sucesso(f"Histórico exportado com sucesso para o arquivo: {nome_arquivo}")
                
        except Exception:
            if self.view:
                self.view.exibir_mensagem_erro("Falha ao exportar. Verifique as permissões")