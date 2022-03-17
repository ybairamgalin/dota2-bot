"""Program execution starts here"""
from bot import TelegramBot


def main():
    bot = TelegramBot()

    try:
        bot.start()
    except KeyboardInterrupt:
        print("Завершение работы")
        exit(0)
    except Exception as e:
        # restart on release
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
