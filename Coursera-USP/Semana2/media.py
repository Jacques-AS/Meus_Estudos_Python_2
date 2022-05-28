'''
Exercício 2
Faça um programa em Python que receba quatro notas,
calcule e imprima a média aritmética. Observe o exemplo abaixo:
Exemplo:
Entrada de Dados:
Digite a primeira nota: 4
Digite a segunda nota: 5
Digite a terceira nota: 6
Digite a quarta nota: 7
Saída de Dados:
A média aritmética é 5.5
'''
primeira_nota = int(input('Digite primeira nota: '))
segunda_nota = int(input('Digite segunda nota: '))
terceira_nota = int(input('Digite terceira nota: '))
quarta_nota = int(input('Digite quarta nota: '))
media_aritmetica = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print(f'A média aritmética é {media_aritmetica}')