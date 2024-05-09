lista = []
lista_de_letras = list("Duduzinho")
lista_de_numeros = list(range(10))

print(lista)
print(lista_de_letras)
print(lista_de_numeros)

print("Ultima letra da lista ", lista_de_letras[-1])

listanova = lista_de_letras + lista_de_numeros

print(listanova)
print("Tamanho da lista nova é: ", len(listanova))
listanova.pop()
print(listanova)
print("Tamanho da lista nova é: ", len(listanova))
del listanova[10]
print(listanova)
print("Tamanho da lista nova é: ", len(listanova))
listanova.append("AAAAAA")
print(listanova)
print("Tamanho da lista nova é: ", len(listanova)) 

