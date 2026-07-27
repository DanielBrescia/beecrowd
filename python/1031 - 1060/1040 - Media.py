
n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n_final = ( (n1 * 2) + (n2 * 3) +  (n3 * 4) +  (n4 * 1) ) / 10
print(f'Media: {n_final:.1f}')
if n_final >= 7.0:
    print('Aluno aprovado.')
if n_final >= 5.0 and n_final <=6.9:
    print('Aluno em exame.')
    ex = float(input())
    print(f'Nota do exame: {ex}')
    exame = (n_final + ex) / 2
    if exame >= 5.0:
        print ('Aluno aprovado.')
        print (f'Media final: {exame:.1f}')
    else:
        print ('Aluno reprovado.')
if n_final < 5.0:
    print('Aluno reprovado.')