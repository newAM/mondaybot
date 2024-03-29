import argparse
import asyncio
import discord
import sys

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(704512791133814929)
    await channel.send("Games tonight?")
    sys.exit(0)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token-file", help="Path to the token file")
    args = parser.parse_args()

    with open(args.token_file, "r") as f:
        token = f.read().rstrip()

    async with client:
        await asyncio.gather(client.start(token), my_background_task())


def entry():
    asyncio.run(main())
