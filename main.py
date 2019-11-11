import csv
from collections import deque 

def escalonar(strref, qtdfrm, qtdpag):
	fila_frm = deque(qtdfrm * [-1])
	fila_prc = deque(qtdpag * [-1])
	tabela_prc = [list(fila_prc)]
	page_fault = [False]
	for page in strref:
		if(page not in fila_frm):
			fila_frm.pop()
			fila_frm.append(page)
			fila_prc.pop()
			fila_prc.append(page)
			page_fault.append(True)
		else:
			page_fault.append(False)
		tabela_prc.append(list(fila_prc))
	return tabela_prc

def salvar_em_csv(nome_arquivo, tabela):
	with open(nome_arquivo, "w+") as f:
		pass
			

if ( __name__ == "__main__"):
	strstrref = input("digite a string de referência: ")
	strref = [int(c) for c in strstrref]
	qtdpag = max(strref) - min(strref) + 1
	qtdfrm = int(input("digite a quantidade de frames: "))
	escalonar(strref, qtdfrm, qtdpag)




