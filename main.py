def input_nao_vazio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto == "":
            print("⚠️ Entrada vazia. Tente novamente.")
        else:
            return texto

def forca_opcao(lista, mensagem):
    while True:
        escolha = input_nao_vazio(mensagem)
        if escolha not in lista:
            print("⚠️ Opção inválida. Tente novamente.")
        else:
            return escolha

def main_queimadas():
    print("-=" * 20)
    print("🔥  SIMULADOR DE RESPOSTA A QUEIMADAS 🔥")
    print("-=" * 20)
    print('''
    1) Inserir nova ocorrência
    2) Atender próxima ocorrência prioritária
    3) Listar ocorrências pendentes
    0) Sair
    ''')
    print("-=" * 20 + "\n")

    opcao = forca_opcao(['0','1','2','3','4','5','6'], "Escolha uma opção:\n-> ")

    if opcao == '1':
        print("opc1")
    elif opcao == '2':
        print("opc2")
    elif opcao == '3':
        print("opc3")
    elif opcao == '0':
        print("👋 Até logo!")

if __name__ == "__main__":
    main_queimadas()