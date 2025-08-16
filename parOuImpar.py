num = int(input('Insira um numero: '))

conta = num%2

if(conta == 0):
    print(f'O numero', num, 'é par')
else:
    print(f'O numero', num, 'é impar')
