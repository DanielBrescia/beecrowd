soma = 0 #Variável acumuladora
menor = 0
qtd = 0 # variável contadora
n = int(input())
while n > 0:
    if n < 18:
        menor += n
        qtd += 1
        n = int(input())
    else:
        soma += n
        qtd += 1
        n = int(input())

print(f'{soma / qtd:.2f}')
print(f'{menor / qtd:.2f}')