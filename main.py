from pyrogram import Client
from helpers.config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "ytdl",
    api_id = API_ID,
    api_hash = API_ID,
    bot_token = BOT_TOKEN,
    plugins = {
        "root": "plugins"
    }
)

app.run()
