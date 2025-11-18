import flet as ft
from controllers import biscoito_controller


class BiscoitoView:
    def __init__(self, page: ft.Page, controller):
        # Parametros
        self.page = page  
        self.controller = controller 
        
        # Criação da frases da tela
        self.frase_texto = ft.Text("Clique para uma frase!", size=30)
        self.contador_texto = ft.Text("Biscoitos abertos: 0", size=16)
        
        # Criação dos botões e ligação com o Controller
        self.botao_abrir = ft.ElevatedButton(
            text="Abrir Biscoito 🥠",
            on_click=self.controller.clique_abrir_biscoito, 
        )
        
        self.botao_reset = ft.TextButton(
            text="Limpar Histórico",
            on_click=self.controller.clique_resetar_historico,
        )



    def montar_layout(self):
        # Monta os componetes na tela
        return ft.Column(
            controls=[
                self.frase_texto,
                self.contador_texto,
                ft.Row([self.botao_abrir, self.botao_reset], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )



    def atualizar_frase(self, frase_nova, quantidade_frase_atualizada):
        self.frase_texto.value = frase_nova
        self.contador_texto.value = f"Biscoitos abertos: {quantidade_frase_atualizada}"
        self.page.update()



    def resetar(self, depois_reset):
        self.frase_texto.value = "Histórico limpo! Clique para começar."
        self.contador_texto.value = f"Biscoitos abertos: {depois_reset}"
        self.page.update()