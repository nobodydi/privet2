from pyrogram import filters
from config import CHANNEL_ID, FORWARD_IDS, OTHER_ID
from Forward import app

# -------------------» ᴄʜᴀɴɴᴇʟ «------------------- #
"""
media_filter = filters.document | filters.video | filters.audio


@app.on_message(filters.chat(FORWARD_IDS) & media_filter)
async def media(_, message):
    await app.copy_message(chat_id=CHANNEL_ID, from_chat_id=FORWARD_IDS, message_id=message.id)

"""


# -------------------» ᴄʜᴀɴɴᴇʟ «------------------- #

media_filter = filters.document | filters.video | filters.audio


@app.on_message(filters.chat(FORWARD_IDS) & media_filter)
async def media(_, message):
    file_name = message.document.file_name if message.document else \
                message.video.file_name if message.video else \
                message.audio.file_name if message.audio else None
    
    if file_name and any(keyword in file_name.lower() for keyword in ["SO1"]):
        await app.copy_message(chat_id=OTHER_ID, from_chat_id=FORWARD_IDS, message_id=message.message_id)
    else:
        await app.copy_message(chat_id=CHANNEL_ID, from_chat_id=FORWARD_IDS, message_id=message.message_id)


