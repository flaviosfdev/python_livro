
frutas = ['manga', 'banana', 'abacaxi', 'laranja', 'kiwi']

print('=== Lista de Frutas ===')
cont = 0
for fruta in frutas:

    if fruta.startswith('a'):
        continue

    print('Fruta {}: {}'.format(cont, fruta))
    cont += 1

print('=== Fim lista de Frutas ===')