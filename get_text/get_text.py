async def start_text(language):
    if language == 'uz':
        return f"*Quyidagilardan birini tanlang*"
    else:
        return f"*Выберите один из следующих*"


async def start_hello_text(language):
    return f"*Assalomu aleykum Xush kelibsiz*" if language == 'uz' else f"*Привет и добро пожаловать*"


async def update_langugaes_text(language):
    return f"uz" if language == '🇺🇿 Uzbek' else f"ru"


async def get_registration_user(lang):
    return f"*Siz ro'yxatdan o'tgansiz*" if lang == '🇺🇿' else f"*Вы зарегистрированы*"


async def get_not_registration_user(lang):
    if lang == 'uz':
        text = f"*Siz ro'yxatdan o'tmagansiz*"
    return text


async def state_user_name(lang):
    if lang == "uz":
        text = f"*Ism Familiyangizmi kiriting\nNamuna: Aziz Azizov*"
    else:
        text = f"*Введите свое имя и фамилию\nПример: Азиз Азизов*"
    return text


async def state_error_username(lang):
    if lang == "uz":
        text = f"*Iltimos Ism Familiyangizmi kiriting\nNamunadek kiriting*"
    else:
        text = f"*Введите свое имя и фамилию\nВведите в качестве примера*"
    return text


async def get_user_phone(lang):
    if lang == "uz":
        text = f"*Raqamingizni yuboring*"
    else:
        text = f"*Отправьте свой номер*"
    return text


async def error_phone_user_number(lang):
    if lang == "uz":
        text = f"*Raqam yuborishda xatolik yuz berdi*"
    else:
        text = f"*Произошла ошибка при отправке номера*"
    return text


async def caption_company(lang):
    if lang == "uz":
        text = f"*2025 yilga kelib, 20 ta davlatda faol mijozlar bazasiga ega geografik jihatdan diversifikatsiyalangan konglomerat paydo bo‘ladi. O‘zbekistonni sanoatlashtirish davlat ramzi, uning mijozlari, aktsiyadorlari va hamkorlari uchun qo‘shimcha qiymat.*"
    else:
        text = f"*К 2025 году стать географически диверсифицированным конгломератом с активной клиентской базой в 20 странах мира. Стать символом индустриализации Узбекистана, который повысит ценности для своих клиентов, акционеров и партнёров*"
    return text
