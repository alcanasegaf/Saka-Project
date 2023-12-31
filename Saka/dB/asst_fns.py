# Saka - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Saka/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Saka/blob/main/LICENSE/>.

from .. import udB


def get_all_users(key):
    return udB.get_key(key) or []


def is_added(id_):
    return id_ in get_all_users("BOT_USERS")


def add_user(id_):
    users = get_all_users("BOT_USERS")
    users.append(id_)
    return udB.set_key("BOT_USERS", users)


def is_blacklisted(id_):
    return id_ in get_all_users("BOT_BLS")


def blacklist_user(id_):
    users = get_all_users("BOT_BLS")
    users.append(id_)
    return udB.set_key("BOT_BLS", users)


def rem_blacklist(id_):
    users = get_all_users("BOT_BLS")
    users.remove(id_)
    return udB.set_key("BOT_BLS", users)
