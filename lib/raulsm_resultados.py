#!/usr/bin/env python3
#Raul Sanzhez Merino raulsm


def script (lista, num_lines, uid, groups, option_n,option_u, option_p):   

    contador = 0
    for i in range(num_lines-1):

        # Solo dejo un esppacio entre los componentes de cada columna

        line =" ".join(lista[i].split())

        # Diferencio cada componente según el espacio (" ") que hay entre ellos

        line = line.split(" ")

        # Al comienzo hay un espacio

        nombre = line[12]
        pid = line[1]
        cpu_string = line[9]
        cpu = cpu_string.replace(',', '.')
        cpu_float = float(cpu)
        usuario = line[2]
        

        if (option_n):
            if cpu_float > 0.0:

                contador += +1
                print("\nNúmero de proceso que consume más del 0.0% de la CPU -> {0}:\n".format(contador))

                print (" " + pid + " " + usuario + " " + " " + uid + " "  + groups + " " +  cpu_string + " " + nombre )
        elif (option_u):    
            if usuario == option_u:   
            	contador += +1
            	print("\nProceso de {} número {}".format(option_u, contador))
            	print ("ORDEN:  " + nombre + ", PID: " + pid)
        
        elif (option_p):
            if pid == option_p:
                print("\nHas seleccionado el PID {}: ".format(option_p))
                print (" " + pid + " " + usuario + " " + " " + uid + " "  + groups + " " +  cpu_string + " " + nombre )
                
        else:
        	print (" " + pid + " " + usuario + " " + " " + uid + " "  + groups + " " +  cpu_string + " " + nombre )
