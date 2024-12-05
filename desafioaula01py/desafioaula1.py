# Exemplo de entrada
resultados = [
    ("Equipe A", [10, 9, 8, 7]),
    ("Equipe B", [6, 7, 8, 9]),
    ("Equipe C", [8, 8, 8, 8]),
    ("Equipe D", [5, 5, 5, 5])
]

# Passo 1: Calcular a média das pontuações de cada equipe
medias = []
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append((equipe, media))

# Passo 2: Ordenar a lista de médias em ordem decrescente
medias.sort(key=lambda x: x[1], reverse=True)

# Passo 3: Criar a lista de classificação
classificacao = medias  # Já está ordenada

# Passo 4: Exibir a classificação final
print("Classificação final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media:.2f}")
