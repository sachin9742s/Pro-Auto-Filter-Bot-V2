#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT & @sachin_official_admin

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot import UPDATE_CHANNEL # Update Text Message Channel Update
from bot import MRK_YT_MASTER
from bot import MT_GROUP
from bot import MT_CHANNEL # Main Channel Added


db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("๐ Sorry Dude, You are **๐ฑ๏ธ๐ฐ๏ธ๐ฝ๏ธ๐ฝ๏ธ๐ด๏ธ๐ณ๏ธ ๐คฃ๐คฃ๐คฃ**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>๐ ๐๐ผ๐ถ๐ป ๐ข๐๐ฟ ๐ ๐ฎ๐ถ๐ป ๐ฐ๐ต๐ฎ๐ป๐ป๐ฒ๐น ๐คญ.\n\nHello Join Our Main Channel? Please Join My Updates Channel to use this Bot!๐\n And  start Me..!๐</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ๐ข ๐น๐๐๐ ๐ผ๐ข ๐๐๐๐๐๐๐ ๐ฒ๐๐๐๐๐๐ ๐ข ", url=f"https://t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>๐ข เด เดเดพเดจเดฒเดฟเตฝ  @{UPDATE_CHANNEL} เดฌเตเดเตเดเดฟเดจเต เดเดกเตเดฎเดฟเตป เดเดเต. เดเดจเตเดจเดฟเดเตเดเต /start เดเตเดเตเดเต</b>\n\n<b>๐ฃ๏ธ any Doubt @KicchaRequest</b>")
            return  
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐Join Main Channel๐', url=f"{MT_CHANNEL}"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '๐ญ DEVELOPER ๐ญ', url="https://t.me/KicchaRequest"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐จโ๐ผ ๐ณ๐๐๐๐๐๐๐๐๐ ๐จโ๐ผ', url="https://t.me/GD_FILMCLUB"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐จโ๐ผ ๐ณ๐๐๐๐๐๐๐๐๐ ๐จโ๐ผ', url="https://t.me/GD_FILMCLUB"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('๐จโ๐ผCreater', url=f'https://t.me/{MRK_YT_MASTER}'),
        InlineKeyboardButton('Help ๐ค', callback_data="help")
    ],[
        InlineKeyboardButton('๐ฃ๏ธGroup', url=f'{MT_GROUP}'),
        InlineKeyboardButton('Channel๐', url=f'{MT_CHANNEL}')
    ],[
        InlineKeyboardButton('๐ฅ๏ธ OTT MOVIES ๐ฅ๏ธ', url='https://t.me/KR_ROCKERS_DVD_WEB_OTT_MOVIES')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
     )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('๐  ๐ท๐๐๐', callback_data='start'),
        InlineKeyboardButton('๐ฐ๐๐๐๐ ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('๐ ๐ฒ๐๐๐๐ ๐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton("ใ   Add Me To Your Group โ", url="https://t.me/Vijay_ProBot?startgroup=true"),
    ],[
        InlineKeyboardButton('๐ค Request Group ๐ค', url='https://t.me/KicchaRequest'),
        InlineKeyboardButton('MOVIE CHAMMEL ๐ค', url='https://t.me/GD_FILMCLUB')
    ],[
        InlineKeyboardButton('๐ค SACHIN S ๐ค', url='https://t.me/sachin_official_admin')
    ],[
        InlineKeyboardButton('๐  Home', callback_data='start'),
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
