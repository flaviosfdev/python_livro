# listas em python são sequencias, sendo possível acessar elementos por:
# indices e slices(trechos)

frutas = ['manga', 'banana', 'abacaxi', 'laranja', 'kiwi']

print(frutas)
print(len(frutas))
print(frutas[1])
print(frutas[-2])

lista = []
# python avalia listas vazias como False
if lista: # não entra nesse laço, pois a lista é vazia
    print('Nunca sou executado')
else:
    print('Sempre sou executado')