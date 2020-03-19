aprendendoPython = 59.90
aprendendoJava = 59.90

soma = aprendendoJava + aprendendoPython

print("O total em estoque é: R$ {}".format(soma))

soma = 0
contador = 0

while contador < 35:
    soma += 59.90
    contador += 1

print("Soma: R$ {}".format(soma))

if soma < 150:
    print("Seu estoque está muito baixo!")
elif soma >= 2000:
    print("Seu estoque está muito alto!")
else:
    print("Seu estoque está bom!")

imaginario = 1 + 5j
print(imaginario.imag)
print(imaginario)