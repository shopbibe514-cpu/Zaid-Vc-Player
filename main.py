import os
import sys
import asyncio
import time
import subprocess
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

# ============================================
# CRITICAL: Force time synchronization first
# ============================================
print("🕐 Syncing system time...")

ntp_servers = [
    'pool.ntp.org',
    'time.google.com',
    'time.facebook.com',
    'time.apple.com',
    'asia.pool.ntp.org'
]

for server in ntp_servers:
    try:
        subprocess.run(
            ['ntpdate', '-u', server], 
            timeout=5, 
            check=False,
            capture_output=True
        )
        print(f"  ✓ Synced with {server}")
    except:
        pass

os.environ['TZ'] = 'Asia/Singapore'
try:
    time.tzset()
except:
    pass

print(f"📅 Current system time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================
# Get configuration from environment variables first
# ============================================
print("🔑 Loading configuration...")

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
SESSION_NAME = os.environ.get('SESSION_NAME', 'ZaidVCBot')
SESSION2 = os.environ.get('SESSION2', None)

if not API_ID or not API_HASH or not BOT_TOKEN:
    try:
        from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2
        print("  ✓ Loaded from config.py")
    except ImportError:
        print("❌ ERROR: Missing API_ID, API_HASH, or BOT_TOKEN!")
        sys.exit(1)
else:
    try:
        API_ID = int(API_ID)
    except ValueError:
        print("❌ ERROR: API_ID must be an integer!")
        sys.exit(1)
    print("  ✓ Loaded from environment variables")

print(f"  ✓ Bot Token: {BOT_TOKEN[:10]}...")
print(f"  ✓ Session: {SESSION_NAME}")

# ============================================
# Imports
# ============================================
from pyrogram import Client
from pyrogram.enums import ParseMode
from pytgcalls import PyTgCalls, idle

# ============================================
# Pyrogram Client Configuration
# ============================================
print("🤖 Initializing bot clients...")

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=60,
    workers=20,
    max_concurrent_transmissions=10,
    parse_mode=ParseMode.HTML,
    in_memory=True
)

app2 = None
if SESSION2 and SESSION2 != "None":
    app2 = Client(
        SESSION2,
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        sleep_threshold=60,
        workers=20,
        max_concurrent_transmissions=10,
        parse_mode=ParseMode.HTML,
        in_memory=True
    )

# ============================================
# PyTgCalls Clients
# ============================================
print("🎵 Initializing voice clients...")

call = PyTgCalls(app)
call2 = PyTgCalls(app2) if app2 else None

# ============================================
# Startup Function
# ============================================
async def start_bot():
    try:
        print("\n" + "="*50)
        print("🚀 Starting Zaid VC Bot...")
        print("="*50 + "\n")
        
        print("📱 Connecting to Telegram...")
        await app.start()
        me = await app.get_me()
        print(f"  ✓ Bot: @{me.username} (ID: {me.id})")
        
        if app2:
            await app2.start()
            me2 = await app2.get_me()
            print(f"  ✓ Second client: @{me2.username}")
        
        print("\n🎵 Starting voice clients...")
        await call.start()
        print("  ✓ Voice client started")
        
        if call2:
            await call2.start()
            print("  ✓ Second voice client started")
        
        print("\n" + "="*50)
        print("✅ Bot is now running!")
        print("="*50 + "\n")
        
        await idle()
        
    except Exception as e:
        print(f"\n❌ Error during startup: {e}")
        LOGGER.exception("Startup error")
        raise
    finally:
        print("\n🛑 Shutting down...")
        
        if app2:
            await app2.stop()
        await app.stop()
        
        print("✓ Bot stopped successfully")

# ============================================
# Main Entry Point
# ============================================
if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n💥 Fatal error: {e}")
        LOGGER.exception("Fatal error")
        sys.exit(1)
