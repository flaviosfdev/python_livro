#
# salario = 3000
# imposto = 0.27
#
# print(salario - (salario * imposto))
# aplicando tratamento de string
# print('Valor real: R$ {}'.format(salario - (salario * imposto)))

salario = int(input('Salário: '))
imposto = input('Imposto em % (ex.: 27.5): ')

# if imposto == '': ===> string vazia equivale a false (not)

imposto = 27.5 if not imposto else float(imposto) # chamado operador ternário ()
# if not imposto:
#     imposto = 27.5
# else:
#     imposto = float(imposto)

# if imposto < 10:
#     print('Imposto Médio: {}'.format(imposto) + '%')
# elif imposto < 27.5:
#     print('Imposto Alto: {}'.format(imposto) + '%')
# else:
#     print('Imposto Muito Alto: {}'.format(imposto) + '%')

if imposto < 10.:
    print('Imposto Baixo: {}'.format(imposto))
elif 10. <= imposto <= 27.:
    print('Imposto Médio: {}'.format(imposto))
elif 27. < imposto <= 100:
    print('Imposto Alto: {}'.format(imposto))
else:
    print('Imposto Inválido!')

print('O valor real é: R$ {}'.format(salario - (salario * imposto * 0.01))  )