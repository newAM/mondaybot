import argparse
import discord
import sys

client = discord.Client()


async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id=704512791133814929)
    await channel.send("Games tonight?")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token-file", help="Path to the token file")
    args = parser.parse_args()

    with open(args.token_file, "r") as f:
        token = f.read().rstrip()

    client.loop.create_task(my_background_task())
    client.run(token)


if __name__ == "__main__":
    main()
