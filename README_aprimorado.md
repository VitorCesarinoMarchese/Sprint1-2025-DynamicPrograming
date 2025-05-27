# Sprint1-2025-DynamicPrograming

## Descrição

Este projeto é um sistema de gerenciamento de estoque hospitalar desenvolvido em Python. Ele permite controlar insumos hospitalares, incluindo funcionalidades para adicionar, buscar, listar, atualizar e remover itens do estoque. O sistema também utiliza grafos (com NetworkX) para analisar a distribuição dos insumos por local e identificar produtos acima ou abaixo da quantidade ideal.

## Funcionalidades

- **Adicionar Insumo:** Insere um novo item ao estoque, garantindo ordenação para buscas eficientes.
- **Buscar Insumo:** Busca binária por nome do insumo (após ordenação).
- **Listar Insumos:** Exibe todos os insumos ou detalhes de um específico.
- **Atualizar Quantidade:** Altera a quantidade atual de um insumo.
- **Remover Insumo:** Remove um insumo do estoque.
- **Análise com Grafo:** Constrói um grafo conectando insumos no mesmo local e identifica produtos acima/abaixo do ideal.

## Como Usar

1. Instale as dependências:
   ```sh
   pip install networkx
   ```
2. Execute o script principal:
    ```sh
    python main.py
    ```
O script irá demonstrar todas as funcionalidades acima, exibindo o resultado no terminal.

## Estrutura do Código
- main.py: Script principal com todas as funções e exemplos de uso.
- Estrutura de dados baseada em lista de dicionários para os insumos.
- Funções separadas para cada operação de estoque e análise.

## Exemplo de Saída
 ```sh
    --- Sistema de Gerenciamento de Estoque Hospitalar ---

    Ordenando estoque inicial...
    Estoque ordenado por nome.

    --- Listando Todos os Insumos ---
    Insumo: Agulhas
    Local: Depósito C
    Quantidade Atual: 550 unidades
    ...
    Produtos Abaixo do Ideal:
    - Álcool em gel: Atual=50, Ideal=120 (Faltam 70)
    ...

    --- Fim da Execução ---
 ```
## Requisitos
- Python 3.7+
- networkx