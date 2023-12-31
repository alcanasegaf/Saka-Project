# Saka - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Saka/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Saka/blob/main/LICENSE/>.

from importlib import util
from sys import modules

# for addons
configPaths = [
    "ub",
    "var",
    "support",
    "userbot",
    "telebot",
    "fridaybot",
    "uniborg.util",
    "telebot.utils",
    "userbot.utils",
    "userbot.events",
    "userbot.config",
    "fridaybot.utils",
    "fridaybot.Config",
    "userbot.uniborgConfig",
]


def load_addons(plugin_name):
    base_name = plugin_name.split("/")[-1].split("\\")[-1].replace(".py", "")
    if base_name.startswith("__"):
        return
    from Saka import fns

    from .. import HNDLR, LOGS, asst, saka_bot, udB
    from .._misc import _supporter as config
    from .._misc._assistant import asst_cmd, callback, in_pattern
    from .._misc._decorators import saka_cmd
    from .._misc._supporter import Config, admin_cmd, sudo_cmd
    from .._misc._wrappers import eod, eor
    from ..configs import Var
    from ..dB._core import HELP

    name = plugin_name.replace("/", ".").replace("\\", ".").replace(".py", "")
    spec = util.spec_from_file_location(name, plugin_name)
    mod = util.module_from_spec(spec)
    for path in configPaths:
        modules[path] = config
    modules["Saka.functions"] = fns
    mod.LOG_CHANNEL = udB.get_key("LOG_CHANNEL")
    mod.udB = udB
    mod.asst = asst
    mod.tgbot = asst
    mod.saka_bot = saka_bot
    mod.ub = saka_bot
    mod.bot = saka_bot
    mod.ayra = saka_bot
    mod.borg = saka_bot
    mod.telebot = saka_bot
    mod.jarvis = saka_bot
    mod.friday = saka_bot
    mod.eod = eod
    mod.edit_delete = eod
    mod.LOGS = LOGS
    mod.in_pattern = in_pattern
    mod.hndlr = HNDLR
    mod.handler = HNDLR
    mod.HNDLR = HNDLR
    mod.CMD_HNDLR = HNDLR
    mod.Config = Config
    mod.Var = Var
    mod.eor = eor
    mod.edit_or_reply = eor
    mod.asst_cmd = asst_cmd
    mod.saka_cmd = saka_cmd
    mod.on_cmd = saka_cmd
    mod.callback = callback
    mod.Redis = udB.get_key
    mod.admin_cmd = admin_cmd
    mod.sudo_cmd = sudo_cmd
    mod.HELP = HELP.get("Addons", {})
    mod.CMD_HELP = HELP.get("Addons", {})

    spec.loader.exec_module(mod)
    modules[name] = mod
    doc = modules[name].__doc__.format(i=HNDLR) if modules[name].__doc__ else ""
    if "Addons" in HELP.keys():
        update_cmd = HELP["Addons"]
        try:
            update_cmd.update({base_name: doc})
        except BaseException:
            pass
    else:
        try:
            HELP.update({"Addons": {base_name: doc}})
        except BaseException:
            pass
