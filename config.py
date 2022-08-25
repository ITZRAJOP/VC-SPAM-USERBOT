# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "3898418"))
API_HASH = os.getenv("API_HASH", "5a82313211da04d63297bd4de436228c")
SESSION = os.getenv("SESSION", "")
OWNER = os.getenv("OWNER", "")
SUPPORT = os.getenv("SUPPORT", "TheDeadlyBots")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))
