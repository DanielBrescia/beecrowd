# Função do tipo "pergunta"
def retorna_media(a, b, c): #Def = definição
    m = (a + b + c) / 3
    return m #responde algo

# Função do tipo "Ordem"
def exibe_media(a, b, c): #Todo parametro é uma variável local
    m = (a + b + c) / 3
    print(m)

x = int(input('1º valor: ')) #Variavel global
y = int(input('2º valor: '))
z = int(input('3º valor: '))

m1 = retorna_media(x, y, z) #importa a ordem, para ligar a (a, b, c)
print(f'm1 = {m1}')

m2 = exibe_media(x, y, z) 

