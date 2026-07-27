a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maior_AB = (a+b+abs(a-b))/2
maior_C = (maior_AB+c+abs(maior_AB - c))/2
print(f'{maior_C:.0f} eh o maior')