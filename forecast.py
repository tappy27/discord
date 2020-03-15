import math
import datetime


def get_forecast():

    now = datetime.datetime.today()
    standard_time = datetime.datetime(2020, 1, 23, 6, 00, 00) #rotate_mode = 0

    rotate_mode = (now - standard_time).days % 3

    #Defence Forces schedule
    table = ['　　全兵団　　', '深碧の造魔兵団', '蒼怨の屍獄兵団', '銀甲の凶蟲兵団', '翠煙の海妖兵団', 
             '　　全兵団　　', '闇朱の獣牙兵団', '紫炎の鉄機兵団', '翠煙の海妖兵団']

    if rotate_mode == 0:
        pass
    elif rotate_mode == 1:
        table = table[6:] + table[:6] 
    elif rotate_mode == 2:
        table = table[3:] + table[:3]

    dic = {}
    dic['current_group'] = table[now.hour % 9]
    dic['next_group'] = table[(now.hour + 1) % 9]
    dic['next_next_group'] = table[(now.hour + 2) % 9]
    dic['time_to_next'] = str(60 - now.minute)

    
    #Boss schedule
    dic['inuhone'] =  str((rotate_mode + 1) % 3 + 1)
    dic['sasori'] = str(rotate_mode % 3 + 1)
    dic['hage'] = str((rotate_mode + 2) % 3 + 1)
    dic['gorilla'] = dic['hage']

    return dic

