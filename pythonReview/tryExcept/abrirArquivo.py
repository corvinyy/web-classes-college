f = None
try:
    f = open('dados.txt', 'r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print("O arquivo não existe")
finally:
    if f is not None:
        f.close()
    print("Fim da leitura") 
