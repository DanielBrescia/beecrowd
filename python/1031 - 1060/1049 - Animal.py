#Animal
entrada = input()
if entrada == 'vertebrado':
    entrada = input()
    if entrada == 'ave':
        entrada = input()
        if entrada == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        entrada = input()
        if entrada == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    entrada = input()
    if entrada == 'inseto':
        entrada = input()
        if entrada == 'hematofago':
            print('pulga')
        else: 
            print('lagarta')
    else:
        entrada = input()
        if entrada == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
    
