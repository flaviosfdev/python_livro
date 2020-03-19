from datetime import date


def somar(a, b):
    return a + b
c = somar(2, 2.5)
print(c)

print('==========================')

# valores padronizados de argumentos
def salario_descontado_imposto(salario, imposto=11.): # imposto tem valor padrão
    return salario - (salario * imposto * 0.01)

print(salario_descontado_imposto(1039))
# se fosse passado um segundo parâmtro, este substituiria o valor padrão do parâmetro 'imposto' da assinatura do método

