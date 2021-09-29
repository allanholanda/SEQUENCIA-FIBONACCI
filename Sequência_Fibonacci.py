lim = int(input('Digite um limite para a sequência que seja maior do que 0: '))
while lim <= 0:
    lim = int(input('Limite inválido. Digite novamente: '))
a = 0
b = 1
if lim > 0:
    for x in range(0, lim):
        soma = a + b
        if x >= b - 1:
            print(b)
            a = b
            b = soma
print('Fim do programa')
