#Atividade02: 
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
        print(f'Venda: R$ {venda}\nDesconto R$: {desconto}\nValor Final: R$: {valor_desconto}')
    else:
        print(f'Venda: R${venda}')
        venda_total += venda

    opt = input('Deseja continuar? (s/n): ').lower().strip()
    while opt != 's' and opt != 'n':
        opt = input('Resposta inválida. Digite [s] para sim ou [n] para não: ')

print(f'Venda total foi R${venda_total:.2f} e o total de desconto foi R${desconto_total:.2f}')
