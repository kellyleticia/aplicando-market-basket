import os
import random
import csv
random.seed(42)
def gerando_amostras(teste):
    num_amostras = 400
    max_tamanho_amostra = 5
    amostras = []
    for x in range(num_amostras):
        tamanho_amostra = random.randint(2, max_tamanho_amostra)
        amostra = random.sample(teste, tamanho_amostra)
        amostras.append(amostra)
    return amostras

def percorrendo_diretorio(dir):
    diretorio = dir
    lista = []
    for arquivo in os.listdir(diretorio):
        with open(os.path.join(diretorio, arquivo), 'r') as f:
            conteudo = f.read().rstrip().splitlines()
            lista.extend(conteudo)
    resultado = gerando_amostras(lista)
    return resultado

def percorrendo_diretorios(diretorios):
    lista = []
    for diretorio in diretorios:
        for arquivo in os.listdir(diretorio):
            with open(os.path.join(diretorio, arquivo), 'r') as f:
                conteudo = f.read().rstrip().splitlines()
                lista.extend(conteudo)
    resultado = gerando_amostras(lista)
    return resultado

dir1 = 'keywords_dev'
p1 = percorrendo_diretorio(dir1)

dir2 = 'keywords_ed'
p2 = percorrendo_diretorio(dir2)

dir3 = 'keywords_rc'
p3 = percorrendo_diretorio(dir3)

matriz_final = []
matriz_final.extend(p1)
matriz_final.extend(p2)
matriz_final.extend(p3)

with open('matriz_por_tag.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(matriz_final)

c1 = percorrendo_diretorios([dir1, dir2])
c2 = percorrendo_diretorios([dir2, dir3])

matriz2 = []
matriz2.extend(c1)
matriz2.extend(c2)

with open('matriz_duas_combinacoes.csv', 'w', newline='') as g:
    write = csv.writer(g)
    write.writerows(matriz2)

resultado = percorrendo_diretorios([dir1, dir2, dir3])

with open('matriz_total.csv', 'w', newline = '') as h:
    writ = csv.writer(h)
    writ.writerows(resultado)