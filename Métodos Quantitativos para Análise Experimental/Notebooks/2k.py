# Programa que calcula todos os valores para mim
import numpy as np
from pprint import pprint

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

nReplicacoes = 3
nFatores     = 2
nParametros  = 3

# Dados do Phoenix20. Estão aqui para referência. Não mexer!

dados20 = {
            "levels0":  [ 1,  1,  1, 1],
            "levelsA":  [-1,  1, -1, 1],
            "levelsB":  [-1, -1,  1, 1],
            "levelsAB": [1,  -1, -1, 1],
            "Y1":  [30.58, 30.04, 30.03, 29.19],
            "Y2":  [30.49, 31.44, 29.12, 30.63],
            "Y3":  [30.44, 31.15, 30.77, 29.90]
}

dados5 = {
            "levels0":  [ 1,  1,  1, 1],
            "levelsA":  [-1,  1, -1, 1],
            "levelsB":  [-1, -1,  1, 1],
            "levelsAB": [1,  -1, -1, 1],
            "Y1":  [59.46, 54.57, 59.27, 56.65],
            "Y2":  [56.32, 59.15, 58.84, 57.11],
            "Y3":  [57.76, 59.99, 55.26, 57.98]
}

dados2 = {
            "levels0":  [ 1,  1,  1, 1],
            "levelsA":  [-1,  1, -1, 1],
            "levelsB":  [-1, -1,  1, 1],
            "levelsAB": [1,  -1, -1, 1],
            "Y1":  [78.44, 78.08, 79.18, 77.54],
            "Y2":  [79.29, 79.06, 78.66, 78.91],
            "Y3":  [78.20, 78.29, 79.58, 77.30]
}


dados = dados2

dados["Ymedio"] = []
for y1, y2, y3 in zip(dados["Y1"], dados["Y2"], dados["Y3"]):
    media = (y1 + y2 + y3) / nReplicacoes
    dados["Ymedio"].append(media)

print(f"Y médio: {[dados["Ymedio"]]}")

######
##
## Calculando os SS
##
######

for factor in ["levels0", "levelsA", "levelsB", "levelsAB"]:
    total = 0
    for factorLevel, yMedio in zip(dados[factor], dados["Ymedio"]):
        total += factorLevel * yMedio
    
    total = total / 2 ** nFatores
    factorName = factor.strip("levels")

    # Calculando os coeficientes
    dados[f"q{factorName}"] = total

    # Calculando os SS
    dados[f"SS{factorName}"] = 4 * nReplicacoes * total**2

# Calculando o SSE
dados["SSE"] = 0
for ymedio, y1, y2, y3 in zip(dados["Ymedio"], dados["Y1"], dados["Y2"], dados["Y3"]):
    dados["SSE"] += (y1 - ymedio)**2 + (y2 - ymedio)**2 + (y3 - ymedio)**2

# Calculando o SST
dados["SST"] = dados["SSA"] + dados["SSB"] + dados["SSAB"] + dados["SSE"]


for q in ["q0", "qA", "qB", "qAB"]:
    pprint(f"Coeficiente {q}: {dados[q]:.4f}")
print("\n")

print(f"Modelo: {dados["q0"]:.4f} + {dados["qA"]:.4f}Xa + {dados["qB"]:.4f}Xb + {dados["qAB"]:.4f}XaXb\n")

######
##
## Calculando a % de variação explicada por cada coeficiente
##
######
for ss in ["SSA", "SSB", "SSAB"]:
    print(f"{ss}: 2^2 * 3 * ({np.sqrt(dados[ss]/12):.4f})^2 = {dados[ss]:.4f}")
    print(f"Variação explicada pelo {ss}: 100 * {ss} / SST = {100 * dados[ss] / dados["SST"]:.2f}%\n")

pprint(f"SSE: {dados["SSE"]:.4f}")
pprint(f"Variação explicada pelo SSE: 100 * SSE / SST = {100 * dados["SSE"] / dados["SST"]:.2f}%")

print(f"SST: {dados['SST']:.4f}\n")

######
##
## Teste F
##
######

# Graus de liberdade
# São 12 amostras, então temos 11 graus de liberdade totais. Desses 11, 8 vão para os erros. 
# Sobram 3 graus de liberdade, 1 para cada fator.
dofA  = 1
dofB  = 1
dofAB = 1

dofE  = 8 # nAmostras - (2^k). Temos 12 amostras e 2 fatores: A e B. Logo, dof = 12 - 2^2 = 8
pprint(f"Graus de Liberdade dos fatores: {dofA}")
pprint(f"Graus de Liberdade dos erros: {dofE}")

dados["MSA"]  = dados["SSA"]  / dofA
dados["MSB"]  = dados["SSB"]  / dofB
dados["MSAB"] = dados["SSAB"] / dofAB

dados["MSE"]  = dados["SSE"]  / dofE

# 95% de confiança para 1 grau e 8 graus
valorTabelaF  = 5.32
print(f"Valor crítico tabela F para 1 e 8 graus a 95% de confiança: {valorTabelaF}\n")
for ms in ["MSA", "MSB", "MSAB"]:
    fComputado = dados[ms] / dados["MSE"]
    pprint(f"F calculado para {ms}/MSE: {dados[ms]:.4f} / {dados["MSE"]:.4f} = {fComputado:.4f}")

    isPorcentagemVariacaoSignigicativa = "" if fComputado > valorTabelaF else "NÃO"
    pprint(f"Porcentagem de variação explicada pelo {ms} {isPorcentagemVariacaoSignigicativa} é significativa")

print("\n")


######
##
## Intervalo de Confiança
##
######

# Calculando o Se e os desvios para cada coeficiente
dados["Se"]   = np.sqrt(dados["SSE"] / (4 * (nReplicacoes - 1)))
print(f"Se: sqrt(SSE / 8) = {dados["Se"]:.4f}")

for s in ["Sq0", "SqA", "SqB", "SqAB"]:
    dados[s] = dados["Se"] / np.sqrt(4 * nReplicacoes)
    pprint(f"{s}: {dados[s]:.4f}")


# 95% de confiança para 8 graus de liberdade (4 * (nReplicacoes - 1))
valorTabelaT = 2.306
print(f"\nValor na tabela T para 8 graus de liberdade a 95% de confiança: {valorTabelaT}\n")
# Calculando os ICs
for q, s in zip(["q0", "qA", "qB", "qAB"], ["Sq0", "SqA", "SqB", "SqAB"]):
    valorQ = dados[q]
    valorS = dados[s]

    lowerBound = valorQ - valorTabelaT * valorS
    upperBound = valorQ + valorTabelaT * valorS


    isSignificant = "" if (lowerBound < 0 and upperBound < 0) or (lowerBound > 0 and upperBound > 0) else "NÃO"

    print(f"IC {q}: {valorQ:.4f} +- {valorTabelaT} * {valorS:.4f} = [{lowerBound:.4f}, {upperBound:.4f}] -> {isSignificant} é significativo")


'''
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

# Sample data (replace with your actual 'dados' dictionary)
dados = {
    "Replicação 1": dados["Y1"],
    "Replicação 2": dados["Y2"],
    "Replicação 3": dados["Y3"]
}

# Define the categories
x_labels = [
    "StepSize = 3, Número de Frames = 8",
    "StepSize = 6, Número de Frames = 8",
    "StepSize = 3, Número de Frames = 16",
    "StepSize = 6, Número de Frames = 16"
]

# Assign numeric positions to each category
x = np.arange(len(x_labels))  # [0, 1, 2, 3]

# Define a function to normalize RGB values from [0, 255] to [0, 1]
def normalize_rgb(rgb_tuple):
    return tuple([x / 255 for x in rgb_tuple])

# Define the color mapping for categories using normalized RGB tuples
category_color_map = {
    "StepSize = 3, Número de Frames = 8": "#b21507",
    "StepSize = 6, Número de Frames = 8": "#994208",
    "StepSize = 3, Número de Frames = 16": "#045c20",
    "StepSize = 6, Número de Frames = 16": "#330370"
}

# Define the marker style mapping for categories
category_marker_map = {
    "StepSize = 3, Número de Frames = 8": "o",      # Circle
    "StepSize = 6, Número de Frames = 8": "s",      # Square
    "StepSize = 3, Número de Frames = 16": "D",     # Diamond
    "StepSize = 6, Número de Frames = 16": "^"      # Triangle Up
}

# Define replication colors using normalized RGB tuples
replication_color_map = {
    "Replicação 1": normalize_rgb((128, 0, 128)),   # Purple
    "Replicação 2": normalize_rgb((0, 128, 128)),   # Teal
    "Replicação 3": "#acbf1d"    # SaddleBrown
}

# Create the plot with specified figure size
fig, ax = plt.subplots(figsize=(16, 12))

# Set y-axis limits to accommodate markers below the axis
ax.set_ylim(ymin=-15, ymax=100)

# Set axis labels with increased font size
ax.set_xlabel("Combinação de Fator", fontsize=22)
ax.set_ylabel("WER", fontsize=22)

# Define bar width and offsets for grouped bars
bar_width = 0.2
offsets = [-bar_width, 0, bar_width]  # For Rep1, Rep2, Rep3

# List of replications
replications = list(dados.keys())

# Iterate over each replication and plot its bars with confidence intervals
for i, replication in enumerate(replications):
    # Calculate positions
    positions = x + offsets[i]
    
    # Get y-values
    y_values = dados[replication]
    
    # Plot the bars with error bars
    ax.bar(
        positions,
        y_values,
        bar_width,
        label=replication,
        color=replication_color_map[replication],
        alpha=0.7,
        capsize=5,  # Length of the error bar caps
        error_kw={'elinewidth':1.5, 'ecolor':'black'}
    )

# Remove default x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels([''] * len(x_labels))  # Empty labels


# Add category markers below the x-axis
for i, category in enumerate(x_labels):
    ax.scatter(
        x[i], 
        -10,  # Position below the x-axis
        color=category_color_map[category], 
        marker=category_marker_map[category], 
        s=200,  # Larger marker size for visibility
        zorder=5  # Ensure markers are on top
    )

# **Create Custom Legend Handles for Replications**
replication_legend_elements = [
    Line2D([0], [0], marker='s', color='w', label=replication,
           markerfacecolor=color, markersize=10)
    for replication, color in replication_color_map.items()
]

# **Create Custom Legend Handles for Categories**
category_legend_elements = [
    Line2D([0], [0], marker=category_marker_map[category], color='w', label=category,
           markerfacecolor=category_color_map[category], markersize=10)
    for category in x_labels
]

# **Combine All Legend Handles and Labels**
handles = replication_legend_elements + category_legend_elements 
labels = [replication for replication in replication_color_map.keys()] + \
         [category for category in x_labels] + ['Threshold = 30.125']

# **Position the Legend Below the Plot**
ax.legend(
    handles=handles,
    labels=labels,
    title='Replications, Factor Combinations, and Threshold',
    fontsize=18,
    title_fontsize=18,
    loc='upper center',          # Anchor point of the legend within the bbox
    bbox_to_anchor=(0.5, -0.15), # Position below the plot: (x, y)
    borderaxespad=0.0,           # No padding between the plot and the legend
    ncol=3                        # Number of columns in the legend for compactness
)

# **Add a Descriptive Title to the Plot**
ax.set_title("WER by Factor Combination and Replication", fontsize=22)

# **Remove Grid Lines if Present**
ax.grid(False)

# **Adjust Layout to Make Space for the Legend**
plt.tight_layout(rect=[0, 0.05, 1, 1])  # Increase bottom margin to accommodate the legend

# **Save the Plot (Optional)**
plt.savefig('wer_bar_plot_with_threshold_and_below_legend.png', dpi=300, bbox_inches='tight')

# **Show the Plot**
plt.show()
'''