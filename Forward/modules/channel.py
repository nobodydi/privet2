from pyrogram import filters
from config import MOVIES_ID, FORWARD_IDS, SERIES_ID
from Forward import app


x = ["S01","S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "season 01","season 02","season 03","season 04","season 05","season 06","season 07","season 08","season 09","season 10", "season 1","season 2","season 3","season 4","season 5","season 6","season 7","season 8","season 9"]

# -------------------» ᴄʜᴀɴɴᴇʟ «------------------- #

media_filter = filters.document | filters.video | filters.audio

@app.on_message(filters.chat(FORWARD_IDS) & media_filter)
async def media(_, message):
    file_name = message.document.file_name if message.document else \
                message.video.file_name if message.video else \
                message.audio.file_name if message.audio else None
    print(file_name)
    for keyword in x:
        if keyword in file_name:
            await app.copy_message(chat_id=SERIES_ID, from_chat_id=FORWARD_IDS, message_id=message.id)
            break
    else:
        await app.copy_message(chat_id=MOVIES_ID, from_chat_id=FORWARD_IDS, message_id=message.id)


