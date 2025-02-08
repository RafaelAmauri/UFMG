import numpy as np 
import os
import matplotlib.pyplot as plt

path = "/home/rafael/Estudos/Datasets/phoenix2014-release/phoenix-2014-multisigner/features/fullFrame-256x256px/train"

annPathFullDataset = "/home/rafael/Estudos/Datasets/phoenix2014-release/phoenix-2014-multisigner/annotations/manual/train.corpus.csv"

annPathPhoenix20AL = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix20/AL6Steps16Frames16BatchSize/Replication1/run6/train.corpus.csv"
annPathPhoenix20Random = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix20/Random/Replication1/train.corpus.csv"

annPathPhoenix5AL = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix5/AL6Steps16Frames16BatchSize/Replication2/run6/train.corpus.csv"
annPathPhoenix5Random = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix5/Random/Replication1/train.corpus.csv"

annPathPhoenix2AL = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix2/AL6Steps16Frames16BatchSize/Replication3/run6/train.corpus.csv"
annPathPhoenix2Random = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix2/Random/Replication1/run1/train.corpus.csv"

nFrames = []
palavras = []

with open(annPathPhoenix2Random, "r") as f:
    lines = f.readlines()
    del lines[0]
    for l in lines:
        videoPath = l.split("|")[1].rstrip("*.png")
        frase = l.split("|")[-1].split(" ")
        

        nFrames.append(len(os.listdir(f"{path}/{videoPath}")))
        palavras.extend(frase)



def plot_frame_count_distribution(frame_counts, bins=50):
    plt.figure(figsize=(9,9))
    plt.hist(frame_counts, bins=bins, edgecolor='black')
    plt.xlabel('Número de Frames')
    plt.xticks((0, 50, 100, 150, 200, 250, 300))
    plt.ylabel('Frequência')
    plt.title('Distribuição de Número de Frames por Vídeo - Replicação 1 Active Learning Subconjunto 2%')
    plt.savefig("/home/rafael/histograma.png", dpi=100)
    plt.show()

palavras = set(palavras)
print(f"{len(palavras)} Palavras unicas")

print(f"{len(nFrames)} videos unicos")
media = np.mean(nFrames)
S = np.std(nFrames, ddof=1)
Q1 = np.percentile(nFrames, 25)

print(f"Media = {media:.2f}, DP = {S:.2f}, Q1 = {Q1}")

valorTabelaT = 1.960

upperBound = media + valorTabelaT * (S / np.sqrt(len(nFrames)))
lowerBound = media - valorTabelaT * (S / np.sqrt(len(nFrames)))

print(f"IC = [{lowerBound:.2f}, {upperBound:.2f}]")

# Example usage:
#plot_frame_count_distribution(nFrames, bins=30)