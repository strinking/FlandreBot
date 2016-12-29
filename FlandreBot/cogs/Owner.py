import discord
from discord.ext import commands
import importlib

class unloadError(Exception):
    pass

class unloadOwner(Exception):
    pass

class cogNotFound(Exception):
    pass


class Owner:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def reload(self, ctx, *, module: str):
        """Reload modules."""
        # Get the message sent
        message = ctx.message

        try:
            # Check if user has the manage_server perm
            
            if self.checkAdmin(message.author, message.channel):
                
                # Get the module's cog and check it has a _unload function in it (Must be an async function)
                cog = self.bot.get_cog(module)
                unload_function = getattr(cog, "_unload", None)
                if unload_function is not None:
                    await unload_function()

                self.reloadcog(module)
                await self.bot.say("Done reloading " + module)
            else:
                await self.bot.say("You need the manage server permission")
        except:
            await self.bot.say("something went wrong")

            
    @commands.command(pass_context=True)
    async def load(self, ctx, *, module: str):
        """Reload modules."""
        # Get the message sent
        message = ctx.message

        try:
            # Check if user has the manage_server perm
            
            if self.checkAdmin(message.author, message.channel):
                self.loadcog(module)
                await self.bot.say("Done loading " + module)
            else:
                await self.bot.say("You need the manage server permission")
        except:
            await self.bot.say("something went wrong")
    
    @commands.command(pass_context=True)    
    async def unload(self, ctx, *, module: str):
        """Reload modules."""
        # Get the message sent
        message = ctx.message

        try:
            # Check if user has the manage_server perm
            
            if self.checkAdmin(message.author, message.channel):
                
                # Get the module's cog and check it has a _unload function in it (Must be an async function)
                cog = self.bot.get_cog(module)
                unload_function = getattr(cog, "_unload", None)
                if unload_function is not None:
                    await unload_function()

                self.unloadcog(module)
                await self.bot.say("Done unloading " + module)
            else:
                await self.bot.say("You need the manage server permission")
        except:
            await self.bot.say("something went wrong")
    
    #reload function
    def reloadcog(self, cog):
        if not "FlandreBot.cogs." in cog:
            cog = "FlandreBot.cogs." + cog
        self.bot.unload_extension(cog)
        self.bot.load_extension(cog)
        
    def loadcog(self, cog):
        if not "FlandreBot.cogs." in cog:
            cog = "FlandreBot.cogs." + cog
        self.bot.load_extension(cog)
      
    def unloadcog(self, cog):
        if not "FlandreBot.cogs." in cog:
            cog = "FlandreBot.cogs." + cog
        self.bot.unload_extension(cog)
        
        
    def checkAdmin(self, user, channel):
        return (user.permissions_in(channel).manage_server)
                
                
def setup(bot):
    bot.add_cog(Owner(bot))