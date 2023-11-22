from pyrogram import Client, filters

MESSAGE = """Hello, {}
Welcome to youtube downloader
use `/help` for the list of available commands
"""


@Client.on_message(filters.command("start"))
async def handler (c, m):
    name = m.chat.first_name
    await m.reply(MESSAGE.format(name))
