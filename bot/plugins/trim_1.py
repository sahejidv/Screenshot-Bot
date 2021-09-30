import asyncio

from pyrogram import Filters, ForceReply

from ..utils import sample_fn
from ..screenshotbot import ScreenShotBot
from ..config import Config


@ScreenShotBot.on_callback_query(Filters.create(lambda _, query: query.data.startswith('trim')))
async def _(c, m):
    dur = m.message.text.markdown.split('\n')[-1]
    await m.message.delete(True)
    await c.send_message(
        m.from_user.id,
        f'#trim_video\n\n{dur}\n\nදැන් එවන්න trim කිරිය යුතු කාලය තත්පරවලින් ,   ඒක එවන්න ඔනි  මෙහෙම  {Config.MAX_TRIM_DURATION}s. \n**start:end**\n\nEg: `400:500` ==> මෙක ට්‍රිම් කරනව  400තත්පර ඉදන්  500තත්පරයට',
        reply_to_message_id=m.message.reply_to_message.message_id,
        reply_markup=ForceReply()
    )
