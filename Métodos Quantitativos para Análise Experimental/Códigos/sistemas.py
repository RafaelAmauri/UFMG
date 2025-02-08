import numpy as np

 # Aqui é um teste pareado de numero de amostras iguais.
def pairedTTest(results1, results2):
    diffs = []

    # Calcula a diferença Xi Yi e adiciona em uma lista
    for r1, r2 in zip(results1, results2):
        diffs.append(r1 - r2)

    # Calcula a média entre as diferenças
    mediaDiffs = np.mean(diffs)
    print(f"Média das diferenças: {mediaDiffs:.4f}")

    # Desvio padrão das diferenças
    Sd = np.std(diffs, ddof=1)
    print(f"Sd: {Sd:.4f}")

    # Graus de liberdade
    degreesOfFreedom = len(results1) - 1
    print(f"Graus de liberdade: {degreesOfFreedom}")

    # Valor na tabela T para 2 graus de liberdade com 95% de confiança
    valorTabelaT = 4.303
    print(f"\nValor na tabela T para 2 graus de liberdade a 95% de confiança: {valorTabelaT}\n")


    IC =  valorTabelaT * (Sd / np.sqrt(len(results1)))

    lowerBound = mediaDiffs - IC
    upperBound = mediaDiffs + IC

    isSignificant = "" if (lowerBound < 0 and upperBound < 0) or (lowerBound > 0 and upperBound > 0) else "NÃO"

    print(f"IC: {mediaDiffs:.4f} +- {IC:.4f} = [{lowerBound:.4f}, {upperBound:.4f}] -> {isSignificant} é significativo")

phoenix20 = (
                [29.19, 30.63, 29.90],
                [30.97, 31.21, 31.13]
)

phoenix5 = (
                [56.65, 57.11, 57.98],
                [58.72, 57.66, 56.01]
)

phoenix2 = (
                [77.54, 78.91, 77.30],
                [77.31, 77.37, 75.68]
)

dados = phoenix20

t1, t2 = dados

pairedTTest(t1, t2)