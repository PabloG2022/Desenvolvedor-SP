#objetivo - calcular o percentual de representações dos estados
# entrada - faturamento mensal
# Saída - Mensagem


SP = float(67.83643)
RJ  =float(36.67866)
MG  =float(29.22988)
ES = float(27.16548)
Outros = float(19.84953)
valor_total = float(SP + RJ + MG + ES + Outros)
print(valor_total)
porcentagem_SP = float((valor_total/SP)*100)
porcentagem_RJ = float((valor_total/RJ)*100)
porcentagem_MG = float((valor_total/MG)*100)
porcentagem_ES = float((valor_total/ES)*100)
porcentagem_Outros = float((valor_total/Outros)*100)

print(f'Porcentagem de SP {porcentagem_SP:6.2f}')
print(f'Porcentagem de RJ {porcentagem_RJ:6.2f}')
print(f'Porcentagem de MG {porcentagem_MG:6.2f}')
print(f'Porcentagem de ES {porcentagem_ES:6.2f}')
print(f'Porcentagem de OUT {porcentagem_Outros:6.2f}')
