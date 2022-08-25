import asyncio
from pytgcalls import idle
from VCRAID import call_py, bot
from config import SUPPORT

async def main():
    await call_py.start()
    await bot.join_chat("TheDeadlyBots")
    await bot.join_chat("TheBotUpdates")
    await bot.send_message(
            SUPPORT,
            "<b>VCRAID UserBot Successfully Deployed And Started!</b>")
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @THEDEADLYBOTS |
    ------------------
"""
    )
    await idle()   

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
