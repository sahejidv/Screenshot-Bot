import asyncio

from pyrogram import Filters, ForceReply

from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(Filters.create(lambda _, query: query.data.startswith('mscht')))
async def _(c, m):
    dur = m.message.text.markdown.split('\n')[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f'#manual_screenshot\n\n{dur}\n\nමතක තියා ගන්න මන් විහගයගෙ ,  දැන් එවන්න ss ඕන තැන්  තත්පරවලින්  ඒක හැබැයි  කොමාවකින් වෙන් කරල තිබිය යුතුයි  `,`(comma).\nEg: `0,10,40,60,120`.\nමෙකෙන් දෙයි    0, 10, 40, 60, and 120 යන තත්පරවල තියන  ss . \n\n1. මෙකෙ උපරිම screen shot දෙන්න පුලුවන් 10යි .\n2. මතක තිය ගන්න value එක 0 ට වඩා වැඩි වෙන්න ඔනි  , or less than the video length in order to be valid.',
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply()
    )
