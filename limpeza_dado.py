# Regex
import re  

# Leitura com open, read e um alias
filename = 'insulin.txt'

with open(filename) as fn:
    content = fn.read()

# Uso do regex
corrigido = re.sub(r'(ORIGIN|//|\d+|\s+)', '', content)
print(corrigido)

print(len(corrigido))


# cria os cortes
lsinsulin = corrigido[0:24]    # 1-24
binsulin = corrigido[24:54]    # 25-54
cinsulin = corrigido[54:89]    # 55-89
ainsulin = corrigido[89:110]   # 90-110

# salva os arquivos
with open("1_lsinsulin-seq-clean.txt", "w") as f:
    f.write(lsinsulin + "\n")

with open("2_binsulin-seq-clean.txt", "w") as f:
    f.write(binsulin + "\n")

with open("3_cinsulin-seq-clean.txt", "w") as f:
    f.write(cinsulin + "\n")

with open("4_ainsulin-seq-clean.txt", "w") as f:
    f.write(ainsulin + "\n")

'''
Explicação da regex:

re.sub(r'()') → remove

ORIGIN → corresponde exatamente à palavra ORIGIN

// → corresponde exatamente às duas barras

\d+ → corresponde a qualquer sequência de um ou mais dígitos numérico

\s+ → remove espaços

O | é um OR lógico dentro do regex, ou seja, remove qualquer uma dessas opções.

'''