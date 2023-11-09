from datetime import datetime
import sys

def notas_maior_valor(valor):
    contador = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}
    if valor > 100:
        while valor >= 100:
            contador[100] += 1
            valor -= 100
    if valor > 50:
        while valor >= 50:
            contador[50] += 1
            valor -= 50
    if valor > 20:
        while valor >= 20:
            contador[20] += 1
            valor -= 20
    if valor > 10:
        while valor >= 10:
            contador[10] += 1
            valor -= 10
    if valor > 5:
        while valor >= 5:
            contador[5] += 1
            valor -= 5
    if valor > 2:
        while valor >= 2:
            contador[2] += 1
            valor -= 2
    for nota, contador_nota in contador.items():
        if contador_nota > 1:
            print(f'{contador_nota} x {nota} reais')
    confirmacao = input(f'Deseja continuar com a operação? [s/n]: ')
    if confirmacao == 's':
        return contador
    else:
        print('Operação cancelada.')
        raise SystemExit(1)

def notas_menor_valor(valor):
    contador = {20:0, 10:0, 5:0, 2:0}
    if valor > 20:
        while valor >= 20:
            contador[20] += 1
            valor -= 20
    if valor > 10:
        while valor >= 10:
            contador[10] += 1
            valor -= 10
    if valor > 5:
        while valor >= 5:
            contador[5] += 1
            valor -= 5
    if valor > 2:
        while valor >= 2:
            contador[2] += 1
            valor -= 2
    for nota, contador_nota in contador.items():
        if contador_nota > 1:
            print(f'{contador_nota} x {nota} reais')
    confirmacao = input(f'Deseja continuar com a operação? [s/n]: ')
    if confirmacao == 's':
        return contador
    else:
        print('Operação cancelada.')
        raise SystemExit(1)

def notas_meio_a_meio(valor):
    contador_principal = notas_maior_valor(valor/2)
    contador_auxiliar = notas_menor_valor(valor/2)
    for nota in contador_auxiliar:
        contador_principal[nota] += contador_auxiliar[nota]
    for nota, contador_nota in contador.items():
        if contador_nota > 1:
            print(f'{contador_nota} x {nota} reais')
    confirmacao = input(f'Deseja continuar com a operação? [s/n]: ')
    if confirmacao == 's':
        return contador_principal
    else:
        print('Operação cancelada.')
        raise SystemExit(1)

def requisitos_minimos(data):
    data_atual = datetime.now()
    while True:
        try:
            data = datetime.strptime(data, '%d/%m/%Y')
            if data_atual.year - data.year > 5:
                return data
            else:
                print('Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.')
                raise SystemExit(1)
            break
        except:
            data = input('Data inválida, digite no formato dia/mês/ano: ')

def validar_emprestimo(valor, salario):
    while valor % 2 != 0 or valor > salario * 2:
        valor = float(input('Valor inválido, ele precisa ser multiplo de dois e não pode exceder o dobro do salário: '))
    return valor

def opcoes_retirada(valor_emprestimo):
    print('Opções de retirada:\n1. Notas de maior valor\n2. Notas de menor valor\n3. Notas meio a meio')
    while True:
        try:
            selecao = int(input('Selecione uma opção: '))
            if selecao == 1:
                return notas_maior_valor(valor_emprestimo)
            elif selecao == 2:
                return notas_menor_valor(valor_emprestimo)
            elif selecao == 3:
                return notas_meio_a_meio(valor_emprestimo)
            else:
                print('Opção inválida, Digite o número correspondente a opção.')
        except:
            print('Opção inválida, Digite o número correspondente a opção.')

def main():
    nome = input('Nome completo: ')
    data_admissao = requisitos_minimos(input('Data de admissão (dia/mês/ano): '))
    salario_atual = float(input('Salário atual: '))
    valor_emprestimo = validar_emprestimo(float(input('Valor de empréstimo: ')), salario_atual)
    retirada = opcoes_retirada(valor_emprestimo)
main()