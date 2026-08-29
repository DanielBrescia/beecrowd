import time

inicio = time.time()

saque = int(input())
print(saque)
caixa = {100:0,50:0,20:0,10:0,5:0,2:0,1:0}
for i, qtd in caixa.items():
    nota = saque // i
    caixa[i] = nota
    print(f'{nota} nota(s) de R$ {i},00')
    saque = saque % i

fim = time.time()
print("Tempo de execução:", fim - inicio, "segundos")