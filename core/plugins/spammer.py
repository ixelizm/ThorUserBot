
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from core.cmdhelp import CmdHelp

@Client.on_message(filters.command(['spam'], ['!','.','/']) & filters.me)
async def spam(client:Client, message:Message):
    msg = message.text
    msgsplit = msg.split(" ", 2)

    try:
        cmd1 = msgsplit[1]
        cmd2 = msgsplit[2]
        await message.delete()
    except:
        return
    chat_id = message.chat.id
    for _ in range(0, int(cmd1)):
        await client.send_message(chat_id, cmd2)
        await asyncio.sleep(0.7)
CmdHelp("spammer").add_command("spam", "<sayı> <spamlanacak yazı>", "Spam yapar.").add_warning("Sorumluluk kabul etmiyoruz!").add()
