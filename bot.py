import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

# 🔥 CONFIG
WELCOME_CHANNEL_ID = 1483278869820735691  # mets ton ID ici

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ===== BIENVENUE AUTO =====
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            description=(
                f"👋 Bienvenue {member.mention} sur le serveur 🎮\n\n"
                "Ici tu peux acheter jeux et cartes cadeaux à bon prix.\n\n"
                "📜 Lis le règlement\n"
                "🛒 Regarde la boutique\n"
                "🎫 Ouvre un ticket pour acheter\n\n"
                "🔥 Amuse-toi bien !"
            ),
            color=0xff7a00
        )

        # 🔥 IMAGE (change le lien)
        embed.set_image(url="https://i.postimg.cc/3x49vyTZ/321ac303e526c9b325dd42370ac73672.webp")

        embed.set_footer(text="GameStore FR")

        await channel.send(embed=embed)

# ===== COMMANDE EMBED PERSONNALISÉ =====
@bot.tree.command(name="embed", description="Envoyer un message stylé avec image")
@app_commands.describe(
    message="Ton message",
    image="Lien de l'image (optionnel)"
)
async def embed(interaction: discord.Interaction, message: str, image: str = None):

    embed = discord.Embed(
        description=message,
        color=0x2b2d31
    )

    # 🔥 image optionnelle
    if image:
        embed.set_image(url=image)

    await interaction.response.send_message(embed=embed)

# ===== COMMANDE MOYENS DE PAIEMENT =====
@bot.tree.command(name="paiement", description="Afficher moyens de paiement")
async def paiement(interaction: discord.Interaction):

    embed = discord.Embed(
        title="💳 Moyens de paiements",
        description=(
            "━━━━━━━━━━━━━━━\n"
            "• PayPal (amie proche / sans notes)\n"
            "• LTC\n"
            "━━━━━━━━━━━━━━━"
        ),
        color=0x2b2d31
    )

    # 🔥 image optionnelle (tu peux changer ou supprimer)
    embed.set_image(url="https://i.imgur.com/your-image.png")

    await interaction.response.send_message(embed=embed)

# ===== READY =====
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    await bot.tree.sync()

# ===== RUN =====
bot.run(TOKEN)