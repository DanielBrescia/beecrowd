soma = 0 #Variável acumuladora
qtd = 0 # variável contadora
n = int(input())
while n > 0:
    soma += n
    qtd += 1
    n = int(input())

print(f'{soma / qtd:.2f}')
