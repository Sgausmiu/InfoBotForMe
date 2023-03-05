import telebot, pyowm, datetime, webbrowser, logging
from translate import Translator
from datetime import date, time
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
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Самара')
w = observation.weather
def get_wind_3():
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('')
    w = observation.weather
    wind_3 = w.wind()['deg']
    if wind_3 == 0:
        print('С')
    elif 22 < wind_3 < 25:
        print('ССВ')
    elif 25 < wind_3 < 45:
        print('СВ')
    elif 230 < wind_3 < 245:
        print('OKKK')
    #print(wind_3)
def pr_wind_3():
    wind_3 = 35
    if wind_3 == 0:
        print('С')
    elif 22 < wind_3 < 25:
        print('ССВ')
    elif 25 < wind_3 < 45:
        print('СВ')
    print(wind_3)
# windDirection = dict{0:'С', 23:'ССВ', 45:'СВ', 68:'ВСВ', 90:'В', 113:'ВЮВ', 135:'ЮВ', 156:'ЮЮВ', 180:'Ю',
# 203:'ЮЮЗ', 225:'ЮЗ', 248:'ЗЮЗ', 270:'З', 293:'ЗСЗ', 315:'СЗ', 338:'ССЗ'} windDirection = {0: 'С', 23: 'ССВ',
# 'Northeast': 45, 'East':90, 'Southeast': 135, 'South' = 180, 'Southwest' = 225, 'West' = 270, 'Northwest' = 315}
# degrees = int(input('Ввести градус')) degrees = round(degrees / 23) * 23
def parse_wind_direction():  # -> str:
    degrees = 30#int(input('Ввести градус'))
    # degrees_2 = round(degrees / 23) * 23
    # if 20 < degrees < 225:
    #     return 'СЮС'
    # else:
    #     return 'c'


    windDirection = {0: 'С', 23: 'ССВ', 45: 'СВ', 68: 'ВСВ', 90: 'В', 113: 'ВЮВ', 135: 'ЮВ', 156: 'ЮЮВ', 180: 'Ю',
                     203: 'ЮЮЗ',
                     225: 'ЮЗ', 248: 'ЗЮЗ', 270: 'З',
                     293: 'ЗСЗ', 315: 'СЗ', 338: 'ССЗ', 360: 'С'}
    for k in windDirection.keys():
        if 0 > degrees < 23:
            return windDirection.get(k[0])
        elif 23 > degrees < 45:
            print (windDirection.get(k[23]))
        #print(windDirection[k])






print(parse_wind_direction())
print(pr_wind_3())

# def windDirection(message):
#     mgr = owm.weather_manager()
#     observation = mgr.weather_at_place(message.text)
#     w = observation.weather
#     wind_3 = w.wind['deg']
#     if wind_3 == 0:
#        return 'С'
#     elif 0>= wind_3 > 22.5:
#         return 'ССВ'
#     elif 22.5>= wind_3 > 45:
#         return 'СВ'
#     elif 202.5 >= wind_3 > 225:
#         return 'ЮЗ'

