PREFIX = 't?'
TOKEN = 'TWÓJ TOKEN'

from discord.ext import commands
import discord 
from random import choice

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')

@bot.command()
async def status(ctx, args):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=args))
    succes = discord.Embed(title=f"Zmieniono status bota na: {args}", color=0x00e6de)

    await ctx.send(embed=succes)

@bot.command()
async def stitch(ctx):
    stitches = [
        "https://static.wikia.nocookie.net/bohaterowie/images/f/f6/Stitch_%28Lilo_%26_Stitch%29.svg.png/revision/latest?cb=20201031124027&path-prefix=pl",
        "https://static.wikia.nocookie.net/disney/images/a/a8/Profile_-_Stitch.jpeg/revision/latest/top-crop/width/360/height/450?cb=20190312072323",
        "https://cdn.shopify.com/s/files/1/0054/4371/5170/products/Stitch_472pin.png?v=1598373624",
        "https://wallpaperaccess.com/full/810731.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1kk6ewuq-ddePN7u-9VjkBuEpWpiDjUuZIA&usqp=CAU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ7BQmoYz1OWZZS1Wi6fWZOhf_gjqdvCBUAQ&usqp=CAU"
    ]

    random_stitch = choice(stitches)
    stitch_embed = discord.Embed(title=f'Gotowe, {ctx.author.name}')
    stitch_embed.set_image(url=random_stitch)

    await ctx.send(embed=stitch_embed)

bot.run(TOKEN)
