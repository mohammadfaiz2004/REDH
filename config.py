import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "E_T_B")
ALIVE_NAME = getenv("ALIVE_NAME", "BOB")
BOT_USERNAME = getenv("BOT_USERNAME", "xsongsbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXSONGS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xb_bk")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xb_bp")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ف ب غ س ك و م ا ت / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://t.me/xb_bp")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mohammadfaiz2004/REDH")
IMG_1 = getenv("IMG_1", "https://t.me/xb_bp")
IMG_2 = getenv("IMG_2", "https://t.me/xb_bp")
IMG_3 = getenv("IMG_3", "https://t.me/xb_bp")
