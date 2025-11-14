"""
PROJETO BISCOITO DA SORTE
"""

import flet as ft
import random
from models.biscoito_model import BiscoitoModel
from dados import FRASES



# ============================================================================
# Função Principal da Aplicação
# ============================================================================
def main(page: ft.Page):
    biscoito_model = BiscoitoModel()
    
    # Configurações da janela
    page.title = "Biscoito da Sorte"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # ========================================================================
    # Componentes da Interface (View)
    # ========================================================================
    
    # Título
    titulo = ft.Text(
        "🥠 Biscoito da Sorte",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="amber800",
        text_align=ft.TextAlign.CENTER,
    )
    
    # Container para exibir a frase principal
    frase_texto = ft.Container(
        content=ft.Text(
            "Clique no botão para abrir seu biscoito!",
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="grey700",
        ),
        margin=ft.margin.symmetric(vertical=30),
        padding=20,
        bgcolor="amber50",
        border_radius=10,
        border=ft.border.all(2, "amber200"),
        alignment=ft.alignment.center,
    )
    
    # Contador de cliques
    contador_texto = ft.Text(
        f"Biscoitos abertos: {biscoito_model.get_total_frases()}",
        size=14,
        color="grey600",
        text_align=ft.TextAlign.CENTER,
    )
    
    
    # ========================================================================
    # Função de Evento (Controller)
    # ========================================================================
    
    def abrir_biscoito(e):
        """
        Função chamada quando o botão é clicado.
        """
        
        # Atualiza o texto da frase na tela
        frase_texto.content = ft.Text(
            biscoito_model.obter_frase(),
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="amber900",
            weight=ft.FontWeight.W_500,
        )
        
        # Atualiza o contador na tela
        contador_texto.value = f"Biscoitos abertos: {biscoito_model.get_total_frases()}"
        
        # Atualiza a página
        page.update()


    def resetar_historico(e):
        """
        Função chamada para resetar o histórico.
        """
        # Zera o estado no Model
        biscoito_model.resetar_historico()
        
        # Atualiza a frase principal para a mensagem inicial
        frase_texto.content = ft.Text(
            "Clique no botão para abrir seu biscoito!",
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="grey700",
        )

        # 3. Atualiza o contador na tela
        contador_texto.value = f"Biscoitos abertos: {biscoito_model.get_total_frases()}"
        
        # 4. Atualiza a página
        page.update()
    
    
    # ========================================================================
    # Botões e Componentes de Layout
    # ========================================================================
    
    # Botão principal
    botao = ft.ElevatedButton(
        text="Abrir Biscoito 🥠",
        on_click=abrir_biscoito,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="amber700",
            padding=20,
        ),
        width=200,
        height=50,
    )

    # Botão de Reset (ft.TextButton)
    botao_reset = ft.TextButton(
        text="Resetar Histórico",
        icon=ft.Icons.RESTART_ALT, 
        on_click=resetar_historico, 
        style=ft.ButtonStyle(color="grey500"),
    )
    
    # Contêiner para posicionar o botão no canto inferior direito
    container_reset_alinhamento = ft.Container(
        content=botao_reset,
        alignment=ft.alignment.center_right, # Alinha o conteúdo à direita
        width=400, # Largura para garantir que o alinhamento funcione
        margin=ft.margin.only(top=20),
    )
    
    
    # ========================================================================
    # Layout da Página
    # ========================================================================
    page.add(
        ft.Column(
            [
                titulo,
                frase_texto,
                ft.Container(
                    content=botao,
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=20),
                contador_texto,
                container_reset_alinhamento, # Adiciona o botão de reset
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
    )



# ============================================================================
# Execução
# ============================================================================
if __name__ == "__main__":
    ft.app(target=main)