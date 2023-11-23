from pyrogram import Client, filters
from helpers.dl import download

@Client.on_message (filters.command(["dl", "download"]))
async def handler (c, m):
    if not len(m.command) >= 2:
        await m.reply ("specify a video url, eg: /dl <video_url>")
    else:
        try:
            buffer = await download(m.command[1])
            await c.reply_video (buffer)
        except Exception as e:
            await m.reply("Invalid url {}".format(e))
