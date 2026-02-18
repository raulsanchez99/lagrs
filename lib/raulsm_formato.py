#!/usr/bin/env python3
#formato.py
#Raul Sanzhez Merino raulsm

import subprocess

def get_output(comando):

	#Obtengo la salida al introducir el comando `top -n 1`
	
	try:
		output  = subprocess.check_output(comando)
	except subprocess.CalledProcessError:
		sys.stderr.write("La orden ha producido un error\n")
		raise SystemExit

	return output


def decode_utf8(output):

	#Paso el código a UTF-8 para que sea legible

	output_decode = output.decode("utf-8")
	
	return output_decode



def no_header(output_decode):

	# Le quito todo hasta la cabecera de la lista para mostrar el listado

	list = output_decode.split("ORDEN")

	# Ha dividido la salida (output) en 2: hasta el final de la cabecera y después de la cabecera
	#Me quedo con lo  que hay después

	list = list[1]

	return list
