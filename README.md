# PROVA10 — Formulário de Contato

Este projeto é um exemplo simples que mostra um formulário de contato. A pessoa preenche Nome, Email e Mensagem e clica em Enviar. Depois aparece uma mensagem dizendo se o envio deu certo ou se faltou alguma informação.

Arquivos importantes
- `PROVA10.py`: abre a pequena aplicação.
- `pagina_cadastro.py`: cria a página com os campos e o botão.
- `formulario.py`: valida os dados (verifica se os campos foram preenchidos e se o email tem formato básico).
- `requirements.txt`: lista a única dependência necessária (`flet`).

Como usar (Windows PowerShell)
1. (Opcional) Crie um ambiente virtual para não misturar com outros programas:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instale a dependência e abra o programa:

```powershell
pip install -r requirements.txt
python PROVA10.py
```

O que acontece na aplicação
- Preencha Nome, Email e Mensagem.
- Clique em Enviar.
- Se tudo estiver certo, verá: "Formulário enviado com sucesso!".
- Se faltar alguma informação ou o email estiver inválido, aparecerá uma mensagem explicando o problema.

Se precisar que eu deixe o texto ainda mais simples, adicione exemplos ou crie um passo-a-passo com imagens, digo o que você prefere e eu faço.
