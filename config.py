## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
import sys
import logging
from os import getenv
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

# ============================================
# Session Variables
# ============================================
SESSION_NAME = getenv("SESSION_NAME", "ZaidVCBot")

def get_session(session_num):
    """Helper function to get session strings"""
    session = getenv(f"STRING_SESSION{session_num}", "")
    return str(None) if not session or session.strip() == "" else session

SESSION2 = get_session("2")
SESSION3 = get_session("3")
SESSION4 = get_session("4")
SESSION5 = get_session("5")

# ============================================
# Required Credentials
# ============================================
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

try:
    API_ID = int(getenv("API_ID", "0"))
except ValueError:
    API_ID = 0
    LOGGER.error("Invalid API_ID! Please check your environment variables.")

API_HASH = getenv("API_HASH", "")

# ============================================
# MongoDB
# ============================================
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
if not MONGO_DB_URL:
    LOGGER.warning("MONGO_DB_URL is not set! Database features may not work.")

# ============================================
# Owner Information
# ============================================
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Zaid2_Robot")

try:
    OWNER_ID = int(getenv("OWNER_ID", "1669178360"))
except ValueError:
    OWNER_ID = 1669178360
    LOGGER.warning("Invalid OWNER_ID, using default.")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid2_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")

# ============================================
# Heroku (Optional)
# ============================================
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ============================================
# Sudo Users & Commands
# ============================================
try:
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
except ValueError:
    SUDO_USERS = [1669178360]
    LOGGER.warning("Invalid SUDO_USERS, using default.")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

# ============================================
# Images & Media
# ============================================
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")

# ============================================
# Limits
# ============================================
try:
    DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
except ValueError:
    DURATION_LIMIT = 60
    LOGGER.warning("Invalid DURATION_LIMIT, using default (60).")

# ============================================
# Upstream Repo
# ============================================
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")

# ============================================
# Heroku Mode
# ============================================
HEROKU_MODE = getenv("HEROKU_MODE", None)

# ============================================
# Safety Check
# ============================================
MISSING_VARS = []

if not BOT_TOKEN:
    MISSING_VARS.append("BOT_TOKEN")
if not API_ID or API_ID == 0:
    MISSING_VARS.append("API_ID")
if not API_HASH:
    MISSING_VARS.append("API_HASH")
if not MONGO_DB_URL:
    MISSING_VARS.append("MONGO_DB_URL (optional but recommended)")

if MISSING_VARS:
    LOGGER.warning(f"Missing environment variables: {', '.join(MISSING_VARS)}")
    if "BOT_TOKEN" in MISSING_VARS or "API_ID" in MISSING_VARS or "API_HASH" in MISSING_VARS:
        LOGGER.error("Critical variables missing! Bot may not work properly.")
else:
    LOGGER.info("✅ All required config variables loaded successfully!")

# Print status for debugging
if __name__ == "__main__":
    print("="*50)
    print("Config Check:")
    print(f"BOT_TOKEN: {'✓' if BOT_TOKEN else '✗'}")
    print(f"API_ID: {'✓' if API_ID else '✗'}")
    print(f"API_HASH: {'✓' if API_HASH else '✗'}")
    print(f"MONGO_DB_URL: {'✓' if MONGO_DB_URL else '✗'}")
    print("="*50)
