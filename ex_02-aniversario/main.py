from datetime import datetime

data_atual = datetime.now().month

def ler_lista_de_consultores():
    with open('dados_consultores.txt', 'r') as arquivo:
        return arquivo.readlines()

def gerar_arquivo_aniversariantes_do_mes(lista):
    with open('consultores_aniversariantes_do_mes.txt', 'w') as arquivo:
        for indice in texto:
            indice = indice.strip('\n')
            indice = indice.split('|')
            if datetime.strptime(indice[2], '%d/%m/%Y').month == data_atual:
                arquivo.write(f'{indice[0]}|{indice[1]}|{indice[2]}\n')
        
opcao = input('Gostaria de gerar o arquivo de aniversariantes do mês? [S/N]: ')
while True:
    if opcao in ['S', 's']:
        texto = ler_lista_de_consultores()
        gerar_arquivo_aniversariantes_do_mes(texto)
        print('Gerado relatório consultores_aniversariantes_do_mes.txt')
        break
    elif opcao in ['N', 'n']:
        print('Finalizando programa...')
        break
    else:
        opcao = input('Opção inválida! Gostaria de gerar o arquivo de aniversariantes do mês? [S/N]: ')