import random
class ContaBancaria:
    def __init__ (self, titular):
        self.titular = titular
        self.saldo = 0
        id = str(random.randint(0, 999)).zfill(3)
        self.conta_id = id
    
    def __str__(self):
        template = (f' ========Banco do Brasil========\n Nº da conta: {self.conta_id}\n Titular: {self.titular}\n Saldo: {self.saldo}\n'+ '='*31)
        return template.format(self)
    
    def depositar(self, valor):
        self.valor = valor
        self.saldo = self.saldo + self.valor

    def sacar(self, sacar):
        self.sacar = sacar
        if(self.saldo > self.sacar):
            print(f'Saque de R${self.sacar} efetuado com sucesso!')
        else:
            print(f'Saldo insuficiente!')
    
conta = ContaBancaria('Jorge Pinetti')
while True:
    print(f'='*30+ '\n 1 - Mostrar saldo \n 2 - Depositar\n 3 - Sacar\n 4 - Sair\n', '='*31)
    acao = int(input('O que deseja fazer? '))

    if(acao == 1):
        print(conta)

    elif(acao == 2):
        print('='*30)
        deposito = int(input('Valor do deposito: '))
        print('='*30)
        conta.depositar(deposito)

    elif(acao == 3):
        print('='*30)
        saque = int(input('Valor de saque: '))
        print('='*30)
        conta.sacar(saque)
    elif(acao == 4):
        print('Encerrando sessão...')
        break
