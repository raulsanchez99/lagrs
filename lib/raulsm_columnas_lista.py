#!/usr/bin/env python3
#Raul Sanzhez Merino raulsm

import re

def get_uid_regexp(output_decode):

        uid = re.compile(r"""
        uid= #Primer grupo
        ( 
        \d{1,4} # Un número de entre 1 y 4 dígitos
        )      
        """, re.VERBOSE)
        #Probamos con el texto de forma literal
        texto=r"""uid=1000(rauls) gid=1000(rauls) grupos=1000(rauls),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),131(lxd),132(sambashare)"""
        for linea in texto.split('\n'):
            m=uid.search(linea)
            if m:
                return m.group(1)
   


def get_groups_regrexp(output_decode):

    parametros = output_decode.split(" ")

    groups = parametros[2].split("grupos=")

    groups = groups[1]

    groups = groups.split(",")

    num_groups = len(groups)

   
    for i in range (0, num_groups-1):
        #Devuelve todas las coincidencias entre lo paréntesis
        group = re.findall(r'[(](.*?)[)]', groups[i]) 
        groups += group

    cadena = " ".join(groups)
    cadena = cadena.split("\n")
    cadena = cadena[1]
    return cadena

        
def lines(list):

    # Divido la lista en lineas a partir de los saltos de linea. 

    lista = list.split("\n")
    
    # Elimino la primera ya que es una linea en blanco
    
    lista.pop(0)

    return lista

def count_lines(lista):

    # Calculo el número de lineas que tiene el listado

    num_lines = len(lista)

    return num_lines
