n = input('Digite o valor em Hexadecimal(16): ')
print('Valor apresentado: ', n)

S = 0  # Solução
i = 0  # Contador

print('O valor Hexadecimal(16),', n, end='  ')
strNumber = str(n) #Convertendo string
for x in reversed(strNumber): #retorna a string inversa / aplicando os numeros nas letras conforme a base hexa
    if x == "A" or x == "a":
        x = 10
    elif x == "B" or x == "b":
        x = 11
    elif x == "C" or x == "c":
        x = 12
    elif x == "D" or x == "d":
        x = 13
    elif x == "E" or x == "e":
        x = 14
    elif x == "F" or x == "f":
        x = 15
    C = int(x) * pow(16, i) #formula, C = int(x) informando que a var x fica um valor int após o processo dos elifs
    S = S + C               # pow(16,i) * 16 ^ i | i sendo expoente.  S = S + C, Solução + Calculo
    i = i + 1 #Expoente | mudança em cada numero
print('em base Decimal(10) é:', S)
