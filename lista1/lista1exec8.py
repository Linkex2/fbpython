import math

preco = int(input("Digite o custo de Fabrica: "))

distribuido = preco * 0.28
imposto = preco * 0.45

total = int(imposto + distribuido + preco)
print(f"O preço do carro será: {total}, imposto é {imposto} e distribuido é {distribuido}")