# 𝗗𝗲𝘃𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 𝗧𝗲𝗮𝗺 𝗬𝘂𝗺𝗺𝗶

from pyrogram import filters

import config
from strings import get_command
from YummiMusic import app
from YummiMusic.misc import SUDOERS
from YummiMusic.utils.database import add_off, add_on
from YummiMusic.utils.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@app.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
