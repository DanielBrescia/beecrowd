maior = int(input())
posicao_maior = 1
qtd = 99
posicao_atual = 2
while qtd > 0:
    atual = int(input())
    qtd -= 1
    if atual > maior:
        maior = atual
        posicao_maior = posicao_atual
    posicao_atual += 1
print(f'{maior}')
print(f'{posicao_maior}')
