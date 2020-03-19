# unpacking é um processo de 'desencapsulamento' na assinatura de metodos
print('Parâmetros ORDENADOS: Listas/Tuplas')
print('Parâmetros NOMEADOS: Dicionários')
def unpacking_experiment(*args):
    nome = args[0]
    telefone = args[1]
    email = args[2]
    data = [nome, telefone, email]
    return data

data = unpacking_experiment('Flávio', '84 9 9999-9999', 'flavio@dev.com')
print('=====================================')
print('Parâmetros ORDENADOS:', data)


def unpacking(**kwargs):
    nome = kwargs['nome']
    telefone = kwargs['telefone']
    email = kwargs['email']
    dados = {'nome': nome, 'telefone': telefone, 'email': email}
    return dados

dados = unpacking(nome='Flávio', telefone='84 9 9999-9999', email='flavio@dev.com')
print('Parâmetros NOMEADOS:', dados)
