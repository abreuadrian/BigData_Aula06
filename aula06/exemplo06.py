#Ex01: Estrutura de repetição: (for)
def ex01():
    start = int(input('Informe o número de inicio: '))      
    finish = int(input('Informe o número final: '))         
    inte = int(input('Informe o intervalo: '))
    for i in range(start, finish+1, inte):                  #range(começo, final, intervalo)
        print(i, end = " ")                                 #end = " " imprime na mesma linha

#Ex02: 
def ex02():
    for i in range (3):
        print(f'\n{i+1}ª rodada')
        n1 = int(input('Informe o número: '))
        n2 = int(input('Informe o segundo número: '))
        soma = n1 + n2
        print(f'O total é {soma}')

#Ex03: Variável Acumuladora
def ex03():
    x = 0 
    for i in range(5):
        num = float(input('Informe o valor de n: '))
        x += num
    print(f'O total é {x}')

#Ex04: soma valores >= 100
def ex04 ():
    total = 0
    for i in range(5):
        n = int(input('Informe um número: '))
        if n >= 100:
            total += n
            print(f'Valor [{n}] somado ✅') 
        else: print(f'Valor [{n}] não computado ❌')
    print(total)

#Ex05: Estrutura de repetição: (while)
def ex05():
    password = '0000'
    leitura = ''

    while password != leitura:
        leitura = input('Digite sua senha: ')
        if leitura == password:
            print('Acesso liberado')
        else:
            print('Senha Incorreta. Tente novamente.')

#Ex06: Números até 10
def ex06():
    i = 1
    while i <= 10:
        print(i)
        i += 1

#Ex07: soma com opção para parar 
def ex07():
    n = 1
    soma = 0 
    while n != 0:
        n = int(input('Digite um número (0 para parar): '))
        soma += n 
    print(f'\nSoma total foi {soma}')

#Ex08: 
def ex08():
    res = 's'
    soma = 0
    while res != 'n':
        n = int(input('Informe um número: '))    
        soma += n
        res = input('Deseja continuar (s/n): ').lower().strip()
    print(f'\n A soma total foi {soma}')