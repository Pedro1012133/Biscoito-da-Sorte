import flet as ft
from controllers import biscoito_controller


class BiscoitoView:
    def __init__(self, page: ft.Page, controller):
        # Parametros
        self.page = page  
        self.controller = controller 
        
        # Criação da frases da tela
        self.page.title = "Biscoito da Sorte V5"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
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
        
        self.botao_exportar = ft.TextButton(
            text="Exportar Histórico",
            on_click=self.controller.clique_exportar_historico, 
        )



    def montar_layout(self):
        self.controller.buscar_e_atualizar_contador()

        return ft.Container(
            content=ft.Column(
                controls=[
                    self.frase_texto,
                    ft.Divider(height=25, color=ft.Colors.TRANSPARENT),
                    self.contador_texto,
                    ft.Row(
                        [self.botao_abrir], 
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [self.botao_reset, self.botao_exportar],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=30
        )



    def exibir_contador(self, total_atualizado: int): 
        self.contador_texto.value = f"Biscoitos abertos: {total_atualizado}"
        self.page.update()



    def atualizar_frase(self, frase_nova, quantidade_frase_atualizada):
        self.frase_texto.value = frase_nova
        self.exibir_contador(quantidade_frase_atualizada)


    
    def resetar(self, depois_reset):
        self.frase_texto.value = "Histórico limpo! Clique para começar."
        self.exibir_contador(depois_reset)



    def exibir_mensagem_sucesso(self, mensagem: str):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(mensagem), 
            bgcolor=ft.Colors.GREEN_700, 
            duration=4000
        )
        self.page.snack_bar.open = True
        self.page.update()



    def exibir_mensagem_erro(self, mensagem: str):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(mensagem), 
            bgcolor=ft.Colors.RED_700, 
            duration=6000
        )
        self.page.snack_bar.open = True
        self.page.update()