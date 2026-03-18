import discord
from discord.ext import commands
from discord.ui import View
import os

# 🔑 CONFIG
TOKEN = os.getenv("TOKEN")

GUILD_ID = 1483270417056665806  # ID serveur
WELCOME_CHANNEL_ID = 1483278869820735691  # salon bienvenue
ROLE_ID = 1483292624797306930  # rôle après règlement

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ READY
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    bot.add_view(ReglementView())  # 🔥 garde le bouton actif

# 🎉 BIENVENUE
@bot.event
async def on_member_join(member):
    if member.guild.id != GUILD_ID:
        return

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    embed = discord.Embed(
        title="🎉 Bienvenue !",
        description=f"Bienvenue {member.mention} sur le serveur 🔥\nAccepte le règlement pour accéder au serveur.",
        color=discord.Color.orange()
    )

    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.set_image(url="https://i.imgur.com/yourimage.png")

    await channel.send(embed=embed)

# 🔥 EMBED (répondre à un message)
@bot.command()
async def embed(ctx):

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

# 📜 BOUTON REGLEMENT
class ReglementView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✅ Accepter le règlement", style=discord.ButtonStyle.green)
    async def accept(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.guild.id != GUILD_ID:
            return

        role = interaction.guild.get_role(ROLE_ID)

        await interaction.user.add_roles(role)

        await interaction.response.send_message(
            "✅ Tu as accepté le règlement !",
            ephemeral=True
        )

# 📩 COMMANDE POUR ENVOYER LE REGLEMENT
@bot.command()
async def reglement(ctx):

    if ctx.guild.id != GUILD_ID:
        return

    embed = discord.Embed(
        title="📜 Règlement",
        description="Merci de lire et accepter le règlement pour accéder au serveur.",
        color=discord.Color.blue()
    )

    view = ReglementView()

    await ctx.send(embed=embed, view=view)

# 🚀 LANCEMENT
bot.run(TOKEN)
