def escrever_arquivo(texto):
    diretorio = 'C:/dev/dio/teste.txt'
    arquivo = open(diretorio, 'w')  # o 'w' escreve na primeira vez e sobrescreve nas outras vezes.
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')  # O 'a' atualiza sem sobrescrever.
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivos):
    arquivo = open(nome_arquivos, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')  # sempre que encontrar um \n vira um item inteiro da lista
    for x in aluno_nota:
        print(x)


if __name__ == '__main__':
    media_notas('notas.txt')
    # escrever_arquivo('Primeira Linha\n')
    # aluno = 'Daniel, 10, 10, 5, 5'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
