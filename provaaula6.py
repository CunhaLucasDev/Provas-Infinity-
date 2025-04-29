#Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos.
#  Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam.
#  Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
#Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

print('Acesso ao Sistema:  Para continuar iremos precisar do seu login e senha:')

tentativas = 3 

usuario_correto = 'Mario123'

senha_correta = '1234'

for tentativas in range (3):
    usuario = input('Informe seu usuario :')
    senha = input('Informe sua senha : ')
    if usuario == usuario_correto and senha == senha_correta: 
        print('Acesso concedido: Bem Vindo !!')
        break
    else :
      print('Usuario ou senha incorretos !')
    tentativas_restantes = 2 - tentativas
    if tentativas > 0 :
       print('Voce ainda tem',tentativas_restantes,'tentativas')

else :
   for tentativas in range (3):
       print('Acesso Bloqueado')
    


