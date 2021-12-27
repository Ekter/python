import os
import random
import pandas as pd
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib.request


load_dotenv("../../globals.env")
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
RESPONSES = [
    "PLIK37",
    "#Évangile n°1 : Plik a raison",
    "#Évangile n°2 : Plik n'a pas tord",
    "#Évangile n°3 : Plik ne se trompe pas",
    "#Évangile n°4 : Plik est dans le vrai",
    "#Évangile n°5 : Plik n'est pas dans le faux",
    "#Évangile n°6 : Kilp n'a pas raison",
    "#Évangile n°7 : Kilp a tord",
    "#Évangile n°8 : Kilp se trompe",
    "#Évangile n°9 : Kilp n'est pas dans le vrai",
    "#Évangile n°10 : Kilp est dans le faux",
    "#Évangile n°11 : Kilp est l'acte de tuer et Plik l'acte de donner la vie",
    "#Évangile n°12 : 2 décimales c'est un arrondi de fils de pute",
    "#Évangile n°13 : Les fils de putes c'est aussi des fils de kilpomanes",
    "#Évangile n°14 : Plik est Plein",
    "#J'ai raison donc je suis",
    "#On ne diminue pas son bonheur en le partageant",
    "#Le parapente c'est divin",
    "#niounnn",
    "#je suis fatigué",
    "#il fait froid",
    "Faire tomber une patate, c'est 37 ans de malheur",
    None,
    1,
]
bot = commands.Bot(command_prefix=["§", "rb"])


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.command(name="info", help="Informations tirées du Plikoran",aliases=["infos","i","!"])
async def info(ctx: commands.Context, n: int = -1):
    if not n in range(len(RESPONSES)):
        response = random.choice(RESPONSES)
    else:
        response = RESPONSES[n]
    await ctx.message.delete()
    await ctx.send(response)


@bot.command(name="attack", help="Fait des dégats à un boss",aliases=["a","attaque","att","at"])
async def info(
    ctx: commands.Context, boss: str = "ver", degats: int = -1, team: str = "team"
):
    df = pd.read_csv("attacks.csv")
    df = df.append({"team": team, "boss": boss, "degats": degats}, ignore_index=True)[
        ["team", "boss", "degats"]
    ]
    print(df)
    df.to_csv("attacks.csv")
    await ctx.send(
        f"Tu as attaqué le boss {boss} à {degats} dégats avec ta team {team}. Réponse enregistrée!"
    )
    try:
        dfvie = pd.read_csv("vieactboss.csv")
        print(dfvie)
        dfvie[boss][0] = dfvie[boss][0] - degats
        print(dfvie)
        dfvie[["ver", "bete", "gast", "garam"]].to_csv("vieactboss.csv")
    except ValueError as e:
        await ctx.send(f"boss {boss} non trouvé")
        print(e)

@bot.command(name="vie",help="Affiche la vie actuelle des boss",aliases=["v","vieact","vieactuelle","vieactuel"])
async def vie(ctx: commands.Context):
    dfvie = pd.read_csv("vieactboss.csv")
    await ctx.send(f"{dfvie}")


@bot.command(name="ping",help="Ping en masse de la personne voulue(actuellement pas fonctionnel)",aliases=["p","pong"])
async def info(ctx: commands.Context, n: int = 10, user: discord.Member = "ver"):
    for i in range(n):
        try:
            await ctx.send(f"{user.mention}")
        except Exception as e:
            await ctx.send(f"Ping {i} {ctx.author.mention}")

@bot.command(name="wiki",help="Affiche la page wikipédia voulue(sans accent svp)",aliases=["w"])
async def wiki(ctx: commands.Context, target: str = None):
    url="https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard" if target==None else "https://fr.wikipedia.org/wiki/"+target
    url=url.lower()
    print(url)
    with urllib.request.urlopen(url) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        print(soup)
        n=0
        for anchor in soup.get_text().split("\n"):
            if n>0:
                try:
                    await ctx.send(anchor)
                except Exception as e:
                    print(f"{e}")
                    pass
            n+=1

@bot.command(name="ckoi",help="Affiche une description courte (sans accent svp)",aliases=["c"])
async def wk(ctx: commands.Context, target: str = None):
    try:
        url="https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard" if target==None else "https://fr.wikipedia.org/wiki/"+target
        with urllib.request.urlopen(url) as response:
            webpage = response.read()
            soup = BeautifulSoup(webpage, 'html.parser')
            num2 = soup.find("div", {"class": "mw-parser-output"})
            for i in num2:
                if str(i)[:3]=="<p>":
                    await ctx.send(i.get_text())
                    break
    except Exception as e:
        await ctx.send(f"Je ne sais pas ce que c'est {target}.")

@bot.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n{kwargs}\n")
        else:
            raise


bot.run(TOKEN)
