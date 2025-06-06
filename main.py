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
    return regioes[escolha]

def formatar_ocorrencia(o):
    status = o.get("status", "Em andamento")
    formatado = f"""
🆔 {o['id']}
🗺️ Região: {o['regiao']}
🔥 Severidade: {o['severidade']}
🏙️ Local: {o['local']}
📄 {o['descricao']}
📌 Status: {status}
⏰ Criado em: {o['timestamp'].strftime('%d/%m/%Y %H:%M:%S')}"""
    return formatado

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
    while True:
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
            "id": id_str,
            "regiao": regiao,
            "severidade": severidade,
            "local": local,
            "descricao": descricao,
            "timestamp": datetime.datetime.now(),
            "status": "Em andamento"
        }
        
        limpa_tela()
        print(f"Dados da ocorrência:\n{formatar_ocorrencia(ocorrencia)}\n")
        conf = forca_opcao(['s','n'], "\nDeseja confirmar os dados da ocorrência? (s/n):\n-> ")
        if conf == 's':
            break

    limpa_tela()
    print(f"\n✅ Ocorrência registrada com sucesso:\n{formatar_ocorrencia(ocorrencia)}")
    ocorrencias[id_str] = ocorrencia
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

    print("🔍 Ocorrências ativas:")
    for o in ocorrencias.values():
        print(f"{o['id']} | Severidade: {o['severidade']} | Região: {o['regiao']} | Local: {o['local']}")

    id_escolhido = input_nao_vazio("\nDigite o ID da ocorrência que deseja validar:\n-> ").upper()

    if id_escolhido in ocorrencias:
        limpa_tela()
        ocorrencia = ocorrencias.pop(id_escolhido)
        print("\n🔎 Detalhes adicionais da resolução:")
        print("-" * 20)

        vitimas_fatais = forca_opcao(['s','n'], "Houve vítimas fatais? (s/n):\n-> ").lower()
        if vitimas_fatais == 's':
            ocorrencia["vítimas_fatais"] = "Sim"
            ocorrencia["quantidade_vitimas"] = input_nao_vazio("Quantidade de vítimas fatais:\n-> ")
            ocorrencia["causa_morte"] = input_nao_vazio("Causa das mortes:\n-> ")
        else:
            ocorrencia["vítimas_fatais"] = "Não"

        ocorrencia["feridos"] = input_nao_vazio("Número de feridos (0 se nenhum):\n-> ")
        ocorrencia["área_queimada"] = input_nao_vazio("Área estimada queimada (em hectares):\n-> ")
        ocorrencia["recursos_utilizados"] = input_nao_vazio("Recursos utilizados (ex: caminhões, helicópteros, drones):\n-> ")
        ocorrencia["relato_final"] = input_nao_vazio("Relato final da equipe:\n-> ")
        ocorrencia["resolvido_em"] = datetime.datetime.now()
        ocorrencia["status"] = "Solucionado"

        historico.append(ocorrencia)
        limpa_tela()
        print(f"\n✅ Ocorrência {id_escolhido} validada com sucesso!")
        print(formatar_ocorrencia(ocorrencia))
    else:
        print("⚠️ ID não encontrado. Tente novamente.")

    retorna_menu()

def listar_historico():
    limpa_tela()
    print("📚 Histórico de Ocorrências Solucionadas:\n")

    if not historico:
        print("⛔ Nenhuma ocorrência solucionada ainda.")
    else:
        for o in historico:
            print("=" * 50)
            print(formatar_ocorrencia(o))
            if o.get("vítimas_fatais") == "Sim":
                print(f"⚰️ Vítimas Fatais: {o['quantidade_vitimas']} - Causa: {o['causa_morte']}")
            else:
                print(f"⚰️ Vítimas Fatais: Não")
            print(f"🚑 Feridos: {o['feridos']}")
            print(f"🌾 Área Queimada: {o['área_queimada']} hectares")
            print(f"🚒 Recursos Utilizados: {o['recursos_utilizados']}")
            print(f"📝 Relato Final:\n{o['relato_final']}\n")
            print(f"\n📅 Resolvido em: {o['resolvido_em'].strftime('%d/%m/%Y %H:%M:%S')}\n")
            print("=" * 50 + "\n")
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
    4) Ver histórico de ocorrências
    0) Sair
    ''')
    print("-=" * 20 + "\n")

    opcao = forca_opcao(['0','1','2','3','4'], "Escolha uma opção:\n-> ")

    if opcao == '1':
        inserir_ocorrencia()
    elif opcao == '2':
        prioridade_ocorrencia()
    elif opcao == '3':
        validar_ocorrencia()
    elif opcao == '4':
        listar_historico()
    elif opcao == '0':
        print("👋 Até logo!")

if __name__ == "__main__":
    main_queimadas()
