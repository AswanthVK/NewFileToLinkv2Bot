# This file is a part of TG-FileStreamBot

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters
from WebStreamer.utils.Translation import Language, BUTTON
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    # lang = getattr(Language, m.from_user.language_code)
    lang = getattr(Language, "en")
    await m.reply_text(
        text=lang.START_TEXT.format(m.from_user.mention),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True #,
        #reply_markup=BUTTON.START_BUTTONS
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    # lang = getattr(Language, update.from_user.language_code)
    lang = getattr(Language, "en")
    await update.reply_text(
        text=lang.ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True #,
        #reply_markup=BUTTON.ABOUT_BUTTONS
    )


@StreamBot.on_message((filters.command('help')) & filters.private)
async def help_handler(bot, message):
    # lang = getattr(Language, message.from_user.language_code)
    lang = getattr(Language, "en")
    await message.reply_text(
        text=lang.HELP_TEXT.format(Var.UPDATES_CHANNEL),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True #,
        #reply_markup=BUTTON.HELP_BUTTONS
        )
