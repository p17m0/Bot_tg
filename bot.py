import time
import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    JobQueue, # &&&&&&&&&&&&&&&&&&&
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from data import db_postgres

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

NAME, EDUCATION, YEAR, LOCATION, EXPERIENCE, WORK_BEFORE, RESUME, PHONE, EMAIL, PHOTO, LOCATION, WAIT = range(12)
MENU, INN, CONTACT_NAME, CONTACTS, COMMENT = 99, 100, 101, 102, 103
TIME_FOR_REGISTRATION = 360 # 6 минут
TIME_FOR_WAITING = 21600 # 6 часов
TIME_FOR_WAITING_STATUS = 720 # 12 минут
ADMIN_TG_ID = os.getenv('ADMIN_TG_ID')

keyboard = [
                ['Отправить потенциального клиента'],
                ['Запросить логин и пароль для доступа в личный кабинет'],
                ['Запросить видеозвонок'],
                ['Проверить статус сделок'],
            ]
reply_markup = ReplyKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their FIO."""
    user = update.message.from_user
    user_data = context.user_data
    if not db_postgres.check_user(user.id):
        user_data['START'] = True
        await update.message.reply_text("Здравствуйте!\nНапишите ваше полное имя")
        user_data[user.id] = {}
        user_data[user.id].update({'telegramid': user.id})
        return NAME
    if db_postgres.check_activation(user.id):
        reply_markup = ReplyKeyboardMarkup(keyboard)
        await update.message.reply_text("Здравствуйте!", reply_markup=reply_markup)
        return ConversationHandler.END
    if db_postgres.check_user(user.id) and not db_postgres.check_activation(user.id):
        while True:
            await update.message.reply_text('Ожидайте одобрения заявки')
            time.sleep(25) # 21600
            if db_postgres.check_activation(user.id):
                await update.message.reply_text(
                    "Ваша заявка одобрена. Теперь вы являетесь нашим региональным представителем. Просьба зарегистрироваться как самозанятый.",
                    reply_markup=reply_markup
                )
                return ConversationHandler.END


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup(keyboard)
    reply_markup=markup
    await update.message.reply_text("Здравствуйте!", reply_markup=reply_markup)


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected FIO and asks for a education."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'fio': update.message.text})
    logger.info("name of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Укажите в свободной форме ваше образование",
    )

    return EDUCATION

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'obrazovanie': update.message.text})
    logger.info("education of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Укажите ваш год рождения в формате ГГГГ-ММ-ДД",
    )

    return YEAR

async def year_of_birth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'date': update.message.text})
    logger.info("year_of_birth of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "В каком городе вы живете? (укажите также область или край)",
    )

    return LOCATION

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the location and asks for some info about the user."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'city': update.message.text})
    logger.info("location of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Есть ли у вас опыт продаж (любого типа) - в свободной форме"
    )

    return EXPERIENCE

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'samozan': update.message.text})
    logger.info("experience of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Регистрировались ли вы как самозанятый или ИП?",
    )

    return WORK_BEFORE

async def work_before(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'opit': update.message.text})
    logger.info("work_before of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Если у вас есть резюме, можете приложить его в виде ссылки",
    )

    return RESUME

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'resume': update.message.text})
    logger.info("resume of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Ваш контактный телефон",
    )

    return PHONE

async def phone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'phone': update.message.text})
    logger.info("phone of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Ваш контактный емейл",
    )
    return EMAIL

async def user_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'email': update.message.text})
    logger.info("user_email of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Ваше фото",
    )
    return PHOTO

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'photo': f'data/photos/{user.id}.jpg'})
    photo_file = await update.message.photo[-1].get_file()
    print(photo_file)
    await photo_file.download(f'data/photos/{user.id}.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo')

    await update.message.reply_text(
        "Спасибо за предоставленные данные! Пожалуйста, ожидайте.",
    )
    db_postgres.add_user(user_data[user.id])
    print(user_data[user.id])
    user_data[user.id] = {}
    print(user_data[user.id])
    context.bot.send_message(chat_id=ADMIN_TG_ID, text=f'Появилась заявка на регистрацию от пользователя {user.id}')
    while True:
        time.sleep(5) # 21600
        if db_postgres.check_activation(user.id):
            await update.message.reply_text(
                "Ваша заявка одобрена. Теперь вы являетесь нашим региональным представителем. Просьба зарегистрироваться как самозанятый.",
                reply_markup=reply_markup
            )
            return ConversationHandler.END



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day."
    )

    return ConversationHandler.END

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "Отправить потенциального клиента":
        await update.message.reply_text(text='Укажите название компании, инн')
        return INN
    if update.message.text == "Запросить логин и пароль для доступа в личный кабинет":
        await ask_login(update, context)
    if update.message.text == "Запросить видеозвонок":
        await ask_call(update, context)
    if update.message.text == 'Проверить статус сделок':
        user = update.message.from_user
        old_message = ''
        time.sleep(10)
        new_message = db_postgres.take_deals_history(user.id)
        if old_message != new_message:
            old_message = new_message
            await update.message.reply_text(
                    f"{new_message}",
                    reply_markup=reply_markup)


async def inn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id] = {}
    user_data[user.id].update({'telegramid': user.id})
    user_data[user.id].update({'inn': update.message.text})
    await update.message.reply_text(text='Укажите имя контактного лица, с которым вы держали связь, а также его должность')
    return CONTACT_NAME

async def contact_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'contact_name': update.message.text})
    await update.message.reply_text(text='Контактный телефон, емейл или другие контактные данные')
    return CONTACTS

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'contacts': update.message.text})
    await update.message.reply_text(text='Дайте краткий комментарий о первичных переговорах, информацию об объекте, на чем остановились переговоры и т.п.')
    return COMMENT

async def comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_data = context.user_data
    user_data[user.id].update({'comment': update.message.text})
    print(user_data[user.id])
    # Собранные данные кладем в БД в таблицу clients
    db_postgres.add_client(user_data[user.id])
    # и отправляется уведомление на почту и в телегу админу
    # send_mail
    context.bot.send_message(chat_id=ADMIN_TG_ID, text=f'Сделана сделка пльзователем {user.id}')
    user_data[user.id] = {}
    print(user_data[user.id])
    await update.message.reply_text(text='Ваша заявка на сделку была принята.'
                                         'Менеджер обработает ее и сделает на ее основе сделку и инициирует переговоры.'
                                         'Все события по сделке будут транслироваться вам в телеграм')
    return ConversationHandler.END

async def ask_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    login, password = db_postgres.take_login_password(user.id)
    await update.message.reply_text(text=f'Ваш логин: {login}; Пароль: {password}.')

async def ask_call(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # send_email or send message to admin about call
    await update.message.reply_text(text='Запрос звонка...')

async def timeout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(text='Регистрация отменена')

async def notification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time.sleep(5)
    await update.message.reply_text(text='Нотификатион')

def main() -> None:
    """Run the bot."""
    token = os.getenv('TOKEN')
    # Create the Application and pass it your bot's token.
    app = Application.builder().token(token).build()

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT, name)],
            EDUCATION: [MessageHandler(filters.TEXT, education)],
            YEAR: [MessageHandler(filters.TEXT, year_of_birth)],
            LOCATION: [MessageHandler(filters.TEXT, location),],
            EXPERIENCE: [MessageHandler(filters.TEXT, experience)],
            WORK_BEFORE: [MessageHandler(filters.TEXT, work_before)],
            RESUME: [MessageHandler(filters.TEXT, resume)],
            PHONE: [MessageHandler(filters.TEXT, phone)],
            EMAIL: [MessageHandler(filters.TEXT, user_email)],
            PHOTO: [MessageHandler(filters.PHOTO, photo),],
            ConversationHandler.TIMEOUT: [MessageHandler(filters.TEXT, timeout)],
        },
        conversation_timeout=TIME_FOR_REGISTRATION,
        fallbacks=[CommandHandler('cancelito', cancel)],
    )
    offer_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Text([
            'Отправить потенциального клиента',
            'Запросить логин и пароль для доступа в личный кабинет',
            'Запросить видеозвонок',
            'Проверить статус сделок',
            ]), echo)],
        states={
            MENU: [MessageHandler(filters.TEXT, echo)],
            INN: [MessageHandler(filters.TEXT, inn)],

            CONTACT_NAME: [MessageHandler(filters.TEXT, contact_name)],
            CONTACTS: [MessageHandler(filters.TEXT, contacts)],
            COMMENT: [MessageHandler(filters.TEXT, comment)],
        },
        fallbacks=[CommandHandler('cancelito', cancel)]
    )
    app.add_handler(conv_handler)
    app.add_handler(offer_handler)
    # Run the bot until the user presses Ctrl-C
    app.run_polling()




if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        print('DONE')