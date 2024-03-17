from tqdm import tqdm
from time import sleep

cores = {
    'limpa': '\033[m',
    'branco': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'cinza': '\033[37m',

}

def Carregamento():
    for i in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=60):
        sleep(0.02)

def DeterminaOpçao():
    while True:
        opcao = str(input('Deseja criptografar (C) ou descriptografar (D): '))[
            0].strip().upper()
        if opcao in 'CD':
            return opcao
        else:
            print(f'{cores["vermelho"]}Opção Inválida. {cores["limpa"]}')

def DeterminaMensagem(opcao, mensagem):
    traduzido = ''
    chave = 4
    if opcao == 'D':
        chave = -4
    for letra in mensagem:
        if letra == '{' or letra == '}':
            traduzido += letra
        else:
            num = ord(letra)
            num += chave
            traduzido += chr(num)
    return traduzido

def continua():
    while True:
        continua = str(input('Deseja continuar ? S ou N: '))[0].upper().strip()
        if continua in 'SN':
            return continua
        else:
            print(f'{cores["vermelho"]}Opção Inválida. {cores["limpa"]}')

def main():
    opcao = DeterminaOpçao()
    mensagem = str(input('Digite sua frase: '))
    if opcao == 'C':
        print(f'{cores["amarelo"]}Sua frase criptografada é:{cores["limpa"]} ')
    else:
        print(
            f'{cores["amarelo"]}Sua frase descriptografada é:{cores["limpa"]} ')
    Carregamento()
    print(f'{cores["azul"]}{DeterminaMensagem(opcao, mensagem)}{cores["limpa"]}')
    if continua() == 'S':
        main()
    else:
        print(f'{cores["vermelho"]}Fim do programa!{cores["limpa"]}')

main()
