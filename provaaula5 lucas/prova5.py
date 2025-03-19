
#[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de
#  alunos em uma disciplina. O programa deve solicitar ao usuário o número de
#  alunos e,  em seguida, para cada aluno, pedir o nome e três notas.
#  Utilize um loop 'for' para iterar sobre os alunos e suas notas.

#Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação
#  ou reprovação.Ao final, exiba a média geral da turma.

#nota 
#nome 
#media 
#aprovado 
print('Programa para calculo das notas e apresentação de Medias: ')

qtd_alunos = int(input('Informe a quantidade de alunos :'))
nota_media_turma=0
for i in range (0,qtd_alunos):
    nome_aluno = input('informe o nome do aluno :')
    nota1 = float(input('Informe a nota do aluno :'))
    nota2 = float(input('Informe a nota do aluno :'))
    nota3 = float(input('Informe a nota do aluno :'))
    nota_media = (nota1+nota2+nota3)/3 
    if nota_media >=7:
      print(f'O {nome_aluno}, teve as notas{nota1}, {nota2}, {nota3}  sendo  aprovado com a media{nota_media}:')
    else:
      print (f'O {nome_aluno}, teve as notas  {nota1}, {nota2}, {nota3} sendo  reprovado com a media de {nota_media}')
    nota_media_turma =float(nota_media_turma + nota_media)
nota_final_turma = nota_media_turma/qtd_alunos


print(f'A media da turma foi {nota_final_turma}')

print('Fim do Programa')


