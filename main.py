import discord
from discord.ext import commands
import random
import os

# Create an instance of a bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

eco_memes = os.listdir("./images")

recycling_tips = [
"Utiliza frascos de vidrio para guardar las sobras en lugar de recipientes de plástico.",
"Convierte las camisetas viejas en trapos de limpieza.",
"Utiliza ambos lados del papel antes de reciclarlo.",
"Haz abono con los restos de comida en lugar de tirarlos.",
"Utiliza una botella de agua reutilizable en lugar de comprar las de plástico.",
"Dona ropa vieja en lugar de tirarla.",
"Utiliza pilas recargables para reducir los residuos.",
"Reutiliza las botellas de vidrio como jarrones o recipientes de almacenamiento.",
"Utiliza servilletas de tela en lugar de las de papel.",
"Compra productos con un embalaje mínimo.",
"Utiliza una bolsa de la compra reutilizable en lugar de bolsas de plástico.",
"Recicla los productos electrónicos en centros de residuos electrónicos designados.",
"Utiliza un calendario digital en lugar de uno de papel.",
"Compra artículos de segunda mano para reducir la demanda de productos nuevos.",
"Repara los artículos en lugar de sustituirlos."
]

waste_sorting_tips = {
"plastico": "Arroja los plásticos en el contenedor amarillo.",
"papel": "Arroja el papel en el contenedor azul.",
"vidrio": "Arroja el vidrio en el contenedor verde.",
"organico": "Arroja los residuos orgánicos en el contenedor marrón.",
"metal": "Arroja los metales en el contenedor amarillo.",
"electronicos": "Lleva los aparatos electrónicos a un centro de reciclaje de residuos electrónicos.",
"baterias": "Desecha las pilas en los puntos de recogida designados.",
"textiles": "Dona o recicla los textiles en los bancos de ropa.",
"madera": "Desecha la madera sin tratar en el contenedor de reciclaje adecuado.",
"peligrosos": "Lleva los residuos peligrosos a un centro de eliminación especial.",
"bombillas": "Recicla las bombillas en los puntos de recogida designados.",
"poliestireno": "Consulta las directrices locales para el reciclaje de poliestireno.",
"tetra pak": "Recicla los envases de Tetra Pak en el lugar adecuado bin.",
"latas": "Recicle las latas de aluminio en el contenedor amarillo.",
"caja de carton": "Aplaste las cajas de cartón y recíclelas en el contenedor azul."
}

decomposition_facts = [
"Una botella de plástico tarda 450 años en descomponerse.",
"Una lata de aluminio tarda entre 80 y 200 años en descomponerse.",
"Una botella de vidrio puede tardar hasta 1 millón de años en descomponerse.",
"Una colilla de cigarrillo tarda entre 1 y 5 años en descomponerse.",
"Un calcetín de lana tarda entre 1 y 5 años en descomponerse.",
"Una lata tarda unos 50 años en descomponerse.",
"Un zapato de cuero tarda entre 25 y 40 años en descomponerse.",
"Un cartón de leche tarda 5 años en descomponerse.",
"Una bolsa de plástico tarda entre 10 y 20 años en descomponerse.",
"Una toalla de papel tarda entre 2 y 4 semanas en descomponerse.",
"Una cáscara de plátano tarda entre 2 y 5 semanas en descomponerse.",
"Una camisa de algodón tarda entre 1 y 5 meses en descomponerse.",
"Un hilo de pescar tarda 600 años en descomponerse." "Un pañal desechable tarda 500 años en descomponerse.",
"La suela de goma de una bota tarda entre 50 y 80 años en descomponerse."
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='recycle')
async def recycle(ctx):
    tip = random.choice(recycling_tips)
    await ctx.send(f'Tip de recicleje: {tip}')

@bot.command(name='sort')
async def sort(ctx, material: str = None):
  if material is None:
      available_materials = ', '.join(waste_sorting_tips.keys())
      await ctx.send(f"Por favor, especifica un material. Estos son los materiales disponibles: {available_materials}")
  else:
      tip = waste_sorting_tips.get(material.lower(), "¡No sé dónde tirar eso!")
      await ctx.send(f'Tip de orden de residuos: {tip}')

@bot.command(name='meme')
async def meme(ctx):
    meme = random.choice(eco_memes)
    with open(f'images/{meme}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command(name='decompose')
async def decompose(ctx):
    fact = random.choice(decomposition_facts)
    await ctx.send(f'Descomposición de elementos: {fact}')

# Run the bot with your token
bot.run('Acá va tu token')
