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
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')  # sempre que encontrar um \n vira um item inteiro da lista
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')  # Quebra os itens da lista em ','
        print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4  # converte para inteiro e divede por 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/dev/dio/notas_alunos')


def


if __name__ == '__main__':
    copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira Linha\n')
    # aluno = 'Daniel, 10, 10, 5, 5'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
