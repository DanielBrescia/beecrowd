def eh_par(x):
    if x % 2 == 0:
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

qtd_pares = 0

if eh_par(a):
    qtd_pares +=1
    
if eh_par(b):
    qtd_pares +=1
    
if eh_par(c):
    qtd_pares +=1
    
if eh_par(d):
    qtd_pares +=1
    
if eh_par(e):
    qtd_pares +=1

print(f'{qtd_pares} valores pares')
