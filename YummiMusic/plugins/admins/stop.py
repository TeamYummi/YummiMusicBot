# 𝗗𝗲𝘃𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 𝗧𝗲𝗮𝗺 𝗬𝘂𝗺𝗺𝗶

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from YummiMusic import app
from YummiMusic.core.call import Yummi
from YummiMusic.utils.database import set_loop
from YummiMusic.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Yummi.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
