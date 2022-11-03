#objetivo-  receber a palavra, inverter e mostrar na tela
# Entrada - String palavra
#Saida - Mensagem normal e invertida
Palavra = ''
while Palavra != "N" and Palavra != "n":
    Palavra = input('digite a palavra para vê-la invertida: ')
    Palavra_invertida = Palavra[::-1]
    print('Palavra normal: ',Palavra,'\npalavra invertida: ', Palavra_invertida)
    Palavra = input('deseja ver outra palavra? S/N: ')

print('saiu do loop')    
