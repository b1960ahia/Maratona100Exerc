soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma dos {} valores impares multiplos de 3 e {}'.format(cont, soma))





