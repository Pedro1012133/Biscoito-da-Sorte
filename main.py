import flet as ft
from models.biscoito_model import BiscoitoModel
from views.biscoito_view import BiscoitoView
from controllers.biscoito_controller import BiscoitoController


def main(page: ft.Page):
    page.title = "Biscoito da Sorte"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Instanciação dos objetos
    model = BiscoitoModel()
    controll = BiscoitoController(objeto_model=model) 
    view = BiscoitoView(page=page, controller=controll) 

    # Injeção do View no Controller
    controll.set_view(view) 

    # Adicionar o Layout na tela
    page.add(view.montar_layout())

ft.app(target=main)