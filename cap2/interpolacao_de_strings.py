
# Interpolacao pode ser feita com % ou .format

# Python também implementa o formato printf

print('% dias para a copa' %(100)) # substitui os caracteres a partir do símbolo %

print('%d dias para a copa' %(100))
# %d => inteiro
# %s => string
# %f => float

print('{} dias para a copa'.format(100))

# format com variaveis como paramentro
print('{dias} dias para a {evento}'.format(evento = 'copa', dias = 100))
