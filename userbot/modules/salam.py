from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Salam Dari {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.`")
# Owner @Si_Dian
# Thanks XBOT-REMIX

@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Salam Dari {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.`")
# Owner @Si_Dian
# Izin Maling Om

@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Jawab Salam Dulu Biar Sopan.`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.`")
# Owner @Si_Dian
# Izin Maling Om

@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Jawab Salam Dulu Biar Sopan.`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.`")
# Owner @Si_Dian
# Hehehehe

@register(outgoing=True, pattern='^PPPP(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Door To Door`")
    sleep(2)
    await typew.edit("`GC Lu Gua Gedoor`")
	sleep(2)
    await typew.edit("`Gajadi Deh, Nyari Slipkol Aja`")
# Owner @Si_Dian
# Izin Maling Om

@register(outgoing=True, pattern='^pppp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Door To Door`")
    sleep(2)
    await typew.edit("`GC Lu Gua Gedoor`")
	sleep(2)
    await typew.edit("`Gajadi Deh, Nyari Slipkol Aja`")
# Owner @Si_Dian
# Izin Maling Om

CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
\nUsage: Buat Gedor.\
\n\n`PPPP`\
\nUsage: Buat Gedor."
})
