import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""π³πππ π¨π π₯πΊπππΎππ π‘πΊπ-π ππ π‘ππ !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π¦ππππΌπΎ πππ½πΎ", url=f"https://t.me/Its_romeoo")
                ]
                
           ]
        ),
    )
