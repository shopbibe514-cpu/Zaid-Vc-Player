import os
from os import getenv
from dotenv import load_dotenv

# Load environment variables
if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

admins = {}

# ==============================
# Basic Bot Settings
# ==============================

SESSION_NAME = getenv("SESSION_NAME", "ZaidVCBot")
BOT_NAME = getenv("BOT_NAME", "Umk")

# ==============================
# Required Credentials
# ==============================

try:
    API_ID = int(getenv("API_ID", "0"))
except:
    API_ID = 0

API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# ==============================
# Assistant / String Sessions
# ==============================

STRING_SESSION = getenv("STRING_SESSION", "")
SESSION2 = getenv("STRING_SESSION2", "")
SESSION3 = getenv("STRING_SESSION3", "")
SESSION4 = getenv("STRING_SESSION4", "")
SESSION5 = getenv("STRING_SESSION5", "")

# ==============================
# Mongo Database
# ==============================

MONGO_DB_URL = getenv("MONGO_DB_URL", "")

# ==============================
# Owner & Support
# ==============================

OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")

try:
    OWNER_ID = int(getenv("OWNER_ID", "1669178360"))
except:
    OWNER_ID = 1669178360

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid2_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")

# ==============================
# Heroku (Optional)
# ==============================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

# ==============================
# Sudo Users & Commands
# ==============================

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

# ==============================
# Images & Media
# ==============================

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")

# ==============================
# Limits
# ==============================

try:
    DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
except:
    DURATION_LIMIT = 60

# ==============================
# Upstream Repo
# ==============================

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")

# ==============================
# Safety Check (Warnings Only)
# ==============================

missing_vars = []

if not BOT_TOKEN:
    missing_vars.append("BOT_TOKEN")
if not API_ID:
    missing_vars.append("API_ID")
if not API_HASH:
    missing_vars.append("API_HASH")

if missing_vars:
    print("⚠️ Warning: Some required variables are missing!")
    for var in missing_vars:
        print(f"   - {var} is missing!")
    print("Please add them in Render Environment Variables before deploying.")
