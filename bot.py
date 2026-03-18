import discord
from discord.ext import commands
import os

# 🔑 CONFIG
TOKEN = os.getenv("TOKEN")

GUILD_ID = 1483270417056665806  # 🔥 ID DE TON SERVEUR
WELCOME_CHANNEL_ID = 1483278869820735691  # 🔥 ID DU SALON BIENVENUE

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ BOT READY
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# 🎉 MESSAGE DE BIENVENUE (SEULEMENT TON SERVEUR)
@bot.event
async def on_member_join(member):
    if member.guild.id != GUILD_ID:
        return  # ignore les autres serveurs

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    embed = discord.Embed(
        title="🎉 Bienvenue !",
        description=f"Bienvenue {member.mention} sur le serveur 🔥\nAmuse-toi bien !",
        color=discord.Color.orange()
    )

    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

    embed.set_image(url="https://i.imgur.com/yourimage.png")

    await channel.send(embed=embed)

# 🔥 COMMANDE EMBED (répondre à un message)
@bot.command()
async def embed(ctx):

    # 🔒 limite au serveur
    if ctx.guild.id != GUILD_ID:
        return

    if ctx.message.reference is None:
        await ctx.send("❌ Réponds à un message pour le transformer en embed")
        return

    msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)

    embed = discord.Embed(
        description=msg.content,
        color=discord.Color.blue()
    )

    embed.set_footer(text="Game Store")

    await ctx.send(embed=embed)

# 🚀 LANCEMENT
bot.run(TOKEN)
