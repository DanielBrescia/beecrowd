x = int(input())
y = int(input())

if x > y:
    z = x
    x = y
    y = z

soma = 0
n = x + 1
while n < y:
    if n % 2 == 1:
        soma += n 
    n += 1

print (soma)
    