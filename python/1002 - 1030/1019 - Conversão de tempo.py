seg = int(input())
horas = seg // 3600 #entraga valor inteiro
resto = seg % 3600 #entrega valor restante 
minuto = resto // 60 
segundos = resto % 60
tempo =[horas, minuto, segundos]
print(f"{tempo[0]}:{tempo[1]}:{tempo[2]}")