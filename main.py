import os
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

def limpa_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

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
    formatado = f"""
🆔 {o['id']}
🗺️ Região: {o['regiao']}
🔥 Severidade: {o['severidade']}
🏙️ Local: {o['local']}
📄 {o['descricao']}
⏰ {o['timestamp'].strftime('%d/%m/%Y %H:%M:%S')} """

    return (formatado)

def listar_por_severidade():
    lista = list(ocorrencias.values())
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j]['severidade'] < chave['severidade']:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

    for o in lista:
        print(f"{o['id']} | Severidade: {o['severidade']} | Região: {o['regiao']} | Local: {o['local']}")

# -------------- AÇÕES -------------- #

def inserir_ocorrencia():
    limpa_tela()
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

    local = input_nao_vazio("Insira o endereço:\n-> ")
    descricao = input_nao_vazio("Descreva a ocorrência:\n-> ")

    novo_id = len(ocorrencias) + 1
    id_str = f"OCR{novo_id:03d}"
    ocorrencia = {
        "id": f"OCR{novo_id:03d}",
        "regiao": regiao,
        "severidade": severidade,
        "local": local,
        "descricao": descricao,
        "timestamp": datetime.datetime.now()
    }

    ocorrencias[id_str] = ocorrencia
    print(f"\n✅ Ocorrência registrada com sucesso:\n{formatar_ocorrencia(ocorrencia)}"
        )
    retorna_menu()


def prioridade_ocorrencia():
    limpa_tela()
    print("❗Ocorrências por prioridade:\n")
    if not ocorrencias:
        print("⛔ Nenhuma ocorrência para atender.")
    else:
        print("=" * 45)
        listar_por_severidade()
    retorna_menu()


def validar_ocorrencia():
    limpa_tela()
    print("✅ Validação de Ocorrência:\n")

    if not ocorrencias:
        print("⛔ Nenhuma ocorrência registrada.")
        return retorna_menu()
    while True:
        print("🔍 Ocorrências ativas:")
        for o in ocorrencias.values():
            print(f"{o['id']} | Região: {o['regiao']} | Local: {o['local']} | Severidade: {o['severidade']}")

        id_escolhido = input_nao_vazio("\nDigite o ID da ocorrência que deseja validar:\n-> ").upper()

        if id_escolhido in ocorrencias:
            ocorrencia = ocorrencias.pop(id_escolhido)
            print("\n🔎 Detalhes adicionais da resolução:")

            vitimas_fatais = input_nao_vazio("Houve vítimas fatais? (Sim/Não):\n-> ").capitalize()
            feridos = input_nao_vazio("Número de feridos (0 se nenhum):\n-> ")
            area_queimada = input_nao_vazio("Área estimada queimada (em hectares):\n-> ")
            recursos = input_nao_vazio("Recursos utilizados (ex: caminhões, helicópteros, drones):\n-> ")
            relato = input_nao_vazio("Relato final da equipe:\n-> ")

            ocorrencia["resolvido_em"] = datetime.datetime.now()
            ocorrencia["vítimas_fatais"] = vitimas_fatais
            ocorrencia["feridos"] = feridos
            ocorrencia["área_queimada"] = area_queimada
            ocorrencia["recursos_utilizados"] = recursos
            ocorrencia["relato_final"] = relato

            historico.append(ocorrencia)

            print(f"\n✅ Ocorrência {id_escolhido} validada com sucesso!")
            print(formatar_ocorrencia(ocorrencia))
            break
        else:
            print("⚠️ ID não encontrado. Tente novamente.")

    retorna_menu()

# -------------- MENU PRINCIPAL -------------- #

def main_queimadas():
    limpa_tela()
    print("-=" * 20)
    print("🔥  SIMULADOR DE RESPOSTA A QUEIMADAS 🔥")
    print("-=" * 20)
    print('''
    1) Inserir nova ocorrência
    2) Listar ocorrências por severidade
    3) Validar ocorrência solucionada
    0) Sair
    ''')
    print("-=" * 20 + "\n")

    opcao = forca_opcao(['0','1','2','3','4','5','6'], "Escolha uma opção:\n-> ")

    if opcao == '1':
        inserir_ocorrencia()
    elif opcao == '2':
        prioridade_ocorrencia()
    elif opcao == '3':
        validar_ocorrencia()
    elif opcao == '0':
        print("👋 Até logo!")

if __name__ == "__main__":
    main_queimadas()