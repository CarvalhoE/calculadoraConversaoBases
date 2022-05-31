n = int(input('Digite o valor em binario(2): '))
print('Valor apresentado: ',n)
S = 0
i = 0 #i=0 corresponde a primeira posição da direita para esquerda
print('O valor Binario(2),',n,end='  ')
while n >= 1:
    d = n % 10; #Extração do primeiro digito da direita para esquerda, n%10 > restante da divisão de n por 10
    n = int(n/10); #n=n//10 | aplicando a estrategia a cima á extração de cada digito
    S = S+d*pow(2,i)
    i = i+1 # mudança de posição adicionada ao proximo numero (S) / exp
print('em base Decimal(10) é:',S)