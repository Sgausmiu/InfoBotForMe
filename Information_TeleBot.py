import telebot, pyowm, datetime, webbrowser, logging
from translate import Translator
from pyowm.utils import config as cfg
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("2049763311:AAE_Hag8ynuKvsEWiBijXAh_2gMxVMN6uu0")
my_user_id = [164594856]
bot_user_id = [2049763311]  # user_bot_reference = "http://t.me/Information1587720bot"
config_dict = get_default_config()
config_dict['connection']['use_ssl'] = False
config_dict['connection']["verify_ssl_certs"] = False
owm = pyowm.OWM('fddfda5827012a5f639e3ed88bf5c07f', config_dict)
# ya_token = 'b31b6d84-0d3f-4f6f-be55-fd8db6eba323'
config = cfg.get_default_config()
config['language'] = 'ru'
logging.basicConfig(level=logging.DEBUG, filename="inf_bot.log", filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message.chat.id, 'Приветствую, я - информационный бот. Отправь мне название города, сообщу текущую погоду.')
@bot.message_handler(content_types=['text'])
def send_message(message):
    try:
        if message.text == '/772077':
            return helper_my(message)
        else:
            translator = Translator(to_lang='ru')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            w = observation.weather
            wind = w.wind()['speed']
            wind_2 = w.wind()['gust']
            humidity_1 = w.humidity
            temperature = w.temperature('celsius')['temp']
            current_date = datetime.datetime.now()
            rain = mgr.weather_at_place(message.text).weather.rain
            pressure_dict = mgr.weather_at_place(message.text).weather.barometric_pressure()
            visibility = observation.weather.visibility_distance
            wind_3 = w.wind()['deg']
            wind_4 = []
            if 0 < wind_3 < 23:
                wind_4.append('С-СВ')
            elif 22 < wind_3 < 46:
                wind_4.append('СВ')
            elif 45 < wind_3 < 68:
                wind_4.append('В-СВ')
            elif 67 < wind_3 < 91:
                wind_4.append('В')
            elif 90 < wind_3 < 113:
                wind_4.append('В-ЮВ')
            elif 112 < wind_3 < 136:
                wind_4.append('Ю-В')
            elif 135 < wind_3 < 158:
                wind_4.append('Ю-ЮВ')
            elif 157 < wind_3 < 181:
                wind_4.append('Ю')
            elif 180 < wind_3 < 203:
                wind_4.append('Ю-ЮЗ')
            elif 202 < wind_3 < 226:
                wind_4.append('Ю-З')
            elif 225 < wind_3 < 248:
                wind_4.append('З-ЮЗ')
            elif 247 < wind_3 < 271:
                wind_4.append('З')
            elif 270 < wind_3 < 293:
                wind_4.append('З-СЗ')
            elif 292 < wind_3 < 316:
                wind_4.append('С-З')
            elif 315 < wind_3 < 338:
                wind_4.append('С-СЗ')
            else:
                wind_4.append('С')
            location = f"https://yandex.ru/pogoda/maps/nowcast?lat={observation.location.lat}&lon={observation.location.lon}&via=hnaw&[lang=ru_RU]"
            answer = f"Сегодня {'{:%d-%m-%Y %H:%M:%S}'.format(current_date)} - текущее самарское время." \
                     f"\nВ городе {message.text.title()} сейчас {w.detailed_status} и температура {str(temperature)} °С." \
                     f"\nСкорость ветра составляет {wind} м/с, порыв до {wind_2} м/с." \
                     f"\nНаправление потока на розе румбов: {wind_4.pop()}." \
                     f"\nВидимость не более {round(int(visibility * 0.001), 2)} км." \
                     f"\nОтносительная влажность воздуха {humidity_1} %." \
                     f"\nКоличество осадков за последний час {rain.get('1h', 0)} мм." \
                     f"\nАтмосферное давление составляет {(int((pressure_dict['press']) * 0.750064))} мм рт. ст., что примерно составляет {round(float((pressure_dict['press']) / 760), 2)} атм." \
                     f"\nБолее детально: {location}"

            current_month = datetime.datetime.now().strftime('%B')  # месяц буквами
            current_month_translate = translator.translate(current_month)
            if current_month == 'November' or current_month == 'October' or current_month == 'September':
                answer += f"\n\nСейчас {current_month_translate} и на дворе осень, одевайся по погоде, пей дома горячий глинтвейн и слушай Стинга в кассетном плеере. "
            elif current_month == 'June' or current_month == 'July' or current_month == 'August':
                answer += f"\n\nСейчас {current_month_translate} и на дворе прекрасная летняя погода, не работай - просто отдыхай."
            elif current_month == 'January' or current_month == 'February' or current_month == 'December':
                answer += f"\n\nСейчас {current_month_translate} и на дворе зима, грейся о теплую спинку пушистой киски."
            elif current_month == 'March' or current_month == 'April' or current_month == 'May':
                answer += f"\n\nСейчас {current_month_translate} и на дворе весна, радуйся солнышку и смотри на попки девочек."
            bot.send_message(message.chat.id, answer)
    except:
        bot.send_message(message.chat.id, 'Город не найден.')


def helper_my(message):
    if message.text == '/772077':
        ref_1 = webbrowser.open("C:\Program Files\DBeaver\dbeaver.exe")
        ref_2 = webbrowser.open("C:\Program Files (x86)\Fortinet\FortiClient\FortiClient.exe")
        ref_3 = webbrowser.open(r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\bin\pycharm64.exe")
        ref_4 = webbrowser.open(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        ref_5 = webbrowser.open(r"C:\Users\Сенников Виталий\Desktop\образец777.xlsx")
        ref_6 = webbrowser.open(r"C:\Users\Сенников Виталий\Desktop\Шаблон подключения.txt")
        answer_1 = ref_1, ref_2, ref_3, ref_4, ref_5, ref_6
        bot.send_message(message, answer_1)
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав запуска.')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
