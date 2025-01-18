import discord 
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

tips_reciclaje = [
    "🌱 **Tip #1:** Enjuaga los envases antes de reciclarlos para evitar contaminar otros materiales.",
    
    "🌱 **Tip #2:** Aplasta las latas y botellas de plástico para ahorrar espacio en los contenedores.",
    
    "🌱 **Tip #3:** Separa las tapas de las botellas, ya que suelen ser de materiales diferentes.",
    
    "🌱 **Tip #4:** Reutiliza las bolsas de plástico o mejor aún, usa bolsas de tela.",
    
    "🌱 **Tip #5:** No incluyas papel con restos de comida en el reciclaje de papel.",
    
    "🌱 **Tip #6:** Compra productos con envases reciclables o mínimo empaque.",
    
    "🌱 **Tip #7:** Utiliza un contenedor diferente para cada tipo de material reciclable.",
    
    "🌱 **Tip #8:** Retira las etiquetas de los envases de vidrio antes de reciclarlos.",
    
    "🌱 **Tip #9:** Dobla las cajas de cartón para optimizar el espacio de reciclaje.",
    
    "🌱 **Tip #10:** Infórmate sobre los días de recolección de reciclaje en tu zona."
]

reciclables = """🔄 **OBJETOS RECICLABLES:**
• Botellas de plástico
• Latas de aluminio
• Papel y cartón
• Envases de vidrio
• Cajas de cartón
• Periódicos y revistas
• Envases de metal
• Tetra pak
• Bolsas de papel
• Frascos de vidrio"""

no_reciclables = """⛔ **OBJETOS NO RECICLABLES:**
• Pañales
• Papel higiénico usado
• Cerámica rota
• Espejos
• Bombillas
• Residuos electrónicos
• Baterías
• Aceite usado
• Residuos médicos
• Productos químicos"""

@bot.event
async def on_ready():
        print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def recycle(ctx):
    await ctx.send("Que tipo de reciclaje quieres aprender acerca? 'externo' or 'interno'")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and \
               message.content.lower() in ['externo', 'interno']
    
    try:
        response = await bot.wait_for('message', timeout=30.0, check=check)
        
        if response.content.lower() == 'externo':
            await ctx.send("""Reciclaje externo ocurre en las afueras y es cuando la gente envia a botes de reciclaje la basura que encuentran afuera :
• Papel y carton
• Botellas y jarras de cristal
• Botellas de plastico
• Latas de metal y aluminio
Recuerde limpiar los contenedores antes de reciclarlos!""")
            
        elif response.content.lower() == 'interno':
            await ctx.send("""Reciclaje interno ocurre en casa, Y se puede hacer:
• Compostando desechos
• Reutilizando contenedores
• Reutilizando objetos
• Reducir consumo de plasticos
Empieza con pasos pequeños para conseguir grandes impactos!""")
            
    except TimeoutError:
        await ctx.send("No respondiste a tiempo :( Intentalo otra vez!")

    else:
        await ctx.send("Eso no es un tipo de reciclaje")

@bot.command()
async def reciclable(ctx):
    await ctx.send(reciclables)

@bot.command()
async def noreciclable(ctx):
    await ctx.send(no_reciclables)

@bot.command()
async def tips(ctx):
    tip_aleatorio = random.choice(tips_reciclaje)
    await ctx.send(tip_aleatorio)

bot.run("Token")