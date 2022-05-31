resp = 's'

while(resp =='s'):
    print('''Escolha uma das bases para conversão:
    [ 1 ] converter de Hexadecimal para Decimal
    [ 2 ] converter de Octadecimal para Decimal
    [ 3 ] converter de binario para  Decimal''')

    opção = int(input('Sua opção: '))

    if opção == 1:
        # inicializando a string
        string = input('Digite o valor em Hexadecimal(16): ')
        # printando a string original
        print("Valor apresentado: " + str(string))
        # uso de int convertendo hexa para decimal
        res = int(string, 16)
        # O segundo argumento na função de número inteiro, "16" diz ao Python que é uma base dezesseis(Hexa)
        # resultado
        print("O valor Hexadecimal(16) em base Decimal(10) é: " + str(res))

    elif opção == 2:
        # inicializando a string
        string = input('Digite o valor em Octadecimal(8): ')
        # printando a string original
        print("Valor apresentado: " + str(string))
        # uso de int convertendo hexa para decimal
        res = int(string, 8)
        # O segundo argumento na função de número inteiro, "8" diz ao Python que é uma base oito(Octa)
        # resultado
        print("O valor Octadecimal(8) em base Decimal(10) é: " + str(res))

    elif opção == 3:
        # inicializando a string
        string = input('Digite o valor em binario(2): ')
        # printando a string original
        print("Valor apresentado: " + str(string))
        # uso de int convertendo hexa para decimal
        res = int(string, 2)
        # O segundo argumento na função de número inteiro, "2" diz ao Python que é uma base dois(Binario)
        # resultado
        print("O valor Binario(2) em base Decimal(10) é: " + str(res))
    else:
        print("Opção invalida, tente novamente.")

    resp=input("Deseja continuar convertendo ? [S] para sim [N] para não: ").lower()