# Saka - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Saka/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Saka/blob/main/LICENSE/>.

"""
Exceptions which can be raised by Saka Itself.
"""


class SakaError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(SakaError):
    ...
