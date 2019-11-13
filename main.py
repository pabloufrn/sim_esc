import csv
from collections import deque
import numpy as np 


def simular(alg, strref, qtdfrm, qtdpag):
	if(qtdfrm >= qtdpag): 
		print("Erro: Nenhuma página será substituida se qtdfrm >= qtdpag.")
		exit(0)
	if(alg == "fifo"):
		return simular_fifo(strref, qtdfrm, qtdpag)
	elif(alg == "fifo2"):
		return simular_fifo2(strref, qtdfrm, qtdpag)
	elif(alg == "lru"):
		pass
	else:
		print("Erro: forneca um algoritmo válido.")
		return None

def simular_fifo2(strref, qtdfrm, qtdpag):
	refereced = qtdfrm * [False]
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque((qtdpag-qtdfrm) * ['']) # caso qtdfrm > qtdpag não vai ter substituição de páginas
	tabela_prc = [list(fila_prc + fila_frm)]
	page_fault = ['']
	for page in strref:
		if(page not in fila_frm):
			
			removed_index = 0
			for i, p in enumerate(fila_frm):
				if(refereced[i]):
					refereced[i] = False
				else:
					refereced[i] = False
					removed_index = i
					break
			try:
				fila_prc.remove(page)
			except:
				fila_prc.pop()
			fila_prc.appendleft('')
			fila_frm[removed_index] = page
			page_fault.append('P')
		else:
			page_fault.append('')
		tabela_prc.append(list(fila_frm + fila_prc))
	return tabela_prc, page_fault

def simular_fifo(strref, qtdfrm, qtdpag):
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque((qtdpag if qtdpag > qtdfrm else qtdfrm) * [''])
	tabela_prc = [list(fila_prc)]
	page_fault = ['']
	for page in strref:
		if(page not in fila_frm):
			fila_frm.pop()
			fila_frm.appendleft(page)
			fila_prc.pop()
			fila_prc.appendleft(page)
			page_fault.append('P')
		else:
			page_fault.append('')
		tabela_prc.append(list(fila_prc))
	return tabela_prc, page_fault

def salvar_em_csv(nome_arquivo, tabela, qtdframes, page_fault, strref):
	tabela = np.array(tabela).T
	with open(nome_arquivo, "w+") as f:
		writer = csv.writer(f)
		writer.writerow([''] + strref)
		writer.writerow(['-']*len(tabela[0]))
		for line in tabela[0:qtdframes]:
			writer.writerow(line)
		writer.writerow(['-']*len(tabela[0]))
		for line in tabela[qtdframes:]:
			writer.writerow(line)
		writer.writerow(page_fault)

if ( __name__ == "__main__"):
	strstrref = input("digite a string de referência: ")
	strref = [int(c) for c in strstrref]
	qtdpag = max(strref) - min(strref) + 1
	qtdfrm = int(input("digite a quantidade de frames: "))
	alg = input("digite a politíca desejada: (fifo, lru ou fifo2): ")
	tabela, page_fault = simular(alg, strref, qtdfrm, qtdpag)
	salvar_em_csv("saida.csv", tabela, qtdfrm, page_fault, strref)
