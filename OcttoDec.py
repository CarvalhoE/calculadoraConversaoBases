n = int(input('Digite o valor em Octadecimal(8): '))
print('Valor apresentado: ',n)
S = 0
i = 0
print('O valor Octadecimal(8),',n,end='  ')
while n >= 1:
    d = n % 10;
    n = int(n/10);
    S = S+d*pow(8,i)
    i = i+1
print('em base Decimal(10) é:',S)