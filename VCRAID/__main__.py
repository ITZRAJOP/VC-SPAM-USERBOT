import asyncio
from pytgcalls import idle
from VCRAID import call_py

async def main():
    await call_py.start()
    await bot.send_message(SUPPORT, "**VCRAID UserBot Successfully Deployed And Started**")
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
