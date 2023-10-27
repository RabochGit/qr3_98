import telebot
from telebot import types, custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()

# Вставьте свой токен
bot = telebot.TeleBot("6655947678:AAETwTxoqErWI6XtLmhP-mjD4XViI3-Fmo8", state_storage=state_storage, parse_mode='Markdown')

class PollState(StatesGroup):
    name = State()
    age = State()

class HelpState(StatesGroup):
    wait_text = State()

text_website = "Сайт *лучшей* онлайн-школы"  # Можно менять текст
text_ums = "Соц. сети Умскул"  # Можно менять текст
text_me = "Мой ВКонтакте"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_website,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_ums,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_me,
    )
)

@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет!',  # Можно менять текст
        reply_markup=menu_keyboard)

@bot.message_handler(func=lambda message: text_website == message.text)
def help_command(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Сайт Умскул", url="https://nd.umschool.net/home"))
    bot.send_message(message.chat.id, 'Воть', reply_markup=markup)

@bot.message_handler(func=lambda message: text_ums == message.text)
def help_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    youtube = types.KeyboardButton('Ютуб Умскул (https://www.youtube.com/@umschool)')
    vk = types.KeyboardButton('ВК Умскул (https://vk.com/umsch)')
    markup.add(youtube, vk)
    bot.send_message(message.chat.id, 'Выбирайте', reply_markup=markup)


@bot.message_handler(func=lambda message: text_me == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Мой ВК](https://vk.com/proingames)", reply_markup=menu_keyboard)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()