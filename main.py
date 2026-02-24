import os
import sys
import random
import asyncio
import time

# Set timezone to fix Pyrogram error
os.environ['TZ'] = 'Asia/Singapore'
try:
    time.tzset()
except:
    pass

from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2
from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from Zaid.Database import db
from Zaid.main import *



# Create Pyrogram clients with sleep_threshold
app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=30,  # Important for time sync
    workers=10
)

if SESSION2:
    app2 = Client(
        SESSION2,
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        sleep_threshold=30,
        workers=10
    )
else:
    app2 = None

# Create PyTgCalls clients
call = PyTgCalls(app)
if app2:
    call2 = PyTgCalls(app2)
else:
    call2 = None

async def start_bot():
    """Start the bot and all services"""
    print("Starting bot...")
    
    # Start Pyrogram clients
    await app.start()
    print("Bot client started")
    
    if app2:
        await app2.start()
        print("Second client started")
    
    # Start PyTgCalls clients
    await call.start()
    print("Voice client started")
    
    if call2:
        await call2.start()
        print("Second voice client started")
    
    print("Bot is now running!")
    
    # Keep the bot running
    await idle()
    
    # Stop everything when done
    await call.stop()
    if call2:
        await call2.stop()
    await app.stop()
    if app2:
        await app2.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Error: {e}")
