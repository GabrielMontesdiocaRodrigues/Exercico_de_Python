import copy


def exibir(lista): 
    for item in lista : 
        print(item)
    print()

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco' : round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
]

exibir(produtos)
exibir(novos_produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda item : item['nome'], reverse=True)

exibir(produtos_ordenados_por_nome)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda item : item['preco'])

exibir(produtos_ordenados_por_preco)