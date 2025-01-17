import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types import MediaStream, AudioQuality, Update
from YukkiMusic.utils.thumbnails import gen_thumb
from YukkiMusic.misc import clonedb
from .utils.active import _clear_
from .play import pytgcalls

welcome = 20
close = 30


@Client.on_message(filters.video_chat_started, group=welcome)
@Client.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass


@pytgcalls.on_left()
@pytgcalls.on_kicked()
@pytgcalls.on_closed_voice_chat()
async def handler(_, update: Update):
    try:
        chat_id = update.chat_id
        await _clear_(chat_id)
    except Exception as e:
        logging.exception(e)
