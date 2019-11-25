import csv
from collections import deque
import numpy as np 


def simular(alg, strref, qtdfrm, qtdpag):
	if(alg == "fifo"):
		return simular_fifo(strref, qtdfrm, qtdpag)
	elif(alg == "fifo2"):
		return simular_fifo2(strref, qtdfrm, qtdpag)
	elif(alg == "lru"):
		return simular_lru(strref, qtdfrm, qtdpag)
	else:
		print("Erro: forneca um algoritmo válido.")
		return None

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

def simular_fifo2(strref, qtdfrm, qtdpag):
	refereced = qtdfrm * [False]
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque((qtdpag-qtdfrm) * ['']) # caso qtdfrm > qtdpag não vai ter substituição de páginas
	tabela_prc = [list(fila_prc + fila_frm)]
	page_fault = ['']
	for page in strref:
		print("\t".join((str(p) for p in fila_frm)))
		print("\t".join((str(r) for r in refereced)))
		if(page not in fila_frm):
			if(fila_frm[-1] == ''):
				fila_frm.appendleft(page)
				fila_frm.pop()
				page_fault.append('P')
				refereced[1] = refereced[0]
				refereced[0] = False
			else:
				removed_index = -1
				for i in range(len(fila_frm)-1, -1, -1):
					if(refereced[i]):
						refereced[i] = False
					else:
						refereced[i] = False
						removed_index = i
						break
				try:
					fila_prc.remove(page)
				except ValueError:
					fila_prc.pop()
				fila_prc.appendleft(fila_frm[removed_index])
				fila_frm.remove(fila_frm[removed_index])
				fila_frm.appendleft(page)
				page_fault.append('P')
				for i in range(removed_index, 0, -1):
					refereced[removed_index] = refereced[removed_index-1]
				refereced[0] = False
		else:
			page_fault.append('')
			refereced[fila_frm.index(page)] = True
		tabela_prc.append(list(fila_frm + fila_prc))
	return tabela_prc, page_fault

def simular_lru(strref, qtdfrm, qtdpag):
	fila_frm = deque(qtdfrm * [''])
	fila_prc = deque((qtdpag if qtdpag > qtdfrm else qtdfrm) * [''])
	tabela_prc = [list(fila_prc)]
	page_fault = ['']
	for page in strref:
		if(page not in fila_frm):
			fila_frm.pop()
			fila_frm.appendleft(page)
			if(page in fila_prc):
				fila_prc.remove(page)
			else:
				fila_prc.pop()
			fila_prc.appendleft(page)
			page_fault.append('P')
		else:
			page_fault.append('')
			fila_prc.remove(page)
			fila_prc.appendleft(page)
			fila_frm.remove(page)
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

def salvar_em_csv(nome_arquivo, tabela, qtdframes, page_fault, strref, string_dist):
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
		writer.writerow([''] + string_dist)

if ( __name__ == "__main__"):
	strstrref = input("digite a string de referência: \n")
	strref = [int(c) for c in strstrref]
	qtdpag = max(strref) - min(strref) + 1
	qtdfrm = int(input("digite a quantidade de frames: "))
	alg = input("digite a politíca desejada: (fifo, lru ou fifo2): ")
	
	tabela, page_fault = simular(alg, strref, qtdfrm, qtdpag)
	string_dist = calcular_string_distancia(tabela, strref)
	media = calcular_media(string_dist)

	print("string de distância: \n")
	print(string_dist)
	print("\nMédia: ")
	print(media)
	salvar_em_csv("saida.csv", tabela, qtdfrm, page_fault, strref, string_dist)


