#Raul Sanchez raulsm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# top_telegram.py

import os
import re
import telepot
import telepot.namedtuple
import time
import argparse
import mi_top03
from telepot.loop import MessageLoop

# Función para leer el token del bot desde un archivo llamado 'token.txt'
def leer_token():

    try:
    	# Abrimos el archivo en modo lectura
        f = open('token.txt','r')
        token = f.read()
    except FileNotFoundError as e:
        print(e)
        raise SystemExit
    except ValueError as e:
        print(e)
        raise SystemExit
    finally:
        f.close()# Cerramos el archivo, asegurándonos de liberar los recursos

    return token # Devolvemos el token leído
    

# Función para obtener el ID del bot a partir del token
def get_id_bot(token):
    id_bot = re.compile(r"""
    ( 
    \d{10} # Un número de entre 10 dígitos
    )      
    """, re.VERBOSE)
    
    texto=token
    for linea in texto.split('\n'):
        m=id_bot.search(linea)
        if m:
            return m.group(0)

# Función para enviar un mensaje a un usuario usando el bot
def enviar_mensaje(token, id_usuario, mensaje):

    bot = telepot.Bot(token)
    bot.sendMessage(id_usuario, mensaje)

    return print("****-")

# Leemos el token desde el archivo y eliminamos posibles saltos de línea al final
token = leer_token()
token = token.rstrip('\n')
bot = telepot.Bot(token)

# Función que maneja los mensajes entrantes
def handle(msg):
    chat_id = msg["chat"]["id"]  # Obtenemos el ID del chat de donde proviene el mensaje
    texto = msg['text']  # Extraemos el texto del mensaje
    top = msg['from']  # Obtenemos información del remitente
    opciones = ("top, mi_top")  # Opciones válidas que el usuario puede consultar
    
    # Imprimimos en consola quién envió el mensaje y el contenido
    print("{} escribió  => {}".format(top, texto))

    mensaje = texto.lower()  # Convertimos el texto a minúsculas para facilitar la comparación

    # Verificamos si el mensaje coincide con las opciones permitidas
    if mensaje == "top":
        respuesta = mi_top03.main()  # Control de respuesta nula
    elif mensaje == "mi_top":
        respuesta = mi_top03.main()
    else:
        # Si el mensaje no coincide con ninguna opción, enviamos un mensaje de error
        respuesta = "Solo puedes consultar las opciones: {}".format(opciones)
    
    # Imprimimos en consola la respuesta que enviará el bot
    print("LAGRSBOT respondió => {}".format(respuesta))
    
    # Enviamos la respuesta al usuario, verificando que no esté vacía
    if respuesta:
        bot.sendMessage(chat_id, respuesta)
	
    return print("*****")


# Función principal que inicializa el bot y el bucle de escucha
def main():
    token = leer_token()
    token = token.rstrip('\n')

    mensaje = "El bot de top_telegram.py ha funcionado!!!"
    id_usuario ="5552229576"

    enviar_mensaje(token, id_usuario, mensaje)
    bot = telepot.Bot(token)
    MessageLoop(bot, handle).run_as_thread()
    print ("Escuchando...")

    # Mantenemos el programa corriendo en un bucle infinito
    while 1:
        time.sleep(10)


if __name__ == '__main__':
	
	main()
