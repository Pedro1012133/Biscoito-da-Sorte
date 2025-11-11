"""
PROJETO BISCOITO DA SORTE
"""

import flet as ft
import random
from dados import FRASES
<<<<<<< HEAD

=======
>>>>>>> V2

# ============================================================================
# Estado da Aplicação
# ============================================================================
contador_cliques = 0
frase_atual = ""


# ============================================================================
# Função Principal da Aplicação
# ============================================================================
def main(page: ft.Page):
    # Configurações da janela
    page.title = "Biscoito da Sorte"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    global contador_cliques, frase_atual
    
    # ========================================================================
    # Componentes da Interface
    # ========================================================================
    
    # Título
    titulo = ft.Text(
        "🥠 Biscoito da Sorte",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="amber800",
        text_align=ft.TextAlign.CENTER,
    )
    
    # Container para exibir a frase
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
        "Biscoitos abertos: 0",
        size=14,
        color="grey600",
        text_align=ft.TextAlign.CENTER,
    )
    
    # ========================================================================
    # Função de Evento (Callback)
    # ========================================================================
    def abrir_biscoito(e):
        """
        Função chamada quando o botão é clicado.
        """
        global contador_cliques, frase_atual
        
        # Seleciona frase aleatória
        frase_atual = random.choice(FRASES)
        
        # Incrementa contador
        contador_cliques += 1
        
        # Atualiza o texto da frase na tela
        frase_texto.content = ft.Text(
            frase_atual,
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="amber900",
            weight=ft.FontWeight.W_500,
        )
        
        # Atualiza o contador na tela
        contador_texto.value = f"Biscoitos abertos: {contador_cliques}"
        
        # Atualiza a página
        page.update()
    
    # ========================================================================
    # Botão de Ação
    # ========================================================================
    botao = ft.ElevatedButton(
        text="Abrir Biscoito 🥠",
        # icon="cake",
        on_click=abrir_biscoito,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="amber700",
            padding=20,
        ),
        width=200,
        height=50,
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
                ft.Container(height=20),  # Espaçamento
                contador_texto,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
    )


# ============================================================================
# Execução
# ============================================================================
if __name__ == "__main__":
    ft.app(target=main)