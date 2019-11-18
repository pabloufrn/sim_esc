import csv
from collections import deque
import numpy as np 

def escalonar(strref, qtdfrm, qtdpag):
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque(qtdpag * [''])
	tabela_prc = [list(fila_prc)]
	page_fault = [False]
	for index, page in enumerate(strref):
		if(page not in fila_frm):
			fila_frm.pop()
			fila_frm.appendleft(page)
			if(page in fila_prc):
				fila_prc.remove(page)
			else:
				fila_prc.pop()
			fila_prc.appendleft(page)
			page_fault.append(True)
		else:
			page_fault.append(False)
			end = fila_prc.remove(page)
			fila_prc.appendleft(page)
			endf = fila_frm.remove(page)
			fila_frm.appendleft(page)
		tabela_prc.append(list(fila_prc))
	return tabela_prc, page_fault

def calcular_string_distancia(tabela, strref):
	lista_dist = [None]*len(strref)
	for i in range(1, len(strref) + 1):
		try:
			distancia = tabela[i - 1].index(strref[i-1]) + 1
			lista_dist[i - 1] = distancia 
		except ValueError:
			lista_dist[i - 1] = 0
	return lista_dist

def calcular_media(list_dist):
	return sum(list_dist)/len(list_dist)

def salvar_em_csv(nome_arquivo, tabela, qtdframes):
	tabela = np.array(tabela).T
	with open(nome_arquivo, "w+") as f:
		writer = csv.writer(f)
		for line in tabela[0:qtdframes]:
			writer.writerow(line)
		writer.writerow(['-']*len(tabela[0]))
		for line in tabela[qtdframes:]:
			writer.writerow(line)

if ( __name__ == "__main__"):
	strstrref = input("digite a string de referência: \n")
	strref = [int(c) for c in strstrref]
	qtdpag = max(strref) - min(strref) + 1
	qtdfrm = int(input("digite a quantidade de frames: \n\n"))
	
	tabela, page_fault = escalonar(strref, qtdfrm, qtdpag)
	string_dist = calcular_string_distancia(tabela, strref)
	media = calcular_media(string_dist)

	print("string de distância: \n")
	print(string_dist)
	print("\nMédia: ")
	print(media)
	salvar_em_csv("saida.csv", tabela, qtdfrm)


