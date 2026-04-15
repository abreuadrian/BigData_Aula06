#Atividade02: 
import os
import time
venda_total = 0
opt = 's'
desconto_total =0 

while opt != 'n':
    while True:
        try:
            venda = float(input('Informe o valor da venda: R$'))
            break
        except ValueError:
            print('ERRO. Informe o valor da venda.')
            time.sleep(1)
            os.system('cls')
    if venda > 1000:
        desconto = venda * 0.10
        desconto_total += desconto
        valor_desconto = venda - (venda * 0.10)
        venda_total += valor_desconto
    else:
        venda_total += venda
    time.sleep(0.5)
    os.system('cls')
    opt = input('Deseja continuar? (s/n): ').lower().strip()
    while opt != 's' and opt != 'n':
        opt = input('Respostá inválida. Digite [s] para sim ou [n] para não: ')
        time.sleep(0.5)
        os.system('cls')

print(f'Venda total foi R${venda_total:.2f} e o total de desconto foi R${desconto_total:.2f}')
