filePath = "/home/rafael/Estudos/Resultados SlowFastSign/Phoenix2/Random/Replication1/run1/train.corpus.csv"

with open(filePath, "r") as f:
    linhas = f.readlines()

del linhas[0]

palavras = []
for l in linhas:
    palavras.append(l.split("|")[-1])

with open("palavras.txt", "w") as f:
    f.writelines(palavras)