#Adaptado de: https://deinfo.uepg.br/~alunoso/2016/ROUNDROBIN/
import os
MAX = 10

def executar_fila(processos, num_proc, quantum):
	cont_proc = num_proc
	inicio_fila = 1
	while (cont_proc != 0):
		while(processos[inicio_fila] <= 0):
			inicio_fila += 1
			if(inicio_fila >= num_proc):
				inicio_fila = 0

		print("\nO processo " + str(inicio_fila) + " vai executar tendo ainda " + str(processos[inicio_fila]) + 
			  " unidades de tempo faltando.")
		processos[inicio_fila] = processos[inicio_fila] - quantum

		if(processos[inicio_fila] <= 0):
			print("E sai da fila.")
			cont_proc -= 1
		else:
			print("E vai para o final da fila com " + str(processos[inicio_fila]) + "unidades de tempo restantes.")

		inicio_fila += 1;                           
		if(inicio_fila > num_proc):
			inicio_fila = 0;

		print(processos)




if __name__ == "__main__":
	processos = [0]*MAX
	quantum = int(input("Insira o tempo máximo de execução momentânea para os processos: "))
	num_proc = int(input("Insira a quantidade de processos: "))

	for i in range(1, num_proc + 1):
		processos[i] = int(input("Insira o tempo de execução total do processo " + str(i) + ":"))

	executar_fila(processos, num_proc, quantum)