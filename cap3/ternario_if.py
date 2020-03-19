imposto = 0.3
valor_imposto = "Alto" if imposto > 0.27 else "Baixo"
print(valor_imposto)

imposto = 0.1
valor_imposto = 'Alto' if imposto > 0.27 else 'Baixo'
print(valor_imposto)

imposto = float(input('Imposto: '))
if imposto < 10.:
    print('baixo')
elif imposto >= 10. and imposto <= 27.:
    print('médio')
elif imposto > 27. and imposto < 100:
    print('alto')
else:
    print('imposto inválido')