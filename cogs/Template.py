import discord
from discord.ext import commands

class Template(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["testing", "template"])
    async def test(self, ctx):
        await ctx.send(f"Estoy vivo, {ctx.author.name}.")

    @commands.command()
    async def memencion(self, ctx):
        await ctx.send(f"{ctx.author.mention}!!!!")
    
    @commands.command()
    async def primera(self, ctx, word):
        """
        El parámetro word tiene solo la primera palabra
        """
        await ctx.send(f"Has dicho: {word}.")
    
    @commands.command()
    async def dos(self, ctx, primera, segunda):
        """
        Dos parámetros, dos palabras que pillará
        """
        await ctx.send(f"Has dicho: {primera} y luego {segunda}.")

    @commands.command()
    async def echo(self, ctx, *, text):
        """
        Al poner el *, text tendrá todas las palabras
        """
        await ctx.send(f"Todo lo que has dicho es: {text}.")

def setup(bot):
    bot.add_cog(Template(bot))