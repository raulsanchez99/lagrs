#!/usr/bin/env python3
#bot: LagrsRbot

import telepot
import time
from telepot.loop import MessageLoop
from datetime import datetime

# Carga del token
try:
    with open('token.txt') as f:
        TOKEN = f.read().strip()
    bot = telepot.Bot(TOKEN)
except Exception as e:
    print("Error al cargar el token:", str(e))

# Manejo de mensajes
def handle(msg):
    # Extraer información básica
    chat_id = msg["chat"]["id"]
    texto = msg["text"]
    usuario = msg["from"].get("first_name", "Usuario")
    fecha_unix = msg["date"]

    # Convertir fecha Unix a formato legible
    fecha_legible = datetime.fromtimestamp(fecha_unix).strftime("%d/%m/%Y %H:%M:%S")

    # Mostrar información legible en la consola del servidor
    print(f"Recibiendo mensaje de {usuario}:")
    print(f"Fecha y hora: {fecha_legible}")
    print(f"ID del chat: {chat_id}")
    print(f"Mensaje: {texto}")

    # Responder al usuario
    respuesta = f"Hola {usuario}, me has dicho: '{texto}'"
    bot.sendMessage(chat_id, respuesta)

# Función principal
def main():
    MessageLoop(bot, handle).run_as_thread()
    print("Escuchando...")

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()

