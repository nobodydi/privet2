import os
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from config import SUDO_USERS, SERIES_ID, MOVIES_ID, FORWARD_IDS
from Forward import app
from pyromod import listen
from Forward.modules.channel import x

lock = asyncio.Lock()


@app.on_message(filters.command("idex") & filters.user(SUDO_USERS))
async def batch(client, message):
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
            for message_id in message_ids:
                lol = await client.get_messages(chat_id, message_id)
                file_name = None
                if not file_name:
                    if "document" in lol:
                        file_name = lol.document.file_name
                    elif "video" in lol:   
                        file_name = lol.video.file_name
                
                print(file_name)
                for keyword in x:
                    await asyncio.sleep(0.5)
                    if keyword in file_name:
                        try:
                            await asyncio.sleep(1)
                            await app.copy_message(chat_id=SERIES_ID, from_chat_id=FORWARD_IDS, message_id=message_id)
                            break
                        except Exception as e:
                            print(f"Failed to copy message {msg_id}: {e}")
                            continue
                else:
                    try:
                        await asyncio.sleep(1)
                        await app.copy_message(chat_id=MOVIES_ID, from_chat_id=FORWARD_IDS, message_id=message_id)
                    except Exception as e:
                        print(f"Failed {message_id}: {e}")
                        continue           
        except Exception as e:
            print(f"Error: {e}")


          


                
