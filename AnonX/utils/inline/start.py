from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(text="ʜᴇʟᴩ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="❣ sᴜᴩᴩᴏʀᴛ ❣", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="🥀 ʙᴏᴛ ᴏᴡɴᴇʀ 🥀", user_id=OWNER),
        ], 
        [   
            InlineKeyboardButton(text="🥀 ᴍᴀᴅᴇ ʙʏ 🥀", url="https://t.me/imnot_avanish"),
        ],
        [   
            InlineKeyboardButton(text="🥀 ᴘᴏᴡᴇʀᴇᴅ ʙʏ 🥀", url="https://t.me/Miss_X_Network"),
        ],
     ]
    return buttons
