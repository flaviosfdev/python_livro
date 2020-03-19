
# o comando while executa até que:
# a expressao seja avaliada com False
# tenha uma chamada break ou
# levante uma excecao sem tratamento

salario = int(input('Salário? '))
imposto = 27.

while imposto > 0:
    imposto = input('Imposto ou (s) para sair: ')
    if not imposto:
        imposto = 27.
    elif imposto == 's':
        break
    else:
        imposto = float(imposto)

    print('Valor real: {00}'.format(salario - (salario * (imposto * 0.01))))