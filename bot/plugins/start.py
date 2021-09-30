from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"කොහොමද  {m.from_user.first_name}.\n\nමම විහගය විසින්  හදපු  screenshot දෙන බොටෙක්  . මට පුලුවන් ෆයිල් එක ඩවුන්ලොඩ් කරන් නැතුව ෆයිල් එකෙ screenshot,sample video දෙන්න වගෙ ගොඩක් වැඩ ,    (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📌  මගෙ group එක   ', url='https://t.me/joinchat/Q1uroGQ645U1OTg1'),
                    InlineKeyboardButton('🔖  මගෙ  group එකම තමා  ', url='https://t.me/joinchat/Q1uroGQ645U1OTg1')
                ],
                [
                    InlineKeyboardButton('💡  ඔය විහගය ලොබයි repo දිල නැ.  ', url='https://t.me/viha_is_power'),
                    InlineKeyboardButton('👨  මගෙ ලොක්ක ', url='https://t.me/viha_is_power')
                ]
            ]
        )
    )
