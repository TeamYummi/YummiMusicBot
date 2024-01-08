# 𝗗𝗲𝘃𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 𝗧𝗲𝗮𝗺 𝗬𝘂𝗺𝗺𝗶

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YummiMusic import LOGGER, app, userbot
from YummiMusic.core.call import Yummi
from YummiMusic.plugins import ALL_MODULES
from YummiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("YummiMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("YummiMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YummiMusic.plugins" + all_module)
    LOGGER("Yummimusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Yummi.start()
    try:
        await Yummi.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("YummiMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Yummi.decorators()
    LOGGER("YummiMusic").info("Yummi Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("YummiMusic").info("Stopping Yummi Music Bot! GoodBye")
