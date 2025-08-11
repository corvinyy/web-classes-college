lista_func = []

while True:
    opcao = int(input("1. Cadastrar \n2. Exibir todos os funcionários \n3. Exibir média dos salários \n4. Exibir funcionários com salário > 5000 \n5. Sair \nOpção: "))

    if opcao == 1:

        funcionario = {}
        funcionario['nome'] = input("Nome: ")
        funcionario['idade'] = int(input("Idade: "))
        funcionario['cargo'] = input("Cargo: ")
        funcionario['salario'] = float(input("Salário: "))
        print('----------------------------------------------------')
        
        lista_func.append(funcionario)

    elif opcao == 2:
        for i in lista_func:
            print('----------------------------------------------------')
            print(f'Nome: {i['nome']}')
            print(f'Cargo: {i['cargo']}')

    elif opcao == 3:
        media = 0
        for s in lista_func:
            media = media + s['salario']
        print(f'Média Salarial: {media/len(lista_func)}')
            
    elif opcao == 4:
        for s in lista_func:
            if s['salario'] > 5000:
                print('----------------------------------------------------')
                print(f'Nome: {s['nome']}')
                print(f'Salário: {s['salario']}')
                    
    elif opcao == 5:
        print('Saindo...')
        break

    else:
        print("Opção inválida")
