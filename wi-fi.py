import subprocess
import time
from ping3 import ping


def check_wi_fi():
    r = ping('ya.ru')
    if r == None or r == False:
        print('Wi-fi пропал!!!!! ПАНИКА!!!! АЛЯРМ!!!!! пробуем подключиться')
        subprocess.call(['networksetup', '-setnetworkserviceenabled', 'Wi-Fi', 'off'])
        time.sleep(2)
        subprocess.call(['networksetup', '-setnetworkserviceenabled', 'Wi-Fi', 'on'])
        time.sleep(10)
    else:
        time.sleep(15)
        print(f'Все в порядке, сигнал долетел до другой планеты за - {r} мс.')



while True:
    check_wi_fi()
