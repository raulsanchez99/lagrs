#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Raul Sanzhez Merino raulsm

#!/usr/bin/env python3
#  mi_top03.py

import sys
import os

import raulsm_columnas_lista
import raulsm_formato as m1
import raulsm_resultados as m3

from optparse import OptionParser

try:
	pythonpath = os.environ["PYTHONPATH"]
except:
	sys.stderr.write("Error: variable PYTHONPATH no encontrada\n")
	raise SystemExit

pythonpath = pythonpath.split(":")
path = os.environ["HOME"] + "/lagrs/lib"

modulo1 = path + "/raulsm_formato.py"
modulo2 = path + "/raulsm_columnas_lista.py"
modulo3 = path + "/raulsm_resultados.py"

modulos = [modulo1, modulo2, modulo3]

for m in modulos:
	if(not os.path.isfile(m)):
		sys.stderr.write("Error: fichero {} no encontrado\n".format(m))
		raise SystemExit

def main():

	usage = "usage: %prog [options] arg"
	parser = OptionParser(usage)

	parser.add_option("-n", dest="option_n", help="Porcentajes de Cpu mayores a 0.0")
	parser.add_option("-u", dest="option_u", help="Muestra los procesos que están corriendo con el usuario seleccionado")
	parser.add_option("-p", dest="option_p", help="Mostramos la información sobre el PID seleccionado")

	(opciones,argumentos) = parser.parse_args()

	#python3 modulos.py -n 50

	if(opciones.option_n) == True: 
		comando_1 = ["top", "-n",  "1" , "-n", opciones.option_n]
	
	#python3 modulos.py -u 1

	elif(opciones.option_u) == True:
		
		comando_1 = ["top", "-n", "1", "-u", opciones.option_u]

	#python3 modulos.py -p 1

	elif(opciones.option_p) == True:
		comando_1 = ["top", "-n", "1", "-p", opciones.option_p]

	#python3 modulos.py 
	else:
		comando_1 = ["top", "-n", "1"]

	comando_2 = ["id"]
	output = m1.get_output(comando_1)
	output_decode = m1.decode_utf8(output)
	list = m1.no_header(output_decode)
	lista = raulsm_columnas_lista.lines(list)
	num_lines = raulsm_columnas_lista.count_lines(lista)

	output_2 = m1.get_output(comando_2)
	output_decode_2 = m1.decode_utf8(output_2)
	uid =  raulsm_columnas_lista.get_uid_regexp(output_decode_2)
	groups = raulsm_columnas_lista.get_groups_regrexp(output_decode_2)


	m3.script (lista, num_lines, uid, groups, opciones.option_n, opciones.option_u, opciones.option_p)

if __name__ == '__main__':

        main()

