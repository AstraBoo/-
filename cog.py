from discord.ext import commands

class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_text = "Hello, {0.mention}! Welcome to the server!"
        self.welcome_channel = None

    @commands.command()
    async def seth_welcome(self, ctx):
        self.welcome_channel = ctx.message.channel
        await ctx.send("Welcome message channel set to current channel.")

    @commands.command()
    async def seth_w_text(self, ctx, *, text: str):
        self.welcome_text = text
        await ctx.send(f"Welcome message text set to: {text}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if self.welcome_channel:
            welcome_message = self.welcome_text.format(member)
            await self.welcome_channel.send(welcome_message)

          
