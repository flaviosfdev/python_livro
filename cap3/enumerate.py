
# a função enumerate é utilizada quando se quer uma lista enumerada
# exemplo:

frutas = ['abacaxi', 'laranja', 'morango']

for i, fruta in enumerate(frutas):
    print('{} - {};'.format(i, fruta))


# O comando FOR funciona com qualquer objeto do tipo sequência como:
# listas, strings ou com objetos iteráveis(ex.: range())
