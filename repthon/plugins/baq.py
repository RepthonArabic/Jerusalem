# RepthonArabic
# Copyright (C) 2023 RepthonArabic. All Rights Reserved
#
# This file is a part of < https://github.com/RepthonArabic/Repthon/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/Repthon/blob/master/LICENSE/>.
"""سـورس ريبـــثون™
So تخمـط الملـف اهينك واطشك للناس خماط واوثق عليك
Copyright (C) 2023 RepthonArabic. All Rights Reserved
Credit: https://github.com/RepthonArabic/Repthon
Devloper: https://telegram.dog/E_7_V"""
import json
import math
import asyncio
import os
import random
import re
import time
from pathlib import Path
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from telethon.tl.functions.users import GetUsersRequest

from . import zq_lo
from ..Config import Config
from ..helpers import reply_id
from ..sql_helper.globals import gvarstatus
from ..core.logger import logging
from ..helpers.utils import _format
from . import mention

LOGS = logging.getLogger(__name__)
tr = Config.COMMAND_HAND_LER

# Copyright (C) 2023 Baqir . All Rights Reserved
@zq_lo.tgbot.on(InlineQuery)
async def inline_handler(event):
    from .baq import ttt, ddd, bbb, hmm, ymm, fmm, dss, hss, nmm, mnn, bmm, scc
    builder = event.builder
    result = None
    query = event.text
    string = query.lower()
    query.split(" ", 2)
    str_y = query.split(" ", 1)
    string.split()
    query_user_id = event.query.user_id
    user_id = gvarstatus("hmsa_id")
    full_name = gvarstatus("hmsa_name")
    username = gvarstatus("hmsa_user")
    if username.startswith("@"):
        baqir = gvarstatus("hmsa_user")
    else:
        baqir = f"[{full_name}](tg://user?id={user_id})"
    if query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS:  # Code by T.me/E_7_V
        malathid = Config.OWNER_ID
    elif query_user_id == user_id or query_user_id == int(user_id):
        malathid = user_id
    if query_user_id == Config.OWNER_ID or query_user_id == user_id or query_user_id == int(user_id) or query_user_id in Config.SUDO_USERS:  # Code by T.me/E_7_V
        inf = re.compile("secret (.*) (.*)")
        match2 = re.findall(inf, query)
        if match2:
            user_list = []
            baqir = ""
            query = query[7:]
            info_type = [hmm, ymm, fmm]
            if "|" in query:
                iris, query = query.replace(" |", "|").replace("| ", "|").split("|")
                users = iris.split(" ")
            else:
                user, query = query.split(" ", 1)
                users = [user]
            for user in users:
                usr = int(user) if user.isdigit() else user
                try:
                    u = await zq_lo.get_entity(usr)
                except ValueError:
                    u = await zq_lo(GetUsersRequest(usr))
                if u.username:
                    baqir += f"@{u.username}"
                else:
                    baqir += f"[{u.first_name}](tg://user?id={u.id})"
                user_list.append(u.id)
                baqir += " "
            baqie = zilzal[:-1]
            old_msg = os.path.join("./repthon", f"{scc}.txt")
            try:
                jsondata = json.load(open(old_msg))
            except Exception:
                jsondata = False
            timestamp = int(time.time() * 2)
            new_msg = {
                str(timestamp): {"userid": user_list, "text": query}
            }  # Code by T.me/E_7_V
            buttons = [[Button.inline(info_type[2], data=f"{scc}_{timestamp}")],[Button.switch_inline(bmm, query=f"secret {malathid} \nهلو", same_peer=True)]]
            result = builder.article(
                title=f"{hmm} {baqir}",
                description=f"{dss}",
                text=f"{hss} {baqir} \n**{dss}**",
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(new_msg)
                json.dump(jsondata, open(old_msg, "w"))
            else:
                json.dump(new_msg, open(old_msg, "w"))
        elif string == "baqir":
            results = []
            results.append(
                builder.article(
                    title=f"{nmm}",
                    description=f"{mnn}",
                    text=f"**{ttt}** {baqir} **{ddd}**",
                    buttons=bbb,
                    link_preview=False,
                ),
            )
            await event.answer(results)
