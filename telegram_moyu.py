# -*- coding: utf-8 -*-
"""
Created on Wed Feb 8 15:37:38 2023

@author: chris
"""

import logging
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
import time

# API Information
api_id = 20294799
api_hash = 'f4cd0bb899a3a774cfa6fea181f78bc3'
delay = 15  # Seconds

# Logging Configuration
logging.basicConfig(level=logging.INFO, filename='telegram_bot.log')

# Initialize Telegram Client
client = TelegramClient('session_file', api_id, api_hash)

async def main():
    await client.start()
    logging.info("You are now AlwaysOnline™, Yah!")
    
    while True:
        await client(UpdateStatusRequest(offline=False))
        logging.debug("Updated status to online. Sleeping for {} seconds...".format(delay))
        time.sleep(delay)

with client:
    client.loop.run_until_complete(main())
