# 🔥 **Simulador de Resposta a Queimadas - Global Solution**

Este projeto é uma aplicação em Python desenvolvida como parte de um desafio acadêmico para modelar e simular a resposta a incêndios florestais. A solução busca explorar estruturas de dados e algoritmos estudados na disciplina, com foco em **coordenação de ocorrências, priorização por severidade e histórico de ações**.

<br>

## 🤵 **Integrantes**

| Nome                                | RM       |
|-------------------------------------|----------|
| Bruna da Costa Candeias             | 558938   |
| Lucas Derenze Simidu                | 555931   |
| Marcos Vinicius da Silva Costa      | 555490   |

<br>

## 🔗 **Repositório no GitHub**

### *O código-fonte completo está disponível no GitHub: [👉 Acesse o repositório aqui](https://github.com/ldsimidu/gs_dynamic)*

---

<br>

## 💻 **Execução**

Para executar o projeto:

```bash
python main.py
```

## 🎯 **Objetivo**

Desenvolver um sistema de apoio à resposta rápida a queimadas, permitindo:

- Inserção de novas ocorrências
- Atendimento priorizado por severidade
- Registro detalhado de ações realizadas
- Listagem de histórico da equipe
- Simulação automática de ocorrências
- Visualização da conectividade entre regiões

<br>

## 🧠 **Conceitos Aplicados**

O projeto utiliza **100% do Conjunto 3** e também incorpora estruturas do **Conjunto 4**:

### ✅ Conjunto 3 – *Totalmente Utilizado*
- **Análise de Algoritmos / Notação O**: Aplicada na ordenação por severidade e busca binária por ID.
- **Busca Binária**: Para localizar ocorrências rapidamente com base no identificador.
- **Dicionários**: Utilizados para armazenar ocorrências e histórico com acesso rápido.

### ✅ Conjunto 4 – *Complementar*
- **Grafos**: Representação das conexões entre regiões para ilustrar caminhos possíveis de deslocamento das equipes.

<br>

## 🧩 **Funcionalidades**

### 1. Inserir Nova Ocorrência
Permite o registro manual de uma ocorrência com dados como severidade, localização e descrição.

### 2. Listar Ocorrências por Severidade
As ocorrências ativas são ordenadas pela gravidade do incêndio (implementação de ordenação baseada em inserção).

### 3. Validar Ocorrência Solucionada
Remove a ocorrência da lista ativa, solicita detalhes do atendimento (vítimas, área queimada, recursos usados) e armazena no histórico.

### 4. Ver Histórico de Ocorrências
Mostra todas as ocorrências solucionadas com seus respectivos detalhes operacionais e humanos.

### 5. Simular Ocorrências Aleatórias
Gera ocorrências automaticamente com severidade crescente e distribuição regional aleatória.

### 6. Mostrar Grafo de Regiões
Exibe a conectividade entre regiões geográficas, representando possíveis rotas de deslocamento.

<br>

## 🧱 **Estruturas de Dados Utilizadas**

| Estrutura       | Uso Principal                                              |
|------------------|------------------------------------------------------------|
| `dict`           | Armazenamento rápido de ocorrências e histórico           |
| `list`           | Ordenação por severidade e histórico de validações        |
| `heapq` (previsto)| Priorização (não usada diretamente, mas poderia expandir) |
| `deque`          | Ideal para controle de chamadas em FIFO (não usada aqui)  |
| `grafo (dict)`   | Representação das conexões entre regiões geográficas      |

<br>

## 📊 **Simulações e Algoritmos**

- **Busca Binária**: Rápida localização de ocorrências pelo ID.
- **Ordenação por Inserção**: Organiza ocorrências com base na severidade.
- **Simulação Automática**: Geração de dados para testes funcionais do sistema.
- **Visualização de Grafo**: Conexões de deslocamento entre regiões.


