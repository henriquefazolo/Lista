'''
Crie uma lista de string vetI e atribua a cada um de seus elementos um nome com dados vindos do teclado.
Por exemplo:
vetI[0] => "Maria";
vetI[1] => "Joao";
vetI[2] => "Marcelo";
vetI[3] => "Antonia";
Atribua à uma string sBusca um nome com dados vindos do teclado. Mostre na tela os valores dos índices que contém sBusca.
sBusca => "Marcelo"
saída: 2

'''

tabalho_lista = int(input('Insira o tamanho da lista : '))

vetI = []

for i in range(tabalho_lista):
    vetI.append(str(input('Insira um nome : ')))

sBusca = str(input('Digite o nome a ser buscado : '))

if sBusca in vetI:
    print(vetI.index(sBusca))



