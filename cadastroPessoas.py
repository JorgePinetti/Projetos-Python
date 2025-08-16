db = []
def Registrar(nome, cpf):
    paciente = {'nome': nome, 'cpf' : cpf }
    db.append(paciente)
    return paciente

for i in range(2):
    nome = str(input('Insira um nome: '))
    cpf = str(input('Insira o cpf: '))
    Registrar(nome, cpf)
    print('='*30)

print(db)