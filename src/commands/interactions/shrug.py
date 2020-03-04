import discord


async def handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    response = f'{message.author.display_name} shrugs'

    e = discord.Embed(colour=0xff00e7, title=response)
    e.set_image(url=await bot.tenor.get_interact("anime shrug"))
    await message.channel.send(embed=e)