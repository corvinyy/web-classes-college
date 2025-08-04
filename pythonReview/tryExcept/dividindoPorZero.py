try: 
    valor1 = int(input("Digite o primeiro número: "))
    valor2 = int(input("Digite o segundo número: "))
    valor1 / valor2
    print(valor1/valor2)
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
except ValueError:
    print('Por favor digite apenas números inteiros!')
finally:
    print('Executada')