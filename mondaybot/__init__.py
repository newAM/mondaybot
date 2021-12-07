import discord
import sys

client = discord.Client()


async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id=704512791133814929)
    await channel.send("Games tonight?")
    sys.exit(0)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


with open("/etc/nixos/discord_token.txt", "r") as f:
    token = f.read().rstrip()

client.loop.create_task(my_background_task())
client.run(token)
