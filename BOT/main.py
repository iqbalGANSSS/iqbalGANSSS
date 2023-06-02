import discord
from discord.ext import commands

TOKEN = 'MTExNDIxNjc3OTQ4OTc1NTE0Ng.GA2zbr.1XtA1XNdRH__2dv45Me281ERAmP0xw9wIDTCU0'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Bot terhubung sebagai {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def admin_only(ctx):
    await ctx.send("Hanya admin yang dapat menggunakan command ini!")


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def about(ctx):
    await ctx.send('Ikbal ngocok 30x sehari')

@bot.command()
async def greet(ctx, *, name):
    try:
        await ctx.send(f'Halo, {name}!')
    except commands.MissingRequiredArgument:
        await ctx.send('Mohon berikan nama saat menggunakan perintah greet.')

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    avatar_url = member.avatar.url

    embed = discord.Embed(title='Avatar', color=discord.Color.blue())
    embed.set_image(url=avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def event(ctx):
    file_path = 'list_event.txt'  # Ganti dengan path file teks yang sesuai

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        await ctx.send(file_content)
    except FileNotFoundError:
        await ctx.send('File tidak ditemukan.')
    except Exception as e:
        await ctx.send(f'Terjadi kesalahan: {str(e)}')



bot.run(TOKEN)