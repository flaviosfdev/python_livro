# string em python significa sequencia de caracteres
# não existe tipo char, tudo(texto) é string

# acessar elementos code points => variavel[index]
# O índice varia de 0 até o tamanho da string menos 1.
# Se ele for negativo, a contagem é na ordem inversa

nome = "Flávio"

# acesso por índice
print(nome[2])

# saber tamanho de string
print(len(nome))

# acesso de trechos => slice notation
print(nome[1:3]) # variavel[inicio:fim -1]

print("F" not in nome) # case sensitive
print("F" in nome)

# strings sao sequencias imutaveis
# nome[5] = "a" ===>>>> TypeError: 'str' object does not support item assignment

nome = nome[:5] + "a"
print(nome)
# ou
nome = nome.replace("a", "o")
print(nome)

