from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from config import SUDO_USERS as sudo_user
from VCRAID.tgcalls.handlers import skip_current_song, skip_item
from VCRAID.tgcalls.queues import QUEUE, clear_queue




@Client.on_message(filters.user(sudo_user) & filters.command(["end"], [".", "!", "/"]))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)

@Client.on_message(filters.user(sudo_user) & filters.command(["pause"], [".", "!", "/"]))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
                    

@Client.on_message(filters.user(sudo_user) & filters.command(["resume"], [".", "!", "/"]))
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
