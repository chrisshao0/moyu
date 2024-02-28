# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:37:38 2023

@author: chris
"""

import logging
import getpass
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest
import time

# API Information
api_id = 20294799
api_hash = 'f4cd0bb899a3a774cfa6fea181f78bc3'
delay = 15  # Second

# Logging Configuration
logging.basicConfig(level=logging.INFO)

# Login to Telegram
logging.info("Trying to Login to Telegram...")
client = TelegramClient('session_file', api_id, api_hash)
client.connect()
if client.is_user_authorized() is not True:
    logging.info('You have not login yet, Trying to log you in...')
    logging.info('if you have 2FA password, please enter right now. This Password will not be stored')
    password = getpass.getpass()
    if password != '':
        client.start(password=password)
    else:
        client.start()

if client.is_user_authorized():
    logging.info("You are now AlwaysOnline™, Yah!")
    while True:
        client(UpdateStatusRequest(offline=False))
        time.sleep(delay)
        logging.debug("Sleep for 1 min")
else:
    logging.fatal("Login Fails, please retry... 失败，请重试！")
