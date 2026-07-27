#salario com bonus
nome = input()
salario_fixo = float(input())
total_vendas = float(input())
bonus = 0.15
total = salario_fixo + (total_vendas * bonus)
print(f'TOTAL = R$ {total:.2f}')
