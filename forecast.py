import math
import datetime


def get_forecast(now):

    #Defence Forces schedule
    standard_time = datetime.datetime(2020, 3, 29, 0, 00, 00) #rotate_mode = 0
    rotate_mode = (now - standard_time).days % 5

    #table = ['　　全兵団　　', '深碧の造魔兵団', '蒼怨の屍獄兵団', '銀甲の凶蟲兵団', '翠煙の海妖兵団', 
    #         '　　全兵団　　', '闇朱の獣牙兵団', '紫炎の鉄機兵団', '翠煙の海妖兵団']
    table = ['灰塵の竜鱗兵団', '　　全兵団　　', '蒼怨の屍獄兵団', '銀甲の凶蟲兵団', '翠煙の海妖兵団',
             '灰塵の竜鱗兵団', '　　全兵団　　', '闇朱の獣牙兵団', '紫炎の鉄機兵団', '深碧の造魔兵団']

    if rotate_mode == 0:
        pass
    elif rotate_mode == 1:
        table = table[4:] + table[:4]
    elif rotate_mode == 2:
        table = table[8:] + table[:8]
    elif rotate_mode == 3:
        table = table[2:] + table[:2]
    elif rotate_mode == 4:
        table = table[6:] + table[:6]

    dic = {}
    dic['table'] = table[now.hour % len(table):] + table[:now.hour % len(table)]
    dic['time_to_next'] = str(60 - now.minute)

    i = 0
    while table[(now.hour + i) % len(table)] != '灰塵の竜鱗兵団':
        i += 1
    dic['next_new_start'] = str((now + datetime.timedelta(hours=i)).hour)
    dic['next_new_end'] = str((now + datetime.timedelta(hours=i+2)).hour)

    #Boss schedule
    standard_time = datetime.datetime(2020, 3, 30, 6, 00, 00) #rotate_mode = 0
    rotate_mode = (now - standard_time).days % 3

    dic['inuhone'] =  str((rotate_mode + 2) % 3 + 1)
    dic['sasori'] = str((rotate_mode + 1) % 3 + 1)
    dic['hage'] = str(rotate_mode % 3 + 1)
    dic['gorilla'] = dic['hage']

    return dic
    