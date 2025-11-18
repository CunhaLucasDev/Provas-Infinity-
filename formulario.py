import re


def formulario_cadastro(nome: str, email: str, mensagem: str) -> tuple[str, bool]:
    """Valida e processa os dados do formulário de contato.

    Retorna uma tupla (mensagem, sucesso). `mensagem` é o texto em português
    que será mostrado para o usuário; `sucesso` é True quando os dados
    estiverem válidos e a interface pode limpar os campos.
    """
    nome = (nome or "").strip()
    email = (email or "").strip()
    mensagem = (mensagem or "").strip()

    if not (nome and email and mensagem):
        return ("Por favor, preencha todos os campos.", False)

    # verificação simples de formato de e-mail
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return ("Email inválido. Verifique e tente novamente.", False)

    # Aqui poderíamos salvar ou enviar os dados. Para o exercício, retornamos sucesso.
    return ("Formulário enviado com sucesso!", True)
