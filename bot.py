from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,\
    MessageHandler, Filters

from messages import Messages
from keyboards import Keyboards
from users import Users
from user import User
import config


class TelegramBot:
    def __init__(self):
        self.updater = Updater(config.TOKEN)
        self.users = Users()

        self.__add_handlers()

    def __add_handlers(self):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.on_command_start))
        dispatcher.add_handler(MessageHandler(Filters.text,
                                              self.on_text_message))

    def start(self):
        self.updater.start_polling()

    def on_command_start(self, update: Update, context: CallbackContext):
        """handles /start command"""
        message = update.message

        if not self.users.user_in(message.chat_id):
            self.users.add_user(User(message.chat_id))

        update.message.reply_markdown(Messages.start_message(),
                                      reply_markup=Keyboards.start_keyboard())

    def on_text_message(self, update: Update, context: CallbackContext):
        message = update.message
        print(message.text, message.chat_id)

        user = self.users.get(message.chat_id)

        if user is None:
            self.on_command_start(update, context)
            return

        if user.state == 0:
            self.handle_played_time(user, message)
        elif user.state == 1:
            self.handle_role(user, message)
        elif user.state == 2:
            self.handle_category(user, message)

    def handle_played_time(self, user, message):
        user.hours = None

        if message.text == "<100":
            user.hours = 0
        elif message.text == "100-500":
            user.hours = 1
        elif message.text == "500-1000":
            user.hours = 2
        elif message.text == ">1000":
            user.hours = 3
        else:
            message.reply_markdown(Messages.please_repeat(),
                                   reply_markup=Keyboards.start_keyboard())
            return

        user.state = 1
        self.users.update(user)

        message.reply_markdown(Messages.select_position(),
                               reply_markup=Keyboards.position())

    def handle_role(self, user, message):
        user.role = None

        if message.text == "1":
            user.role = 1
        elif message.text == "2":
            user.role = 2
        elif message.text == "3":
            user.role = 3
        elif message.text == "4":
            user.role = 4
        elif message.text == "5":
            user.role = 5
        else:
            message.reply_markdown(Messages.please_repeat(),
                                   reply_markup=Keyboards.position())
            return

        user.state = 2
        self.users.update(user)

        message.reply_markdown(Messages.select_category(),
                               reply_markup=Keyboards.category())

    def handle_category(self, user, message):
        user.category = None

        if message.text == "Сила":
            user.category = 0
        elif message.text == "Ловкость":
            user.category = 1
        elif message.text == "Интеллект":
            user.category = 2
        else:
            message.reply_markdown(Messages.please_repeat(),
                                   reply_markup=Keyboards.category())
            return

        user.state = 0
        self.users.update(user)

        message.reply_markdown(Messages.answer(),
                               reply_markup=Keyboards.category())
        message.reply_markdown(Messages.start_message(),
                                      reply_markup=Keyboards.start_keyboard())


