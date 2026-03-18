import discord
from discord.ext import commands
from discord import app_commands
import os

# ===== CONFIG =====
TOKEN = os.getenv("TOKEN")  # Railway
GUILD_ID = 1483270417056665806  # ⚠️ MET TON ID SERVEUR

WELCOME_CHANNEL_ID = 1483278869820735691  # salon bienvenue

WELCOME_IMAGE = "https://i.imgur.com/yourimage.png"  # image bienvenue

# ===== INTENTS =====
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== ON READY =====
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

    try:
        guild = discord.Object(id=GUILD_ID)
        bot.tree.copy_global_to(guild=guild)
        synced = await bot.tree.sync(guild=guild)
        print(f"Commandes sync : {len(synced)}")
    except Exception as e:
        print(e)

# ===== BIENVENUE =====
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    embed = discord.Embed(
        description=f"👋 Bienvenue {member.mention} sur le serveur !\n\nAmuse-toi bien 🎮",
        color=discord.Color.green()
    )

    embed.set_image(url=WELCOME_IMAGE)
    embed.set_footer(text="Game Store")

    await channel.send(embed=embed)

# ===== COMMANDE EMBED =====
@bot.tree.command(name="embed", description="Envoyer un message stylé")
@app_commands.describe(message="Ton message", image="Lien image (optionnel)")
async def embed(interaction: discord.Interaction, message: str, image: str = None):

    embed = discord.Embed(
        description=message,
        color=discord.Color.blue()
    )

    if image:
        embed.set_image(url=image)

    embed.set_footer(text="Game Store")

    await interaction.response.send_message(embed=embed)

# ===== COMMANDE PAIEMENT =====
@bot.tree.command(name="paiement", description="Afficher les moyens de paiement")
async def paiement(interaction: discord.Interaction):

    embed = discord.Embed(
        title="💳 Moyens de paiements",
        description=(
            "━━━━━━━━━━━━━━━\n"
            "• PayPal (amie proche / sans notes)\n"
            "• LTC\n"
            "━━━━━━━━━━━━━━━"
        ),
        color=discord.Color.green()
    )

    await interaction.response.send_message(embed=embed)

# ===== LANCEMENT =====
bot.run(TOKEN)
