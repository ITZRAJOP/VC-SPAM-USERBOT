from config import *
from pytgcalls import PyTgCalls
from pyrogram import Client, filters

API_ID = API_ID
API_HASH = API_HASH
SESSION_NAME = SESSION_NAME
SUDO_USERS = SUDO_USERS
LOG_GROUP = LOG_GROUP

DEADLY_VERSION = "0.0.1"


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCRAID.plugins"))
call_py = PyTgCalls(bot)
