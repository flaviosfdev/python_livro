# packing é um processo de 'encapsulamento' na chamada de metodos
# pode ser usando quando uma tupla ou lista possui os elementos
# sequenciados na mesma ordem de uma lista de parâmtros de um método
# exemplo:

from datetime import date

d = (2020, 3, 10) # tupla com data
bd = [2020, 3, 21]
# a funcao date(year, month, day) => recebe por padrão ano/mes/dia como paramentros
# pode-se optar por usar date(*tupla)/date(*lista)
# caso a ordem dos elementos case com a ordem dos parâmetros da função

# packing posicional: listas e tuplas
# packing nomeado: dicionários

data = date(*d)
b_day = date(*bd)
print('d = ', data)
print('bday = ', b_day)
print('==================')

def new_user(active = False, admin = False):
    print(active)
    print(admin)

config = {'active': True, 'admin': True}

new_user(config.get('active'), config.get('admin'))

# usando packing com parametros nomeados
print('=====================')
def novo_usuario(ativo = False, administrador = False):
    print(ativo)
    print(administrador)

configuracoes = {'ativo': True, 'administrador': True}
novo_usuario(*configuracoes)
novo_usuario(**configuracoes)
# 1* => chaves do dicionário
# 2* => valores das chaves do dicionário