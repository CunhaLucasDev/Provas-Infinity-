# Você está desenvolvendo um programa em Python para calcular a soma dos números pares dentro de um intervalo determinado pelo usuário.
#  O programa deve solicitar ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. Implemente a estrutura 'else' para exibir
#  uma mensagem indicando que não há números pares no intervalo, caso seja o caso.
# Ao final, exiba a soma dos números pares encontrados.

print('Calculadora da soma dos numeros pares no intervalo determinado pelo Usuario :')
inicio = int(input('Informe o inicio da sequencia:   '))
final = int(input('Informe o final da sequencia:  '))
soma_numeros = 0 

for n in range(inicio, final+1,1):
    if n % 2 ==0 :
      soma_numeros = soma_numeros + n 
      print(n)
if not n % 2 ==0 :  
   print('Não existe numeros pares na sequencia')
    
print(soma_numeros)

print('Fim do Programa ')