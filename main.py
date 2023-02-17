import discord
import asyncio
import datetime

# Set the initial date
current_date = datetime.date(1985, 1, 1)

# Create a Discord client with required intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Define a function to update the date
async def update_date():
    global current_date
    while True:
        current_date += datetime.timedelta(days=1)
        channel = client.get_channel(1075167105076428942)
        await channel.send(f"The date is {current_date.strftime('%B %d, %Y')}")
        await asyncio.sleep(27.62 * 60)  # wait for 27.62 minutes

# Define an event for when the client is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Find the channel to send messages to
    channel = client.get_channel(1075167105076428942)

    # Send the initial message with the starting date
    await channel.send(f"The date is {current_date.strftime('%B %d, %Y')}")

    # Start updating the date
    client.loop.create_task(update_date())

# Run the client
client.run("MTA3NTE2NDM0MzQ0MTgzNDAxNA.GvDdxv.S6N9A6aSujJey60QZJLr1UAm683juCnb6Fm78s")
