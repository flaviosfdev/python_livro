# importando módulos
# import math

# importando módulo com alias
# nesse caso, é possível criar uma variavel com o nome real do módulo
import math as matematica

print(matematica.sqrt(9))

# importando apenas um objeto específico de um módulo
# from: módulo
# import: objeto
from math import sqrt as raiz_quadrada
print(raiz_quadrada(64))

from math import pow as potencia
print(potencia(2,3)) # => 2^3