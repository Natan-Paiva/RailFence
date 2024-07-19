import sys
def criptografa(texto, chave):
    if chave == 1:
        return texto # Se a chave for 1, retorna o texto sem modificações

    rail = [['' for _ in range(len(texto))] for _ in range(chave)] #Cria uma matriz vazia
    dir_baixo = False #Variável para controle de direção
    linha, col = 0, 0 #Variável para controle de posição na matriz

    #Preenche a matriz com os caracteres do texto fazendo um zig-zag
    for char in texto:
        if linha == 0 or linha == chave - 1:
            dir_baixo = not dir_baixo

        rail[linha][col] = char
        col += 1

        if dir_baixo:
            linha += 1
        else:
            linha -= 1

    #Controi o texto criptografado
    resultado = []
    for i in range(chave):
        for j in range(len(texto)):
            if rail[i][j] != '':
                resultado.append(rail[i][j])
    return "".join(resultado)


def descriptografa(cifra, chave):
    if chave == 1:
        return cifra

    rail = [['' for _ in range(len(cifra))] for _ in range(chave)]
    dir_baixo = None
    linha, col = 0, 0

    for i in range(len(cifra)):
        if linha == 0 or linha == chave - 1:
            dir_baixo = not dir_baixo

        rail[linha][col] = '*'  #Marca o trilho com um asterisco
        col += 1

        if dir_baixo:
            linha += 1
        else:
            linha -= 1

    #Substitui os asteriscos pelos caracteres da cifra
    index = 0
    for i in range(chave):
        for j in range(len(cifra)):
            if rail[i][j] == '*' and index < len(cifra):
                rail[i][j] = cifra[index]
                index += 1

    resultado = []
    for j in range(len(cifra)):
        for i in range(chave):
            if rail[i][j] != '*':
                resultado.append(rail[i][j])

    return "".join(resultado)

def main():
    if len(sys.argv) != 4: #Verifica se o número de arugmentos passados está correto
        print("Instrução de uso: python <script> <arquivo.txt> <chave> <modo>")
        print("<modos>: criptografar or descriptografar")
        return

    file_path = sys.argv[1]
    chave = int(sys.argv[2])
    modo = sys.argv[3]

    try:
        with open(file_path, 'r') as file:
            conteudo = file.read()

        if modo == 'criptografar':
            resultado = criptografa(conteudo, chave)
            output_path = file_path.replace('.txt', '_cripto.txt')
        elif modo == 'descriptografar':
            resultado = descriptografa(conteudo, chave)
            output_path = file_path.replace('_cripto.txt', '_decripto.txt')
        else:
            print("Opção inválida, escolha 'criptografar' or 'descriptografar'")
            return

        with open(output_path, 'w') as output_file:
            output_file.write(resultado)

        print(f"Operação bem sucedida. Arquivo salvo em {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()