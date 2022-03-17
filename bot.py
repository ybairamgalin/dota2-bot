from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from messages import Messages
from keyboards import Keyboards
import config


class TelegramBot:
    def __init__(self):
        self.updater = Updater(config.TOKEN)

        self.__add_handlers()

    def __add_handlers(self):
        dispatcher = self.updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.on_command_start))

    def start(self):
        self.updater.start_polling()

    def on_command_start(self, update: Update, context: CallbackContext):
        """handles /start command"""
        update.message.reply_markdown(Messages.start_message(),
                                      reply_markup=Keyboards.start_keyboard())


