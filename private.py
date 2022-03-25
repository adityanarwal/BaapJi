import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""𝖳𝗁𝗂𝗌 𝖨𝗌 𝖥𝖺𝗌𝗍𝖾𝗌𝗍 𝖡𝖺𝗇-𝖠𝗅𝗅 𝖡𝗈𝗍 !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝗈𝗎𝗋𝖼𝖾 𝗖𝗈𝖽𝖾", url=f"https://t.me/Its_romeoo")
                ]
                
           ]
        ),
    )
    


