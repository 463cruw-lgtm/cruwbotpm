from aiogram import Bot
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# =========================
# MAJBURIY OBUNA
# =========================

SUBSCRIPTION_CHATS = [
    "@CRUW_OTZIF"
]


async def check_subscription(
    bot: Bot,
    user_id: int
) -> bool:

    try:
        for chat in SUBSCRIPTION_CHATS:
            member = await bot.get_chat_member(
                chat_id=chat,
                user_id=user_id
            )

            if member.status not in (
                "member",
                "administrator",
                "creator"
            ):
                return False

        return True

    except Exception as e:
        print("❌ OBUNA TEKSHIRUV XATO:", e)
        return False


# =========================
# OBUNA TUGMALARI
# =========================

subscription_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 CRUW OTZIF KANALIGA KIRISH",
                url="https://t.me/CRUW_OTZIF"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ OBUNANI TEKSHIRISH",
                callback_data="check_subscription"
            )
        ]
    ]
)


# =========================
# OBUNA TEKSHIRISH
# =========================

async def subscription_check_message(
    message: Message,
    bot: Bot
) -> bool:

    if await check_subscription(
        bot,
        message.from_user.id
    ):
        return True

    await message.answer(
        """
🔒 <b>BOTDAN FOYDALANISH UCHUN KANALGA A'ZO BO'LING!</b>

📢 Kanal: @CRUW_OTZIF

Keyin <b>✅ OBUNANI TEKSHIRISH</b> tugmasini bosing.
""",
        parse_mode="HTML",
        reply_markup=subscription_keyboard
    )

    return False