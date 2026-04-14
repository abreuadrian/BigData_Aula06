#Aividade01: 4 notas por aluno e calcular a média
import time
import os
def calc_med(y):
    med_list = []
    for i in range(y):
        nota_list = []
        for n in range(4):
            while True:
                try:
                    nota = float(input(f'Informe a {n+1}ª nota: '))
                    if nota > 10 or nota < 0:
                        print('Erro. Insira um nota válida')
                    else: 
                        break
                except ValueError:
                    print('\nERRO. Informe um número inteiro')
            nota_list.append(nota)
        med = sum(nota_list) / 4
        med_list.append(med)
    for q in range(qnt_alunos):
        print('')
        print(f'Média do {q+1}º aluno: {med_list[q]}')

while True:
        try:
            qnt_alunos = int(input('Informe a quantidade de alunos: '))
            os.system('cls')
            break
        except ValueError:
            print('\nERRO. Informe um número inteiro')
calc_med(qnt_alunos)
