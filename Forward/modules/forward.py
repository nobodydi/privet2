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
                await client.get_messages(chat_id, last_msg_id)
                break
            except Exception as e:
                await last_msg.reply_text(f"<code>This is an invalid message, either the channel is private and bot is not an admin in the forwarded chat, or you forwarded messages as copy.\nError: {e}</code>")
                continue

        msg = await message.reply('Processing...⏳')
        total_files = 0
        async with lock:
            try:
                total = last_msg_id + 1
                current = int(os.environ.get("SKIP", 2))
                nyav = 0
                while True:
                    try:
                        message = await client.get_messages(chat_id=chat_id, message_ids=current, replies=0)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        message = await client.get_messages(chat_id, current, replies=0)
                    except Exception as e:
                        print(e)
                    try:
                        for file_type in ("document", "video", "audio"):
                            media = getattr(message, file_type, None)
                            if media is not None:
                                break
                        else:
                            continue
                        media.file_type = file_type
                        media.caption = message.caption
                        for keyword in x:
                            if keyword in media.caption:
                                await app.copy_message(chat_id=SERIES_ID, from_chat_id=FORWARD_IDS, message_id=message.id)
                                break
                        else:
                            await app.copy_message(chat_id=MOVIES_ID, from_chat_id=FORWARD_IDS, message_id=message.id)
        
                        total_files += 1
                    except Exception as e:
                        print(e)
                    current += 1
                    nyav += 1
                    if nyav == 20:
                        await msg.edit(f"🖨️ Total messages fetched: {current}\n🎬 Total messages saved: {total_files}")
                        nyav -= 20
                    if current == total:
                        break
                await msg.edit(f"🎬 Total {total_files} saved to database")
            except Exception as e:
                print(e)
                await msg.edit(f'Error: {e}')



                                        
