import subprocess
import time
from ping3 import ping


def check_wi_fi():
    r = ping('ya.ru')
    try:
        int(r)
        time.sleep(5)
    except Exception as e:
        print(e)
        print('Wi-fi пропал!!!!! ПАНИКА!!!! АЛЯРМ!!!!! пробуем подключиться')
        subprocess.call(['networksetup', '-setnetworkserviceenabled', 'Wi-Fi', 'off'])
        time.sleep(2)
        subprocess.call(['networksetup', '-setnetworkserviceenabled', 'Wi-Fi', 'on'])
        time.sleep(15)

while True:
    check_wi_fi()
