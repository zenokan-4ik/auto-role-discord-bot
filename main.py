import discord
import asyncio
import os
import server
import keep_alive

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.content.lower() == "check":
        await message.channel.send("checking....")
        guild = message.guild
        usernames = server.check()
        for username in usernames:
            for member in guild.members:
                if member.name == username[1:] and "Участник SMP" not in [
                        role.name for role in member.roles
                ]:
                    role = discord.utils.get(guild.roles,
                                             id=1252609951730503741)
                    await member.add_roles(role)
                    # p\int(f"{member.name}, {role}")
        print(f"{usernames}")


async def main():
    while True:
        await asyncio.sleep(1800)


async def start():
    await client.wait_until_ready()
    client.loop.create_task(main())


keep_alive.keep_alive()
client.run(TOKEN)
