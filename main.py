import os
import sys
import random
import asyncio
import time
import subprocess

# ============================================
# CRITICAL: Force time synchronization first
# ============================================
print("🕐 Syncing system time...")

# Try multiple NTP servers
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

# Set timezone
os.environ['TZ'] = 'Asia/Singapore'
try:
    time.tzset()
except:
    pass

# Print current time for debugging
print(f"📅 Current system time: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# ============================================
# Imports
# ============================================
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2
from pyrogram import Client
from pyrogram.enums import ParseMode
from pytgcalls import PyTgCalls, idle
from Zaid.Database import db
from Zaid.main import *

# ============================================
# Pyrogram Client Configuration
# ============================================
print("🤖 Initializing bot clients...")

# Main client with all fixes
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=60,           # Increased for better time sync
    workers=20,                    # More workers for better performance
    max_concurrent_transmissions=10,
    parse_mode=ParseMode.HTML,
    in_memory=True                 # Don't use session files
)

# Second client if available
if SESSION2:
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
else:
    app2 = None

# ============================================
# PyTgCalls Clients
# ============================================
print("🎵 Initializing voice clients...")

call = PyTgCalls(app, sleep_threshold=60)
if app2:
    call2 = PyTgCalls(app2, sleep_threshold=60)
else:
    call2 = None

# ============================================
# Startup Function
# ============================================
async def start_bot():
    """Start the bot and all services"""
    try:
        print("\n" + "="*50)
        print("🚀 Starting Zaid VC Bot...")
        print("="*50 + "\n")
        
        # Start Pyrogram clients
        print("📱 Connecting to Telegram...")
        await app.start()
        me = await app.get_me()
        print(f"  ✓ Bot: @{me.username} (ID: {me.id})")
        
        if app2:
            await app2.start()
            me2 = await app2.get_me()
            print(f"  ✓ Second client: @{me2.username}")
        
        # Start PyTgCalls clients
        print("\n🎵 Starting voice clients...")
        await call.start()
        print("  ✓ Voice client started")
        
        if call2:
            await call2.start()
            print("  ✓ Second voice client started")
        
        print("\n" + "="*50)
        print("✅ Bot is now running!")
        print("="*50 + "\n")
        
        # Keep the bot running
        await idle()
        
    except Exception as e:
        print(f"\n❌ Error during startup: {e}")
        raise
    finally:
        # Cleanup
        print("\n🛑 Shutting down...")
        
        if call2:
            await call2.stop()
        await call.stop()
        
        if app2:
            await app2.stop()
        await app.stop()
        
        print("✓ Bot stopped successfully")

# ============================================
# Main Entry Point
# ============================================
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n💥 Fatal error: {e}")
        sys.exit(1)
    finally:
        loop.close()
