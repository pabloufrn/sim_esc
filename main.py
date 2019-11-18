import csv
from collections import deque
import numpy as np 

def escalonar(strref, qtdfrm, qtdpag):
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque(qtdpag * [''])
	tabela_prc = [list(fila_prc)]
	page_fault = [False]
	for page in strref:
		if(page not in fila_frm):
			fila_frm.pop()
			fila_frm.appendleft(page)
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
	strstrref = input("digite a string de referência: ")
	strref = [int(c) for c in strstrref]
	qtdpag = max(strref) - min(strref) + 1
	qtdfrm = int(input("digite a quantidade de frames: "))
	
	tabela, page_fault = escalonar(strref, qtdfrm, qtdpag)
	salvar_em_csv("saida.csv", tabela, qtdfrm)


