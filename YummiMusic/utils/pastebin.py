# 𝗗𝗲𝘃𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 𝗧𝗲𝗮𝗺 𝗬𝘂𝗺𝗺𝗶

import aiohttp

BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def Yummibin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link
