telefones = []

while True:
    opcao = int(input('''Escolha uma opção: 
[1] - Adicionar telefone
[2] - Remover telefone
[3] - Verificar telefone
[4] - Mostrar agenda
[0] - Sair
opção: '''))
    
    if opcao == 1:
        add_num = int(input('Digite o numero de telefone que deseja adicionar: '))
        telefones.append(add_num)

    elif opcao == 2:
        remover_num = int(input('Digite o número de telefone que deseja remover: '))
        telefones.remove(remover_num)

    elif opcao == 3:
        verif_num = int(input('Número que deseja verificar: '))
        if verif_num in telefones:
            print(f'O número {verif_num} está na lista')
        else:
            print(f'O número {verif_num} NÃO está na lista')
    
    elif opcao == 4:
        for i in telefones:
            print(f'Telefones: {i}')

    elif opcao == 0:
        print('Saindo...')
        break