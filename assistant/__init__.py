# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from Saka import *
from Saka import _saka_cache
from Saka._misc import owner_and_sudos
from Saka._misc._assistant import asst_cmd, callback, in_pattern
from Saka.fns.helper import *
from Saka.fns.tools import get_stored_file
from telethon import Button, custom

from modules import ATRA_COL, InlinePlugin
from strings import get_languages, get_string

OWNER_NAME = saka_bot.full_name
OWNER_ID = saka_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Ada yang salah`")


def get_back_button(name):
    return [Button.inline("Kembali", data=f"{name}")]
