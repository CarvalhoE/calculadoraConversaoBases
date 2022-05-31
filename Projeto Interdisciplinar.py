"""
     RGM          Integrantes do Grupo
26062747 | Breno Espindola Carvalho dos Santos
26542731 | Claudio Andretta
26474263 | Guilherme da Cruz Manoel
26387417 | Guilherme Fernandes Laurindol
26299437 | Lukas Reis de Oliveira

"""

import time

resp = 's'

while(resp =='s'):
    print('''Escolha uma das bases para conversão:
    [ 1 ] converter de Hexadecimal para Decimal
    [ 2 ] converter de Octadecimal para Decimal
    [ 3 ] converter de binario para  Decimal''')

    opção = int(input('Sua opção: '))

    print('Aguarde enquanto preparamos a conversão...')

    time.sleep(4)

    if opção == 1:
        n = input('Digite o valor em Hexadecimal(16): ')
        print('Valor apresentado: ', n)

        S = 0  # Solução
        i = 0  # Contador

        print('O valor Hexadecimal(16),', n, end='  ')
        strNumber = str(n)  # Convertendo string
        for x in reversed(strNumber):  #retorna a string inversa / aplicando os numeros nas letras conforme a base hexa
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
            i = i + 1               #Expoente | mudança em cada numero
        print('em base Decimal(10) é:', S)

    elif opção == 2:
        n = int(input('Digite o valor em Octadecimal(8): '))
        print('Valor apresentado: ', n)
        S = 0
        i = 0
        print('O valor Octadecimal(8),', n, end='  ')
        while n >= 1:
            d = n % 10;
            n = int(n / 10);
            S = S + d * pow(8, i)
            i = i + 1
        print('em base Decimal(10) é:', S)

    elif opção == 3:
        n = int(input('Digite o valor em binario(2): '))
        print('Valor apresentado: ', n)
        S = 0
        i = 0  # i=0 corresponde a primeira posição da direita para esquerda
        print('O valor Binario(2),', n, end='  ')
        while n >= 1:
            d = n % 10;  # Extração do primeiro digito da direita para esquerda, n%10 > restante da divisão de n por 10
            n = int(n / 10);  # n=n//10 | aplicando a estrategia a cima á extração de cada digito
            S = S + d * pow(2, i)
            i = i + 1  # mudança de posição adicionada ao proximo numero (S) / exp
        print('em base Decimal(10) é:', S)
    else:
        print("Opção invalida, tente novamente.")

    resp=input("Deseja continuar convertendo ? [S] para sim [N] para não: ").lower()