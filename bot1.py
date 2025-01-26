import discord
from botlogic import gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send("que rollo plebes")
    elif message.content.startswith('chao'):
        await message.channel.send("hasta luego chao")
    elif message.content.startswith('dame una contraseña'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)




