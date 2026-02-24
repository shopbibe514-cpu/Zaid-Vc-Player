import asyncio
import os
import sys
import logging
import traceback
from pytgcalls import idle
from Zaid.Database import db

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)

try:
    from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
except ImportError:
    LOGGER.error("Failed to import config! Please check config.py file.")
    sys.exit(1)

from pyrogram import Client
from pyrogram.enums import ParseMode
from pytgcalls import PyTgCalls
from Zaid.main import start_bot

# ============================================
# Client Initialization
# ============================================
LOGGER.info("Initializing bot clients...")

# Main client
try:
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
    LOGGER.info("✅ Main client initialized")
except Exception as e:
    LOGGER.error(f"Failed to initialize main client: {e}")
    sys.exit(1)

# Second client (if available)
app2 = None
if SESSION2 and SESSION2 != "None" and SESSION2 != "None":
    try:
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
        LOGGER.info("✅ Second client initialized")
    except Exception as e:
        LOGGER.warning(f"Failed to initialize second client: {e}")

# ============================================
# PyTgCalls Initialization
# ============================================
try:
    call = PyTgCalls(app, sleep_threshold=60)
    LOGGER.info("✅ Voice client initialized")
except Exception as e:
    LOGGER.error(f"Failed to initialize voice client: {e}")
    sys.exit(1)

call2 = None
if app2:
    try:
        call2 = PyTgCalls(app2, sleep_threshold=60)
        LOGGER.info("✅ Second voice client initialized")
    except Exception as e:
        LOGGER.warning(f"Failed to initialize second voice client: {e}")

# ============================================
# Main Function
# ============================================
async def main():
    """Main async function"""
    try:
        LOGGER.info("="*50)
        LOGGER.info("Starting Zaid VC Bot...")
        LOGGER.info("="*50)
        
        # Start main client
        LOGGER.info("Starting main client...")
        await app.start()
        me = await app.get_me()
        LOGGER.info(f"✅ Bot started: @{me.username} (ID: {me.id})")
        
        # Start second client if available
        if app2:
            LOGGER.info("Starting second client...")
            await app2.start()
            me2 = await app2.get_me()
            LOGGER.info(f"✅ Second client started: @{me2.username}")
        
        # Start voice clients
        LOGGER.info("Starting voice client...")
        await call.start()
        LOGGER.info("✅ Voice client started")
        
        if call2:
            LOGGER.info("Starting second voice client...")
            await call2.start()
            LOGGER.info("✅ Second voice client started")
        
        LOGGER.info("="*50)
        LOGGER.info("✅ Bot is now running!")
        LOGGER.info("="*50)
        
        # Keep bot running
        await idle()
        
    except Exception as e:
        LOGGER.error(f"❌ Error in main: {e}")
        traceback.print_exc()
        raise
    finally:
        # Cleanup
        LOGGER.info("Shutting down...")
        
        if call2:
            await call2.stop()
        await call.stop()
        
        if app2:
            await app2.stop()
        await app.stop()
        
        LOGGER.info("✅ Bot stopped successfully")

# ============================================
# Entry Point
# ============================================
if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        LOGGER.info("👋 Bot stopped by user")
    except Exception as e:
        LOGGER.error(f"💥 Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        try:
            loop.close()
        except:
            pass
