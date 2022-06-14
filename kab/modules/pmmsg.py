# Copyright (©️) @ONLY_DUSKY
# By : Dusky Joe

from pyrogram import Client
from kab.tgcalls import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from kab.config import (
    BOT_USERNAME,
)

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hey 👋 I am the Kutty Angel's assistant of Kutty Angel music bot, didn't have a time to talk with you 🙂 kindly join @DuskyBotZUpdates for getting support\n\nPowered by @DuskyBotZSupport")
  return
