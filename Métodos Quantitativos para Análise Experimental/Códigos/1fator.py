import numpy as np
from pprint import pprint

dados20 = {
            "2": [30.21,	30.96,	31.75],
            "3": [31.55,	30.65,	30.84],
            "6": [31.35,	30.11,	30.56],
            "9": [30.95,	30.99,	31.81]
}

dados5 = {
            "2": [56.76,	58.54,	56.35],
            "3": [57.39,	56.95,	58.34],
            "6": [58.36,	58.45,	56.50],
            "9": [56.72,	56.18,	58.63]
}



dados2 = {
            "2": [78.38	,78.63,	77.84],
            "3": [78.91	,78.41,	77.66],
            "6": [78.99	,77.56,	77.91],
            "9": [78.37 ,78.10,	78.67]
}


dados = dados20

#####
## Calculando Níveis e Repetições
#####
nNiveis     = len(dados.keys())
nRepeticoes = len(dados[list(dados.keys())[0]])

print(f"Níveis: {nNiveis}")
print(f"Repetições: {nRepeticoes}")
print("\n")

#####
## Calculando Soma, Média e Efeito da Linha
#####
mediaTotal = 0
somaTotal  = 0
nomesFatores = list(dados.keys())
for fator in nomesFatores:
    dados[f"soma{fator}"]  = np.sum(dados[fator])
    dados[f"media{fator}"] = np.mean(dados[fator])

    somaTotal += np.sum(dados[fator])

mediaTotal = np.mean([dados[f"media{i}"] for i in nomesFatores])

dados["somaTotal"]  = somaTotal
dados["mediaTotal"] = mediaTotal

print(f"Soma  Total: {dados["somaTotal"]:.4f}")
print(f"Média Total: {dados["mediaTotal"]:.4f}")
print("\n")


for fator in nomesFatores:
    dados[f"Efeito{fator}"] = dados[f"media{fator}"] - dados["mediaTotal"]


#####
## Calculando os SS
#####

dados["SSE"] = 0
dados["SSY"] = 0
dados["SSA"] = 0
for fator in nomesFatores:
    for dataPoint in dados[fator]:
        dados["SSE"] += (dataPoint - dados[f"media{fator}"])**2
        dados["SSY"] += dataPoint ** 2
    
    dados["SSA"] += nRepeticoes * (dados[f"Efeito{fator}"] **2)

dados["SS0"] = nNiveis * nRepeticoes * (dados["mediaTotal"]**2)
dados["SST"] = dados["SSY"] - dados["SS0"]
dados["SSE"] = dados["SST"] - dados["SSA"]

for ss in ["SS0", "SSY", "SST", "SSA", "SSE"]:
    print(f"{ss}: {dados[ss]:.4f}")
print("\n")


#####
## Calculando a variação explicada pelo fator e pelo erro
#####
dados["variacaoExplicadaFator"] = dados["SSA"] / dados["SST"]
dados["variacaoExplicadaErros"] = 1 - dados["variacaoExplicadaFator"]

print(f"% Variação Explicada pelo fator:  {100 *dados["variacaoExplicadaFator"]:.4f}%")
print(f"% Variação Explicada pelos erros: {100 * dados["variacaoExplicadaErros"]:.4f}%")
print("\n")


#####
## Teste F
#####
dofMSA = (nNiveis - 1)
dofMSE = (nNiveis * (nRepeticoes - 1))

print(f"Graus de Liberdade do MSA: {dofMSA}")
print(f"Graus de Liberdade do MSE: {dofMSE}")

dados["MSA"] = dados["SSA"] / dofMSA
dados["MSE"] = dados["SSE"] / dofMSE

print(f"MSA: {dados["MSA"]:.4f}")
print(f"MSE: {dados["MSE"]:.4f}")


dados['FComputado'] = dados["MSA"] / dados["MSE"]
print(f"F Computado: {dados['FComputado']:.4f}")

# Para 95% de confiança, 3 e 8 graus de liberdade
valorTabelaF = 4.07
print(f"Valor crítico tabela F para 3 e 8 graus a 95% de confiança: {valorTabelaF}\n")

if dados["FComputado"] < valorTabelaF:
    print(f"Variação explicada pelo Fator NÃO é significativa")
else:
    print(f"Variação explicada pelo Fator é significativa")
print("\n")


#####
## IC para efeitos
#####

Se2 = dados["SSE"] / dofMSE
Se  = np.sqrt(Se2)
Seu = Se / np.sqrt(nNiveis * nRepeticoes)
Sea = Se * np.sqrt((nNiveis - 1) / (nNiveis * nRepeticoes))

print(f"Se^2: {Se2:.4f}")
print(f"Se:   {Se:.4f}")
print(f"Seu:  {Seu:.4f}")
print(f"Sea:  {Sea:.4f}")
print("\n")

# Valor tabela T para 95% de confiança 8 graus de liberdade
valorTabelaT = 2.306
print(f"\nValor na tabela T para 8 graus de liberdade a 95% de confiança: {valorTabelaT}\n")


for fator in nomesFatores:
    lowerBound = dados[f"Efeito{fator}"] - valorTabelaT * Sea
    upperBound = dados[f"Efeito{fator}"] + valorTabelaT * Sea

    isSignificant = "" if (lowerBound < 0 and upperBound < 0) or (lowerBound > 0 and upperBound > 0) else "NÃO"

    print(f"IC {fator}: {dados[f"Efeito{fator}"]:.4f} +- {valorTabelaT} * {Sea:.4f} = [{lowerBound:.4f}, {upperBound:.4f}] -> {isSignificant} é significativo")