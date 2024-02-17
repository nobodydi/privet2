import os
import asyncio
import threading
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS, SERIES_ID, MOVIES_ID, FORWARD_IDS
from Forward import app
from pyromod import listen
from Forward.modules.channel import x

lock = asyncio.Lock()

async def file_finder(app, chat_id, msg_id):
    lol = await app.get_messages(chat_id, msg_id)
    file_name = None
    if lol:
        if lol.document:
            file_name = lol.document.file_name
            return file_name
        elif lol.video:
            file_name = lol.video.file_name
            return file_name
        else:
            return "No media found in the message."
    else:
        return "No message found with the given ID."

def process_messages(client, message_ids, chat_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(batch(client, message_ids, chat_id))
    except Exception as e:
        print(f"Error in processing messages: {e}")

@app.on_message(filters.command("idex") & filters.user(SUDO_USERS))
async def start_batch(client, message):
    if lock.locked():
        await message.reply("<code>Wait until previous process completes.</code>")
    else:
        try:
            last_msg = await client.ask(
                text="<code>Forward last message from DB channel (with quotes)\n\nor send the DB channel post link</code>",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
            last_msg_id = last_msg.forward_from_message_id
            chat_id = last_msg.forward_from_chat.username or last_msg.forward_from_chat.id
        except Exception as e:
            await last_msg.reply_text(f"Error: {e}")
            return
        
        try:
            message_ids = [i for i in range(int(last_msg_id) + 1)]
            await asyncio.sleep(0.5)
            threading.Thread(target=process_messages, args=(client, message_ids, chat_id)).start()
        except Exception as e:
            print(f"Error: {e}")

async def batch(client, message_ids, chat_id):
    async with lock:
        for message_id in message_ids:
            try:
                x = await file_finder(app, FORWARD_IDS, message_id)
                print(x)
                await asyncio.sleep(1)
                await app.copy_message(chat_id=MOVIES_ID, from_chat_id=FORWARD_IDS, message_id=message_id)
            except Exception as e:
                print(f"Failed {message_id}: {e}")
                continue


