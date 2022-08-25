# --------------------------------LICENSE-------------------------
# Files Under @TheDeadlyBots Kang With Credit 
# This File Is Licensed Under GNU 3.0 
# original repo is https://github.com/Team-Deadly
# for any support join @TheDeadlyBots
# ---------------------------------IMPORT--------------------------

import asyncio
from config import HNDLR
from VCRAID IMPORT bot, call_py
from pytgcalls import StreamType
from pyrogram.types import Message
from pyrogram import Client, filters
from VCRAID.helpers.queues import QUEUE, add_to_queue, get_queue
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped




#-------------------------------------CODES-------------------------

@Client.on_message(filters.command(["mc"], prefixes=f"{HNDLR}"))
async def playfrom(client, m: Message):
    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.delete()
        await bot.send_message(
                          chat_id=OWNER_ID,
                          "**USES:** /mc source chat_id example `/mc -1234567890`"           
        )
    else:
        args = m.text.split(maxsplit=1)[1]
        if ";" in args:
            chat = args.split(";")[0]
            limit = int(args.split(";")[1])
        else:
            chat = args
            limit = 10
            lmt = 9
        blaze = await bot.send_message(chat_id=OWNER_ID, "**Vc Raid Starting With {limit} Audios From That Channel!**")
        try:
            async for x in bot.search_messages(chat, limit=limit, filter="audio"):
                location = await x.download()
                if x.audio.title:
                    songname = x.audio.title[:30] + "..."
                else:
                    songname = x.audio.file_name[:30] + "..."
                link = x.link
                if chat_id in QUEUE:
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                else:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(location),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                    # await m.reply_to_message.delete()
                    await bot.send_message(
                                           chat_id=OWNER_ID,
                                           f"**Started Raid In**`{chat_id}` !"
                    )
        except Exception as e:
            await bot.send_message(chat_id=OWNER_ID, f"**ERROR** \n`{e}`")

