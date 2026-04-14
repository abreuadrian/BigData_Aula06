#Ex01: Estrutura de repetição (for e while)
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
