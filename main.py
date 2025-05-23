import time
estoque_hospitalar = {
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
            "quantidade_atual": 500,
            "quantidade_ideal": 500,
            "unidade": "unidades"
        }
    ]
}

def adicionar_insumo(nome, local, quantidade_atual, quantidade_ideal, unidade):
    novo_insumo = {
        "nome": nome,
        "local": local,
        "quantidade_atual": quantidade_atual,
        "quantidade_ideal": quantidade_ideal,
        "unidade": unidade
    }
    estoque_hospitalar["insumos"].append(novo_insumo)
    print(f"Adicionando insumo '{nome}'.")
    time.sleep(0.5)
    print(f"Adicionando insumo '{nome}'..")
    time.sleep(0.5)
    print(f"Adicionando insumo '{nome}'...")
    time.sleep(0.5)
    print(f"Insumo '{nome}' adicionado com sucesso!")

# Função para ordenar insumos por nome usando Merge Sort
def ordernar_insumos(lista, chave="nome"):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        ordernar_insumos(esquerda)
        ordernar_insumos(direita)
        
        i, j, k = 0, 0, 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][chave] < direita[j][chave]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = direita[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = esquerda[j]
            j += 1
            k += 1
    return lista 
estoque_hospitalar = { "insumos": [ordernar_insumos(estoque_hospitalar["insumos"], "nome")] }

# Função para buscar insumo usando busca binária
def buscar_insumo(nome):
    nomes = [insumo["nome"] for insumo in estoque_hospitalar["insumos"]]
    esquerda = 0
    direita = len(nomes) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if nomes[meio] == nome:
            return estoque_hospitalar["insumos"][meio], meio
        elif nomes[meio] < nome:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return "Insumo não encontrado.", -1

def ler_isumo(nome):
    if nome == "todos":
        for insumo in estoque_hospitalar["insumos"]:
            print(f"Insumo: {insumo['nome']}")
            print(f"Local: {insumo['local']}")
            print(f"Quantidade Atual: {insumo['quantidade_atual']} {insumo['unidade']}")
            print(f"Quantidade Ideal: {insumo['quantidade_ideal']} {insumo['unidade']}")
            print("="*20)
        return
    insumo, _ = buscar_insumo(nome)
    print(f"Buscando insumo '{nome}'.")
    time.sleep(0.5)
    print(f"Buscando insumo '{nome}'..")
    time.sleep(0.5)
    print(f"Buscando insumo '{nome}'...")
    time.sleep(0.5)
    if insumo != "Insumo não encontrado.":
        print(f"Insumo: {insumo['nome']}")
        print(f"Local: {insumo['local']}")
        print(f"Quantidade Atual: {insumo['quantidade_atual']} {buscar_insumo['unidade']}")
        print(f"Quantidade Ideal: {insumo['quantidade_ideal']} {buscar_insumo['unidade']}")
        return
    print(f"Insumo '{nome}' não encontrado.")

def atualizar_quantidade(nome, nova_quantidade):
    insumo, index = buscar_insumo(nome)
    if insumo != "Insumo não encontrado.":
        estoque_hospitalar["insumos"][index]["quantidade_atual"] = nova_quantidade
        print(f"Atualizando quantidade do insumo '{nome}'.")
        time.sleep(0.5)
        print(f"Atualizando quantidade do insumo '{nome}'..")
        time.sleep(0.5)
        print(f"Atualizando quantidade do insumo '{nome}'...")
        time.sleep(0.5)
        print(f"Insumo '{nome}' atualizado com sucesso!")
        return
    print(f"Insumo '{nome}' não encontrado.")

def remover_insumo(nome):
    insumo, index = buscar_insumo(nome)
    if insumo != "Insumo não encontrado.":
        estoque_hospitalar["insumos"].pop(index)
        print(f"Removendo insumo '{nome}'.")
        time.sleep(0.5)
        print(f"Removendo insumo '{nome}'..")
        time.sleep(0.5)
        print(f"Removendo insumo '{nome}'...")
        time.sleep(0.5)
        print(f"Insumo '{nome}' removido com sucesso!")
        return
    print(f"Insumo '{nome}' não encontrado.")

# Funções para verificar o estoque, adiconar grafos nelas
def produtos_abaixo_ideal():
    return

def produtos_acima_ideal():
    return

# Função para verificar o estoque e gerar um relatório apenas roda as duas funções acima
def verificar_estoque():
   return 