# -*- coding: utf-8 -*-
"""
Script Python Aprimorado para Controle de Estoque Hospitalar

Este script gerencia um estoque hospitalar utilizando uma lista de dicionários.
Inclui funcionalidades para adicionar, buscar (com busca binária após ordenação),
ler, atualizar e remover insumos. Também demonstra a construção de um grafo
com NetworkX para analisar o estoque por local e identificar itens acima ou
abaixo da quantidade ideal.

Melhorias aplicadas:
- Correção da lógica de ordenação (Merge Sort) e sua aplicação.
- Correção de nome e erro de acesso em `ler_insumo`.
- Otimização da busca binária.
- Remoção de chamadas `time.sleep` das funções principais.
- Reordenação automática da lista após adição/remoção para manter a
  consistência da busca binária.
- Estruturação do código com separação de dados, funções e bloco de execução.
- Adição de docstrings e type hints.
- Correção de nome da função `ordernar_insumos` para `ordenar_insumos`.
- Movida a análise de grafo para o bloco de exemplo.
"""

import networkx as nx
from typing import List, Dict, Any, Tuple, Optional

# --- Estrutura de Dados Inicial ---
estoque_hospitalar: Dict[str, List[Dict[str, Any]]] = {
    "insumos": [
        {
            "nome": "Seringas",
            "local": "Depósito A",
            "quantidade_atual": 150,
            "quantidade_ideal": 200,
            "unidade": "unidades"
        },
        {
            "nome": "Luvas",
            "local": "Depósito B",
            "quantidade_atual": 300,
            "quantidade_ideal": 500,
            "unidade": "pares"
        },
        {
            "nome": "Máscaras",
            "local": "Depósito C",
            "quantidade_atual": 100,
            "quantidade_ideal": 250,
            "unidade": "unidades"
        },
        {
            "nome": "Ataduras",
            "local": "Depósito D",
            "quantidade_atual": 75,
            "quantidade_ideal": 100,
            "unidade": "rolos"
        },
        {
            "nome": "Álcool em gel",
            "local": "Depósito A",
            "quantidade_atual": 50,
            "quantidade_ideal": 120,
            "unidade": "litros"
        },
        {
            "nome": "Termômetros",
            "local": "Depósito B",
            "quantidade_atual": 20,
            "quantidade_ideal": 40,
            "unidade": "unidades"
        },
        {
            "nome": "Agulhas",
            "local": "Depósito C",
            "quantidade_atual": 550,
            "quantidade_ideal": 500,
            "unidade": "unidades"
        }
    ]
}

# --- Funções de Gerenciamento de Estoque ---

def ordenar_insumos(lista: List[Dict[str, Any]], chave: str = "nome") -> None:
    """
    Ordena uma lista de dicionários de insumos in-place usando Merge Sort.

    Args:
        lista (List[Dict[str, Any]]): A lista de insumos a ser ordenada.
        chave (str, optional): A chave do dicionário pela qual ordenar.
                               Defaults to "nome".

    Complexity:
        O(N log N), onde N é o número de insumos.
    """
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Chamadas recursivas (passando cópias)
        ordenar_insumos(esquerda, chave)
        ordenar_insumos(direita, chave)

        # Merge
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][chave] < direita[j][chave]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def buscar_insumo(lista_ordenada: List[Dict[str, Any]], nome: str) -> Tuple[Optional[Dict[str, Any]], Optional[int]]:
    """
    Busca um insumo pelo nome em uma lista *ordenada* usando busca binária.

    Args:
        lista_ordenada (List[Dict[str, Any]]): A lista de insumos, 
                                                **obrigatoriamente ordenada por nome**.
        nome (str): O nome do insumo a ser buscado.

    Returns:
        Tuple[Optional[Dict[str, Any]], Optional[int]]: Uma tupla contendo o 
            dicionário do insumo encontrado e seu índice na lista, ou (None, None)
            se não for encontrado.

    Complexity:
        O(log N), onde N é o número de insumos.
    """
    esquerda, direita = 0, len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        nome_meio = lista_ordenada[meio]["nome"]

        if nome_meio == nome:
            return lista_ordenada[meio], meio
        elif nome_meio < nome:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None, None # Insumo não encontrado

def adicionar_insumo(estoque: Dict[str, List[Dict[str, Any]]], nome: str, local: str, quantidade_atual: int, quantidade_ideal: int, unidade: str) -> None:
    """
    Adiciona um novo insumo à lista de estoque e reordena a lista.

    Args:
        estoque (Dict[str, List[Dict[str, Any]]]): O dicionário principal do estoque.
        nome (str): Nome do novo insumo.
        local (str): Local do novo insumo.
        quantidade_atual (int): Quantidade atual do novo insumo.
        quantidade_ideal (int): Quantidade ideal do novo insumo.
        unidade (str): Unidade de medida do novo insumo.
    """
    # Verifica se o insumo já existe (opcional, mas recomendado)
    insumo_existente, _ = buscar_insumo(estoque["insumos"], nome)
    if insumo_existente:
        print(f"Erro: Insumo '{nome}' já existe no estoque. Use a função de atualização.")
        return

    novo_insumo = {
        "nome": nome,
        "local": local,
        "quantidade_atual": quantidade_atual,
        "quantidade_ideal": quantidade_ideal,
        "unidade": unidade
    }
    estoque["insumos"].append(novo_insumo)
    ordenar_insumos(estoque["insumos"]) # Reordena após adicionar
    print(f"Insumo '{nome}' adicionado com sucesso e estoque reordenado.")

def ler_insumo(estoque: Dict[str, List[Dict[str, Any]]], nome: str) -> None:
    """
    Exibe os detalhes de um insumo específico ou de todos os insumos.

    Args:
        estoque (Dict[str, List[Dict[str, Any]]]): O dicionário principal do estoque.
        nome (str): O nome do insumo a ser lido, ou "todos" para listar todos.
    """
    if nome.lower() == "todos":
        print("\n--- Listando Todos os Insumos ---")
        if not estoque["insumos"]:
            print("Estoque vazio.")
            return
        for insumo in estoque["insumos"]:
            print(f"  Insumo: {insumo['nome']}")
            print(f"  Local: {insumo['local']}")
            print(f"  Quantidade Atual: {insumo['quantidade_atual']} {insumo['unidade']}")
            print(f"  Quantidade Ideal: {insumo['quantidade_ideal']} {insumo['unidade']}")
            print("  " + "-"*20)
        print("--- Fim da Lista ---")
        return

    print(f"\nBuscando insumo '{nome}'...")
    # Garante que a lista está ordenada antes da busca
    # ordenar_insumos(estoque["insumos"]) # Descomente se a ordenação não for garantida em outros pontos
    insumo_encontrado, _ = buscar_insumo(estoque["insumos"], nome)

    if insumo_encontrado:
        print("--- Detalhes do Insumo ---")
        print(f"  Insumo: {insumo_encontrado['nome']}")
        print(f"  Local: {insumo_encontrado['local']}")
        print(f"  Quantidade Atual: {insumo_encontrado['quantidade_atual']} {insumo_encontrado['unidade']}")
        print(f"  Quantidade Ideal: {insumo_encontrado['quantidade_ideal']} {insumo_encontrado['unidade']}")
        print("-------------------------")
    else:
        print(f"Insumo '{nome}' não encontrado.")

def atualizar_quantidade(estoque: Dict[str, List[Dict[str, Any]]], nome: str, nova_quantidade: int) -> None:
    """
    Atualiza a quantidade atual de um insumo específico.

    Args:
        estoque (Dict[str, List[Dict[str, Any]]]): O dicionário principal do estoque.
        nome (str): O nome do insumo a ser atualizado.
        nova_quantidade (int): A nova quantidade atual.
    """
    # Garante que a lista está ordenada antes da busca
    # ordenar_insumos(estoque["insumos"]) # Descomente se a ordenação não for garantida
    insumo, index = buscar_insumo(estoque["insumos"], nome)
    if insumo is not None and index is not None:
        estoque["insumos"][index]["quantidade_atual"] = nova_quantidade
        print(f"Quantidade do insumo '{nome}' atualizada para {nova_quantidade}.")
    else:
        print(f"Erro: Insumo '{nome}' não encontrado para atualização.")

def remover_insumo(estoque: Dict[str, List[Dict[str, Any]]], nome: str) -> None:
    """
    Remove um insumo do estoque e reordena a lista.

    Args:
        estoque (Dict[str, List[Dict[str, Any]]]): O dicionário principal do estoque.
        nome (str): O nome do insumo a ser removido.
    """
    # Garante que a lista está ordenada antes da busca
    # ordenar_insumos(estoque["insumos"]) # Descomente se a ordenação não for garantida
    insumo, index = buscar_insumo(estoque["insumos"], nome)
    if insumo is not None and index is not None:
        estoque["insumos"].pop(index)
        # A lista permanece ordenada após remover um item, não precisa reordenar aqui.
        # Se a adição não reordenasse, seria necessário reordenar aqui também.
        print(f"Insumo '{nome}' removido com sucesso.")
        # Se a busca binária não fosse usada ou a ordem não importasse, a reordenação seria desnecessária.
    else:
        print(f"Erro: Insumo '{nome}' não encontrado para remoção.")

# --- Funções de Análise com Grafo ---

def construir_grafo_por_local(insumos: List[Dict[str, Any]]) -> nx.Graph:
    """
    Constrói um grafo NetworkX onde os nós são insumos e as arestas conectam
    insumos que estão no mesmo local.

    Args:
        insumos (List[Dict[str, Any]]): A lista de dicionários de insumos.

    Returns:
        nx.Graph: O grafo construído.
    """
    G = nx.Graph()
    if not insumos:
        return G

    # Adiciona nós com atributos
    for insumo in insumos:
        nome_no = insumo["nome"] # Usar nome como identificador único do nó
        G.add_node(nome_no,
                   local=insumo["local"],
                   atual=insumo["quantidade_atual"],
                   ideal=insumo["quantidade_ideal"],
                   unidade=insumo["unidade"])

    # Adiciona arestas entre insumos no mesmo local
    locais = {} # Dicionário para agrupar insumos por local
    for i, insumo in enumerate(insumos):
        local = insumo["local"]
        if local not in locais:
            locais[local] = []
        locais[local].append(insumo["nome"])

    # Cria arestas dentro de cada grupo de local
    for local, nomes_insumos in locais.items():
        # Conecta todos os pares de insumos no mesmo local
        for i in range(len(nomes_insumos)):
            for j in range(i + 1, len(nomes_insumos)):
                G.add_edge(nomes_insumos[i], nomes_insumos[j], local=local)

    return G

def analisar_estoque_grafo(grafo: nx.Graph) -> Tuple[List[Tuple[str, int, int]], List[Tuple[str, int, int]]]:
    """
    Analisa o grafo de estoque para encontrar produtos abaixo e acima do ideal.

    Args:
        grafo (nx.Graph): O grafo de estoque construído por `construir_grafo_por_local`.

    Returns:
        Tuple[List[Tuple[str, int, int]], List[Tuple[str, int, int]]]: Uma tupla contendo:
            - Lista de produtos abaixo do ideal: (nome, atual, ideal)
            - Lista de produtos acima do ideal: (nome, atual, ideal)
    """
    abaixo_ideal = []
    acima_ideal = []
    for no, dados in grafo.nodes(data=True):
        if not all(k in dados for k in ('atual', 'ideal')):
            continue # Pula nós sem os dados necessários
        if dados["atual"] < dados["ideal"]:
            abaixo_ideal.append((no, dados["atual"], dados["ideal"]))
        elif dados["atual"] > dados["ideal"]:
            acima_ideal.append((no, dados["atual"], dados["ideal"]))
    return abaixo_ideal, acima_ideal

# --- Bloco de Execução Principal (Exemplo de Uso) ---
if __name__ == "__main__":
    print("--- Sistema de Gerenciamento de Estoque Hospitalar ---")

    # 1. Ordenar o estoque inicial (necessário para busca binária)
    print("\nOrdenando estoque inicial...")
    ordenar_insumos(estoque_hospitalar["insumos"])
    print("Estoque ordenado por nome.")

    # 2. Ler todos os insumos
    ler_insumo(estoque_hospitalar, "todos")

    # 3. Buscar um insumo específico
    ler_insumo(estoque_hospitalar, "Luvas")
    ler_insumo(estoque_hospitalar, "Gazes") # Exemplo de insumo não existente

    # 4. Adicionar um novo insumo
    print("\nAdicionando novo insumo...")
    adicionar_insumo(estoque_hospitalar, "Gazes", "Depósito A", 50, 150, "pacotes")
    ler_insumo(estoque_hospitalar, "Gazes")

    # 5. Atualizar a quantidade de um insumo
    print("\nAtualizando quantidade...")
    atualizar_quantidade(estoque_hospitalar, "Seringas", 180)
    ler_insumo(estoque_hospitalar, "Seringas")

    # 6. Remover um insumo
    print("\nRemovendo insumo...")
    remover_insumo(estoque_hospitalar, "Termômetros")
    ler_insumo(estoque_hospitalar, "Termômetros") # Verificar remoção
    ler_insumo(estoque_hospitalar, "todos") # Verificar lista após remoção

    # 7. Análise com Grafo
    print("\n--- Análise de Estoque com Grafo ---")
    grafo_estoque = construir_grafo_por_local(estoque_hospitalar["insumos"])
    print(f"Grafo construído com {grafo_estoque.number_of_nodes()} nós (insumos) e {grafo_estoque.number_of_edges()} arestas (mesmo local).")

    abaixo, acima = analisar_estoque_grafo(grafo_estoque)

    print("\nProdutos Abaixo do Ideal:")
    if abaixo:
        for nome, atual, ideal in abaixo:
            print(f"  - {nome}: Atual={atual}, Ideal={ideal} (Faltam {ideal - atual})")
    else:
        print("  Nenhum produto abaixo do ideal.")

    print("\nProdutos Acima do Ideal:")
    if acima:
        for nome, atual, ideal in acima:
            print(f"  - {nome}: Atual={atual}, Ideal={ideal} (Sobram {atual - ideal})")
    else:
        print("  Nenhum produto acima do ideal.")

    # Exemplo: Encontrar vizinhos de um insumo no grafo (mesmo local)
    try:
        vizinhos_alcool = list(grafo_estoque.neighbors("Álcool em gel"))
        print(f"\nInsumos no mesmo local que 'Álcool em gel': {vizinhos_alcool}")
    except nx.NetworkXError:
        print("\n'Álcool em gel' não encontrado no grafo (pode ter sido removido ou não adicionado)." )

    print("\n--- Fim da Execução ---")

