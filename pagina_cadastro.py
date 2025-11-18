import flet as ft
from formulario import formulario_cadastro


def construir_pagina(page: ft.Page) -> None:
    """Constrói e anexa a interface do formulário de contato à página fornecida."""
    page.title = "Formulário de Contato - PROVA10"

    nome_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    mensagem_input = ft.TextField(label="Mensagem", width=300, multiline=True, height=100)
    confirmacao_text = ft.Text("")

    def enviar_formulario(e):
        msg, ok = formulario_cadastro(nome_input.value, email_input.value, mensagem_input.value)
        confirmacao_text.value = msg
        if ok:
            nome_input.value = ""
            email_input.value = ""
            mensagem_input.value = ""
        page.update()

    enviar_button = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    page.add(
        nome_input,
        email_input,
        mensagem_input,
        enviar_button,
        confirmacao_text,
    )
