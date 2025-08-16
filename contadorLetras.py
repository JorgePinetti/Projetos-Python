palavra = str(input("Digite a palavra: "))

list = []

vogais = ['a', 'e', 'i', 'o', 'u']

vogais_count = 0
consoantes_count = 0

for i in range(len(palavra)):
    list.append(palavra[i])
    if (palavra[i] in vogais):
        vogais_count = vogais_count + 1
    else:
        consoantes_count = consoantes_count + 1

print(f'Palavra: ', palavra, '\n Letras: ', len(palavra), '\n Vogais: ', vogais_count, '\n Consoantes: ', consoantes_count)


