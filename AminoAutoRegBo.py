import amino
import secmail
import concurrent.futures
import webbrowser
import time
import base64
import string 
import random
import json
from colorama import init, Fore, Back, Style
from nickname_generator import generate
from hashlib import sha1
from bs4 import BeautifulSoup
init()
print(Back.BLACK)
print(Fore.CYAN)
print(Style.NORMAL)
print("""Script by Zevi/Скрипт сделан Zevi
┌────────────────────────────────────┐
│Author :  LilZevi                   │
│Github : https://github.com/LilZevi │
└────────────────────────────────────┘
YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ
Telegram: @NowNameBo
▄▀█ █▀▄▀█ █ █▄░█ █▀█ ▄▀█ █░█ ▀█▀ █▀█ █▀█ █▀▀ █▀▀ █▄▄ █▀█
█▀█ █░▀░█ █ █░▀█ █▄█ █▀█ █▄█ ░█░ █▄█ █▀▄ ██▄ █▄█ █▄█ █▄█
Version = 3.6
1.Generate Emails/Загенерировать почты
2.Get Messages From Email/Получить сообщения из почты
3.Read Messages From Email/Прочитать сообщения из почты
4.AutoReg for Amino/Авторег для амино""")
emailselect = input("Type Number/Введите Цифру: ")

		#email generator def
def emailgenerator():
		try:
			mail = secmail.SecMail()
			email = mail.generate_email()
			print(f"Generated {email}")
			for i in range(emailnumber):
				emailsgenerating = email
				emails = open('generatedemails.txt', 'a+')
				emails.write(emailsgenerating + '\n')
				return email
		except:
			return None
		#email generator def

		#deviceidgenerator def thanks to gefest
def deviceIdgenerator(st : int = 69):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
    thedevice = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
    return thedevice
		#deviceidgenerator def thanks to gefest

		#getmsgdef
def getmsgfromemail():
	try:
		mail = secmail.SecMail()
		email = input("Email/Почта: ")
		msgid = mail.get_messages(email=email).id
		msgdate = mail.get_messages(email=email).date
		msgsender = mail.get_messages(email=email).sender
		msgtitle = mail.get_messages(email=email).title
		print(f"messageId/IdСообщения: {msgid}")
		print(f"messagedate/ДатаСообщения: {msgdate}")
		print(f"messagesender/Отправитель сообщения: {msgsender}")
		print(f"messagetitle/Название сообщения: {msgtitle}")
	except:
		pass
		#getmsgdef

		#readmsgdef
def readmsgfromemail():
	try:
		mail = secmail.SecMail()
		email = input("Email/Почта: ")
		msgid = mail.get_messages(email=email).id
		msgid = msgid[0]
		msginfo = mail.read_message(email=email, id=msgid).info
		msgcontent = mail.read_message(email=email, id=msgid).content
		msghtmlbody = mail.read_message(email=email, id=msgid).htmlBody
		msgattachments = mail.read_message(email=email, id=msgid).attachments
		print(f"MessageInfo/ИнформацияСообщения: {msginfo}")
		print(f"MessageAttachments/ВложенияСообщения: {msgattachments}")
		print(f"MessageHTMLBody/HTMLКодСообщения: {msghtmlbody}")
		print("Message Read/Сообщение прочитано")
	except:
		pass
		#readmsgdef

		#autoregdef
def autoregforamino():
	try:
		thedeviceId = deviceIdgenerator()
		password = input("Password for All Accounts: ")
	except:
		return None
	while True:
		mail = secmail.SecMail()
		client = amino.Client()
		email = mail.generate_email()
		print(f'Email/Почта: {email}')
		print(f'Password/Пароль: {password}')
		print(f'DeviceId/Девайсайди: {thedeviceId}')
		client.request_verify_code(email=email)
		time.sleep(4)
		verifymsgid = mail.get_messages(email=email).id
		verifymsgid = verifymsgid[0]
		themail = mail.read_message(email, verifymsgid).htmlBody
		soup = BeautifulSoup(themail, 'lxml')
		quotes = soup.find_all('a')
		quotes = quotes[0].get('href')
		print(f"Verification Link/Ссылка на верификацию: {quotes}")
		webbrowser.open_new_tab(quotes)
		nick = generate('en')
		try:
			theverificationcode = input("Verification code/Код верификаций: ")
			client.register(nickname=nick, email=email, password=password, verificationCode=theverificationcode, deviceId=thedeviceId)
			print(f"{email} Registered/Зарегистрировали")
			client.login(email=email, password=password)
			client.request_verify_code(email=email)
			time.sleep(4)
			verifymsgid = mail.get_messages(email=email).id
			verifymsgid = verifymsgid[0]
			themail = mail.read_message(email, verifymsgid).htmlBody
			soup = BeautifulSoup(themail, 'lxml')
			quotes = soup.find_all('a')
			quotes = quotes[0].get('href')
			print(f"Verification Link/Ссылка на верификацию: {quotes}")
			webbrowser.open_new_tab(quotes)
			accountactivatingcode = input("Verification code/Код верификаций: ")
			client.activate_account(email=email, code=accountactivatingcode)
			print(F"{email} Activated Account/Активировали аккаунт")
		except amino.lib.util.exceptions.IncorrectVerificationCode:
			print("IncorrectVerificationCode")
			print("Неверный код верификаций")
			return None
		except amino.lib.util.exceptions.AccountLimitReached:
			print("Account Limit Reached")
			print("Превышен лимит аккаунтов")
			return None
		except amino.lib.util.exceptions.InvalidEmail:
			print("Invalid Email")
			print("Неверная почта")
			return None
		except amino.lib.util.exceptions.EmailAlreadyTaken:
			print(f"Email Already Taken {email}")
			print(f"Эту почту уже использовали {email}")
			return None
		except amino.lib.util.exceptions.UnsupportedEmail:
			print(f"UnsupportedEmail {email}")
			print(f"Неподдерживаемая почта {email}")
			return None
		except amino.lib.util.exceptions.CommandCooldown:
			print("CommandCooldown")
			print("Кулдаун команды")
			return None
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"Verification required for {email}")
			print(f"Запрашивается верификация для почты {email}")
			link = e.args[0]["url"]
			print(link)
			webbrowser.open_new_tab(link)
			input(" > ")
			client.register(nickname=nick, email=email, password=password, verificationCode=theverificationcode, deviceId=thedeviceId)
			return email
		except Exception as e:
			print(str(e))
			return None
		#autoregdef

if emailselect == "1":
	emailnumber = int(input("How Much Email Generate?: "))
	with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
		_ = [executor.submit(emailgenerator) for _ in range(emailnumber)]
	print(f"\nGenerated {emailnumber} emails in file generatedemails.txt")
	print(f"\nЗагенерировали {emailnumber} почт в файле generatedemails.txt")

elif emailselect == "2":
	getmsgfromemail()

elif emailselect == "3":
	readmsgfromemail()

elif emailselect == "4":
	autoregforamino()

