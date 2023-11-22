from pyrogram import Client, filters

MESSAGE = """List of available commands:

/start : to start the bot
/help : sends this message
"""

@Client.on_message(filters.command("help"))
async def handler (c, m):
    print(m)
    await m.reply(MESSAGE)
