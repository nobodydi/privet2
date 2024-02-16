from pyrogram import filters
from Forward import app

@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_text(f"Hello {message.from_user.mention} Under in maintainance.")
