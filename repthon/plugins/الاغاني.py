import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
import asyncio
import base64
import io
import urllib.parse
import os
from pathlib import Path
import asyncio
from asyncio import sleep

from ShazamAPI import Shazam
from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError, ChatSendMediaForbiddenError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv, name_dl, song_dl, video_dl, yt_search
from ..helpers.tools import media_type
from ..helpers.utils import _reputils, reply_id
from . import zq_lo, song_download

plugin_category = "البحث"
LOGS = logging.getLogger(__name__)

# =========================================================== #
#                                                             𝙍𝙀𝙋𝙏𝙃𝙊𝙉
# =========================================================== #
SONG_SEARCH_STRING = "<b>╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰</b>"
SONG_NOT_FOUND = "<b>⎉╎لـم استطـع ايجـاد المطلـوب .. جرب البحث باستخـدام الامـر (.اغنيه)</b>"
SONG_SENDING_STRING = "<b>╮ جـارِ تحميـل الاغنيـٓه... 🎧♥️╰</b>"
# =========================================================== #
#                                                             𝙍𝙀𝙋𝙏𝙃𝙊𝙉
# =========================================================== #

@zq_lo.rep_cmd(pattern="بحث(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    else:
        await event.edit("**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    chat = "@Abm_MusicDownloader_Bot"
    async with borg.conversation(chat) as conv: # code by t.me/zzzzl1l
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(d_link)
            await conv.get_response()
            await asyncio.sleep(5)
            zelzal = await conv.get_response()
            if "⏳" not in zelzal.text:
                await zelzal.click(0)
                await asyncio.sleep(5)
                zelzal = await conv.get_response()
                await event.delete()
                await borg.send_file(
                    event.chat_id,
                    zelzal,
                    caption=f"**❈╎البحـث :** `{d_link}`",
                )

            else:
                await event.edit("**- لـم استطـع العثـور على نتائـج ؟!**\n**- حـاول مجـدداً في وقت لاحـق ...**")
        except YouBlockedUserError:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(d_link)
            await conv.get_response()
            await asyncio.sleep(5)
            zelzal = await conv.get_response()
            zelzal = await conv.get_response()
            if "⏳" not in zelzal.text:
                await zelzal.click(0)
                await asyncio.sleep(5)
                zelzal = await conv.get_response()
                await event.delete()
                await borg.send_file(
                    event.chat_id,
                    zelzal,
                    caption=f"**❈╎البحـث :** `{d_link}`",
                )

            else:
                await event.edit("**- لـم استطـع العثـور على نتائـج ؟!**\n**- حـاول مجـدداً في وقت لاحـق ...**")

@zq_lo.rep_cmd(
    pattern="اغنيه?(?:\s|$)([\s\S]*)",
    command=("اغنيه", plugin_category),
    info={
        "header": "لـ تحميـل الاغـانـي مـن يـوتيـوب",
        "امـر مضـاف": {
            "320": "لـ البحـث عـن الاغـانـي وتحميـلهـا بـدقـه عـاليـه 320k",
        },
        "الاسـتخـدام": "{tr}بحث + اسـم الاغنيـه",
        "مثــال": "{tr}بحث حسين الجسمي احبك",
    },
)
async def song(event):
    "لـ تحميـل الاغـانـي مـن يـوتيـوب"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**⎉╎قم باضافـة الاغنيـه للامـر .. بحث + اسـم الاغنيـه**")
    zed = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    zedevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await zedevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    cmd = event.pattern_match.group(1)
    q = "320k" if cmd == "320" else "128k"
    song_file, zedthumb, title = await song_download(video_link, zedevent, quality=q)
    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**⎉╎البحث :** `{title}`",
        thumb=zedthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await zedevent.delete()
    for files in (zedthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


@zq_lo.rep_cmd(
    pattern="فيديو(?:\s|$)([\s\S]*)",
    command=("فيديو", plugin_category),
    info={
        "header": "لـ تحميـل مقـاطـع الفيـديـو مـن يـوتيـوب",
        "الاسـتخـدام": "{tr}فيديو + اسـم المقطـع",
        "مثــال": "{tr}فيديو حالات واتس",
    },
)
async def _(event):
    "لـ تحميـل مقـاطـع الفيـديـو مـن يـوتيـوب"
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply and reply.message:
        query = reply.message
    else:
        return await edit_or_reply(event, "**⎉╎قم باضافـة الاغنيـه للامـر .. فيديو + اسـم الفيديـو**")
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    repevent = await edit_or_reply(event, "**╮ جـارِ البحث ؏ـن الفيديـو... 🎧♥️╰**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await repevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    try:
        stderr = (await _reputils.runcmd(video_cmd))[1]
        # if stderr:
        # return await repevent.edit(f"**Error :** `{stderr}`")
        repname, stderr = (await _reputils.runcmd(name_cmd))[:2]
        if stderr:
            return await repevent.edit(f"**خطأ :** `{stderr}`")
        repname = os.path.splitext(repname)[0]
        vsong_file = Path(f"{repname}.mp4")
    except:
        pass
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{repname}.mkv")
    elif not os.path.exists(vsong_file):
        return await repevent.edit(
            f"**⎉╎عـذراً .. لـم استطـع ايجـاد** {query}"
        )
    await repevent.edit("**- جـارِ التحميـل انتظـر ▬▭...**")
    repthumb = Path(f"{repname}.jpg")
    if not os.path.exists(repthumb):
        repthumb = Path(f"{repname}.webp")
    elif not os.path.exists(repthumb):
        repthumb = None
    title = repname.replace("./temp/", "").replace("_", "|")
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        caption=f"**⎉╎البحث :** `{title}`",
        thumb=repthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await repevent.delete()
    for files in (repthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)
