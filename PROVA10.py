#[PYIA-A10] Desenvolva uma aplicação utilizando o framework Flet que permita ao usuário preencher um
#  formulário de contato. O formulário deve incluir três campos: um campo de texto para o nome,
#  um campo de texto para o email e um campo de texto para a mensagem. 
# Após o usuário preencher esses campos, deve haver um botão de envio. Quando o usuário clicar no botão de envio,
#os dados devem ser processados e uma mensagem de confirmação deve ser exibida na tela,
#  indicando que o formulário foi enviado com sucesso.


import flet as ft
from pagina_cadastro import construir_pagina


def main(page: ft.Page):
    construir_pagina(page)


if __name__ == "__main__":
    ft.app(target=main)