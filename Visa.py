import requests

import random

import os

def banner():

    os.system('clear')

    print ('\t         \033[1;34m   ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')

    print('\t         \033[1;34m   ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')

    print ('\t         \033[1;34m   ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')

    print ('\t         \033[1;34m   ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')

    print ('\t         \033[1;34m   ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇\033[2;32m  Code By :\033[2;31m Creack_Dark ')

    print ('\t         \033[1;34m   ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')

    print ('\t         \033[1;34m   ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')

    print ('\t         \033[1;34m   ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')

    print('''\n\t\033[1;33m         https://t.me/Creack_Dark       

\t       https://github.com/Creack_Dark/\n''')

banner()

print('\033[2;37m-------------------------------------------------------------')

N = '1234567890'

while True:

    bin = int("". join(random.choice(N) for i in range(6)))

    url = f"https://api.dlyar-dev.tk/info-bin?bin={bin}"

    res = requests.get(url).json()

    if res["status"] == True:

       try: 

           co = res["country"]    

           fl = res["flag"]

           print(f'\033[2;32m  Good bin : \033[2;34m {bin}  \n \033[2;33m Bin Visa ✅ \n  Country : \033[2;37m{co} \n \033[2;33m Flag : \033[2;31m{fl} ')

           print('\033[2;37m--------------------------------------------')

       except:

           print(f'\033[2;31m  Bad bin : \033[2;35m {bin} ')

           print('\033[2;37m--------------------------------------------')

           continue

    else:

        print(f'\033[2;31m  Bad bin : \033[2;35m {bin} ')

        print('\033[2;37m--------------------------------------------')  
