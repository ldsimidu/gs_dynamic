import datetime

dia_hoje = datetime.date.today()
ocorrencias = {}
historico = []


# -------------- FUNÇÕES DE UTILIDADE -------------- #

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

def retorna_menu():
    input("\n◀️ Pressione ENTER para voltar ao menu...")
    main_queimadas()


# -------------- VISUALIZAÇÃO -------------- #

def escolher_regiao():
    regioes = {
        "1": "Norte",
        "2": "Sul",
        "3": "Leste",
        "4": "Oeste",
        "5": "Centro"
    }
    mensagem = (
        "Informe a região da ocorrência:\n"
        "1) Norte\n"
        "2) Sul\n"
        "3) Leste\n"
        "4) Oeste\n"
        "5) Centro\n"
        "-> "
    )

    escolha = forca_opcao(list(regioes.keys()), mensagem)
    regiao_escolhida = regioes[escolha]
    return regiao_escolhida

def formatar_ocorrencia(o):
    x = ("=" * 20)
    formatado = f"""
{x}
🆔 {o['id']}
🗺️ Região: {o['regiao']}
🔥 Severidade: {o['severidade']}
📄 {o['descricao']}
⏰ {o['timestamp'].strftime('%d/%m/%Y %H:%M:%S')} """

    return (formatado)


# -------------- AÇÕES -------------- #

def inserir_ocorrencia():
    print("📌 Inserir Nova Ocorrência:")
    
    regiao = escolher_regiao()
    
    while True:
        try:
            severidade = int(forca_opcao(['1','2','3','4','5'], "Informe a severidade (1 a 5):\n-> ").strip())
            if severidade < 1 or severidade > 5:
                raise ValueError("Severidade fora do intervalo permitido.")
        except ValueError as e:
            print(f"⚠️ Valor inválido ({e}). Digite um número entre 1 e 5.\n")
        else:
            break

    descricao = input_nao_vazio("Descreva a ocorrência:\n-> ")

    novo_id = len(ocorrencias) + 1
    id_str = f"OCR{novo_id:03d}"
    ocorrencia = {
        "id": f"OCR{novo_id:03d}",
        "regiao": regiao,
        "severidade": severidade,
        "descricao": descricao,
        "timestamp": datetime.datetime.now()
    }

    ocorrencias[id_str] = ocorrencia
    print(f"\n✅ Ocorrência registrada com sucesso:\n{formatar_ocorrencia(ocorrencia)}"
        )
    retorna_menu()


# -------------- MENU PRINCIPAL -------------- #

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
        inserir_ocorrencia()
    elif opcao == '2':
        print("opc2")
    elif opcao == '3':
        print("opc3")
    elif opcao == '0':
        print("👋 Até logo!")

if __name__ == "__main__":
    main_queimadas()