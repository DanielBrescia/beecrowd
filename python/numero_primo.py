primo = []
qtd_divisores = 0
n = int(input())
cont = 1
while cont <= n:
    if n % cont == 0:
        qtd_divisores += 1
        primo.append(cont)
        print(primo)
    cont += 1
    #if qtd_divisores == 2:
    #    print('É primo')
    #else:
    #    print('Não e primo')
print(primo)
print(qtd_divisores)