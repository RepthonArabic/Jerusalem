# Repthon - @Repthon
# Copyright (C) 2022 Repthon . All Rights Reserved
#< https://t.me/Repthon >
# This file is a part of < https://github.com/RepthonArabic/RepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/RepthonArabic/RepthonAr/blob/master/LICENSE/>.

import asyncio
import glob
import os
import sys
import heroku3
import urllib.request
from datetime import timedelta
from pathlib import Path

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest

from repthon import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import zq_lo
from ..core import web_server
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger("𝐑𝐞𝐩𝐭𝐡𝐨𝐧")
cmdhr = Config.COMMAND_HAND_LER

heroku_api = "https://api.heroku.com"
if Config.HEROKU_APP_NAME is not None and Config.HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


if ENV:
    VPS_NOLOAD = ["vps"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["heroku"]

bot = zq_lo
DEV = 5502537272

async def autovars(): #Code by T.me/E_7_V
    if "ENV" in heroku_var:
        return
    LOGS.info("جـارِ اضافـة بقيـة الفـارات .. تلقائيـاً")
    rrenv = "ANYTHING"
    rrcom = "."
    rrrtz = "Asia/Baghdad"
    heroku_var["ENV"] = rrenv
    heroku_var["COMMAND_HAND_LER"] = rrcom
    heroku_var["TZ"] = rrrtz
    LOGS.info("تم اضافـة بقيـة الفـارات .. بنجـاح")

async def autoname(): #Code by T.me/E_7_V
    if Config.ALIVE_NAME:
        return
    await bot.start()
    await asyncio.sleep(15)
    LOGS.info("جـارِ اضافة فـار الاسـم التلقـائـي .. انتظـر قليـلاً")
    baqir = await bot.get_me()
    rrname = f"{baqir.first_name}"
    LOGS.info(f"تم اضافـة اسـم المستخـدم {rrname} .. بنجـاح")
    heroku_var["ALIVE_NAME"] = rrname

async def setup_bot():
    """
    To set up bot for Repthon
    """
    try:
        await zq_lo.connect()
        config = await zq_lo(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == zq_lo.session.server_address:
                if zq_lo.session.dc_id != option.id:
                    LOGS.warning(
                        f"ايـدي DC ثـابت فـي الجلسـة مـن {zq_lo.session.dc_id}"
                        f" الـى {option.id}"
                    )
                zq_lo.session.set_dc(option.id, option.ip_address, option.port)
                zq_lo.session.save()
                break
        bot_details = await zq_lo.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await zq_lo.start(bot_token=Config.TG_BOT_USERNAME)
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        baqirport = Config.PORT
        await web.TCPSite(app, bind_address, baqirport).start()
        zq_lo.me = await zq_lo.get_me()
        zq_lo.uid = zq_lo.tgbot.uid = utils.get_peer_id(zq_lo.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(zq_lo.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {e}")
        sys.exit()


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.ZQ_LOBLOGO = await zq_lo.tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/f367d5a4a6bf1fbfc99b9.mp4",
                caption="**•⎆┊تـم بـدء تشغـيل سـورس ريبـــثون الخاص بك .. بنجاح 🧸♥️**",
                buttons=[(Button.url("𝙍𝙀𝙋𝙏𝙃𝙊𝙉", "https://t.me/Repthon"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await zq_lo.check_testcases()
            message = await zq_lo.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**•⎆┊تـم اعـادة تشغيـل السـورس بنجــاح 🧸♥️**"
            await zq_lo.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await zq_lo.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def mybot():
    ROGER = bot.me.first_name
    Narcissus = bot.uid
    ba_roger = f"[{ROGER}](tg://user?id={Narcissus})"
    f"ـ {ba_roger}"
    f"•⎆┊هــذا البــوت خــاص بـ {ba_roger} يمكـنك التواصــل معـه هـنا 🧸♥️"
    babot = await zq_lo.tgbot.get_me()
    bot_name = babot.first_name
    botname = f"@{babot.username}"
    if bot_name.endswith("Assistant"):
        print("تم تشغيل البوت بنجــاح")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "ريبـــثون")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"مسـاعـد - {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file("@BotFather", "repthon/baqir/IMG_20220821_170541_585.jpg")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"- بـوت ريبـــثون المسـاعـد ♥️🦾 الخـاص بـ  {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"•⎆┊انـا البــوت المسـاعـد الخــاص بـ {ba_roger} \n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @Repthon 🌐")
        except Exception as e:
            print(e)



async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await zq_lo.tgbot.get_me()
    try:
        await zq_lo(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await zq_lo(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def load_plugins(folder, extfolder=None):
    """
    To load plugins from the mentioned folder
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"repthon/{folder}/*.py"
        plugin_path = f"repthon/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لا يمكنني تحميل {shortname} بسبب الخطأ {e}\nمجلد القاعده {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await zq_lo.tgbot.send_message(
            BOTLOG_CHATID,
            f'Your external repo plugins have imported \n**No of imported plugins :** `{success}`\n**Failed plugins to import :** `{", ".join(failure)}`',
        )


async def saves():
    try:
        os.environ[
            "STRING_SESSION"
        ] = "**- تحذيـر ❌ هذا الملف ملغـم .. لـذلك لم يتـم تنصيبـه في حسـابك للامــان ...**"
    except Exception as e:
        print(str(e))
    try:
        await zq_lo(JoinChannelRequest("@Repthon"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@roger21v"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthonn"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthon_up"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthon_vars"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthon_cklaish"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@ZQ_LO"))
    except BaseException:
        pass 
    try:
        await zq_lo(JoinChannelRequest("@Test_Repthon"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthon_help"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@Repthon_support"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@f3ytr"))
    except BaseException:
        pass
    try:
        await zq_lo(JoinChannelRequest("@xxfir"))
    except BaseException:
        pass




async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await zq_lo.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"
        photozed = await zq_lo.upload_file(file="baqir/taiba/IMG_20220821_230957_726.jpg")
        _, groupid = await create_supergroup(
            "كـروب السجـل ريبـــثون", zq_lo, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "المجموعه الخاصه لفار الـ PRIVATE_GROUP_BOT_API_ID تم حفظه بنجاح و اضافه الفار اليه."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await zq_lo.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        " الصلاحيات غير كافيه لأرسال الرسالئل في مجموعه فار ااـ PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات اضافه اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID لم يتم العثور على قيمه هذا الفار . تاكد من أنه صحيح .")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID قيمه هذا الفار خطا. تاكد من أنه صحيح.")
        except Exception as e:
            LOGS.error("حدث خطأ اثناء التعرف على فار PM_LOGGER_GROUP_ID.\n" + str(e))
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامه (وظيفتهـا تخزيـن رسـائل الخـاص.)"
        photozed = await zq_lo.upload_file(file="baqir/taiba/IMG_20220821_170831_450.jpg")
        _, groupid = await create_supergroup(
            "كـروب التخـزين", zq_lo, Config.TG_BOT_USERNAME, descript, photozed
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تم عمل الكروب التخزين بنجاح واضافة الفارات اليه.")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "repthon"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


async def install_externalrepo(repo, branch, cfolder):
    REPREPO = repo
    if REPBRANCH := branch:
        repourl = os.path.join(REPREPO, f"tree/{REPBRANCH}")
        gcmd = f"git clone -b {REPBRANCH} {REPREPO} {cfolder}"
        errtext = f"There is no branch with name `{REPBRANCH}` in your external repo {ZEDREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = REPREPO
        gcmd = f"git clone {REPREPO} {cfolder}"
        errtext = f"The link({REPREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await zq_lo.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "There was a problem in cloning the external repo. please recheck external repo link"
        )
        return await zq_lo.tgbot.send_message(
            BOTLOG_CHATID,
            "There was a problem in cloning the external repo. please recheck external repo link",
        )
    if os.path.exists(os.path.join(cfolder, "requirements.txt")):
        rpath = os.path.join(cfolder, "requirements.txt")
        await runcmd(f"pip3 install --no-cache-dir {rpath}")
    await load_plugins(folder="repthon", extfolder=cfolder)
