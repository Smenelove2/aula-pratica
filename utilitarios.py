import csv

# Função que lê o arquivo .csv e transforma em uma lista
def ler_notas_csv() -> list[float]:
    notas = []

    with open("notas.csv", mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            notas.append(float(linha[0]))

    return notas