import telebot

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш бот. Чем могу помочь?")


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Вот список доступных команд:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь\n"
        "/perevorot - Перевернуть текст\n"
        "/caps - Преобразовать текст в заглавные буквы\n"
        "/cut - Удалить все гласные буквы из текста\n"
        "/sum_abc - Посчитать количество букв в слове\n"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['perevorot'])
def reverse_text(message):
    text_to_reverse = message.text[len('/perevorot '):].strip()

    if text_to_reverse:
        reversed_text = text_to_reverse[::-1]
        bot.reply_to(message, reversed_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для переворота после команды /perevorot.")

@bot.message_handler(commands=['caps'])
def caps_text(message):
    text_to_caps = message.text[len('/caps '):].strip()

    if text_to_caps:
        caps_text = text_to_caps.upper()
        bot.reply_to(message, caps_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для преобразования в заглавные буквы после команды /caps.")

@bot.message_handler(commands=['cut'])
def cut_vowels(message):
    text_to_cut = message.text[len('/cut '):].strip()

    if text_to_cut:
        vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
        cut_text =''.join([char for char in text_to_cut if char not in vowels])
        bot.reply_to(message, cut_text)
    else:
        bot.reply_to(message, "Пожалуйста, укажите текст для удаления гласных после команды /cut.")

@bot.message_handler(commands=['sum_abc'])
def sum_abc(message):
    text_to_count = message.text[len('/sum_abc '):].strip()
    if text_to_count:
        letter_count = len(text_to_count)
        bot.reply_to(message, f"Количество букв в слове: {letter_count}")
    else:
        bot.reply_to(message, "Пожалуйста, укажите слово для подсчета букв после команды /sum_abc.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Попробуйте /help для списка команд.")


if __name__ == '__main__':
    bot.polling(none_stop=True)