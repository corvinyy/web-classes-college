
import random

def linhas():
    print("----------------------------------")

x = random.randint(0, 5)
tentativas = 0


while True:
    valor = int(input("Adivinhe o número entre 0 e 40: "))

    if valor == x:
        linhas()

        print(f"Você acertou! \nValor digitado: {valor} \nValor de x: {x}")
        tentativas = tentativas + 1
        print(f"Tentativas: {tentativas}")
        break

    elif valor > x:
        linhas()

        print(f"o X é menor que {valor}")
        tentativas = tentativas + 1
        print(f"Tentativas: {tentativas}")

    else:
        linhas()
        
        print(f"o X é maior que {valor}")
        tentativas = tentativas + 1
        print(f"Tentativas: {tentativas}")