import os
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS, SERIES_ID, MOVIES_ID, FORWARD_IDS
from Forward import app
from pyromod import listen
from Forward.modules.channel import x

lock = asyncio.Lock()



@app.on_message(filters.command("index") & filters.user(SUDO_USERS))
async def batch(client, message):
    if lock.locked():
        await message.reply("<code>Wait until previous process completes.</code>")
    else:
        while True:
            last_msg = await client.ask(text="<code>Forward last message from DB channel (with quotes)\n\nor send the DB channel post link</code>", chat_id=message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)        
            try:
                last_msg_id = last_msg.forward_from_message_id
                chat_id = last_msg.forward_from_chat.username or last_msg.forward_from_chat.id
                lol = await client.get_messages(chat_id, last_msg_id)
                await message.reply(lol)
                await message.reply(f"{last_msg_id} {chat_id}")
                break
            except Exception as e:
                await last_msg.reply_text(f"<code>This is an invalid message, either the channel is private and bot is not an admin in the forwarded chat, or you forwarded messages as copy.\nError: {e}</code>")
                continue

       
        
