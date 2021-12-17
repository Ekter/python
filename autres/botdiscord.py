import os
import random
import pandas as pd

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("../../globals.env")
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
RESPONSES=["PLIK37","#Évangile n°1 : Plik a raison",
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
    "Faire tomber une patate, c'est 37 ans de malheur",None,1]
bot = commands.Bot(command_prefix='rb')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="!")
async def info(ctx:commands.Context,n:int=-1):
        if not n in range(len(RESPONSES)):
            response = random.choice(RESPONSES)
        else:
            response=RESPONSES[n]
        await ctx.message.delete()
        await ctx.send(response)

[print(i) for i in bot.get_all_members()]

@bot.command(name="a",desc="Fait des dégats à un boss")
async def info(ctx:commands.Context,boss:str="ver",degats:int=-1,team:str="team"):
    df=pd.read_csv("attacks.csv")
    df=df.append({"team":team,"boss":boss,"degats":degats},ignore_index=True)[["team","boss","degats"]]
    print(df)
    df.to_csv("attacks.csv")
    await ctx.send(f"Tu as attaqué le boss {boss} à {degats} dégats avec ta team {team}. Réponse enregistrée!")
    try:
        dfvie=pd.read_csv("vieactboss.csv")
        print(dfvie)
        dfvie[boss][0]=dfvie[boss][0]-degats
        print(dfvie)
        dfvie[["ver","bete","gast","garam"]].to_csv("vieactboss.csv")
    except ValueError as e:
        await ctx.send(f"boss {boss} non trouvé")
        print(e)


@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n{kwargs}\n')
        else:
            raise

bot.run(TOKEN)
