from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from config import OWNER
from VCRAID.tgcalls.handlers import skip_current_song, skip_item
from VCRAID.tgcalls.queues import QUEUE, clear_queue




@Client.on_message(filters.command(["end"], prefix=","))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await bot.send_message(OWNER, "lawda")
        except Expectations as e:
            await bot.send_message(OWNER, f"{e}")
