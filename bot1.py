import discord
from discord.ext import commands
import random
from botlogic import gen_pass

description = '''Un bot de ejemplo para mostrar la extensión discord.ext.commands.
module.

Aquí se muestran varios comandos de utilidad.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='¿', description=description, intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """suma dos numeros."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """lanza un dado en formato NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('el formato tiene que ser NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='para cuando quieras decidir de otra manera')
async def choose(ctx, *choices: str):
    """elige entre varias opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repitiendo...'):
    """reoite un mensaje multiples veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """dice cuendo se une un miembro."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """dice si un miembro es cool.

    realmente solo verifica si se está invocando un subcomando.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')


@cool.command(name='bot')
async def _bot(ctx):
    """el bot es cool?"""
    await ctx.send('Si, el bot es cool.')

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('hola'):
        await msg.channel.send("que rollo plebes")




