import random

def cifra_de_cesar(texto, chave):
    texto_cifrado = ""
    for caractere in texto:
        if caractere.isalpha():
            deslocamento = ord('A') if caractere.isupper() else ord('a')
            texto_cifrado += chr((ord(caractere) - deslocamento + chave) % 26 + deslocamento)
        else:
            texto_cifrado += caractere
    return texto_cifrado

def cifra_de_substituicao(texto, chave):
    random.seed(chave)
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alfabeto_embaralhado = ''.join(random.sample(alfabeto, len(alfabeto)))
    tabela_substituicao = str.maketrans(alfabeto, alfabeto_embaralhado)
    return texto.translate(tabela_substituicao)

def cifra_xor(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char = texto[i]
        chave_char = chave[i % len(chave)]
        texto_cifrado += chr(ord(char) ^ ord(chave_char))
    return texto_cifrado

chave_secreta = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"

senha1 = input('Digite a 1° senha: ')
senha1_criptografada = cifra_de_cesar(senha1, len(chave_secreta))
print(f'1° senha cifrada: {senha1_criptografada}')

senha2 = input('Digite a 2° senha: ')
senha2_criptografada = cifra_de_substituicao(senha2, chave_secreta)
print(f'2° senha cifrada: {senha2_criptografada}')

senha3 = input('Digite a 3° senha: ')
senha3_criptografada = cifra_xor(senha3, chave_secreta)
print(f'3° senha cifrada: {senha3_criptografada}')

