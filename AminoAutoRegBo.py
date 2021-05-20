import amino
import secmail
import imaplib
import concurrent.futures
import webbrowser
import time
import imaplib
import re
import base64
import string 
import random
import json
import secrets
from colorama import init, Fore, Back, Style
init()
from nickname_generator import generate
from hashlib import sha1
from bs4 import BeautifulSoup
from os import path
THIS_FOLDER = path.dirname(path.abspath(__file__))
RegisteredMail = path.join(THIS_FOLDER, "registeredmails.txt")
RegisteredMailServ = path.join(THIS_FOLDER, "registeredmailswithserv.txt")
GeneratedMail = path.join(THIS_FOLDER, "generatedmails.txt")
print(Back.BLACK)
print(Fore.CYAN)
print(Style.DIM)
print("""Script by Zevi/Скрипт сделан Zevi
┌────────────────────────────────────┐
│Author :  LilZevi&Gefest                 │   
│Github : https://github.com/LilZevi │
└────────────────────────────────────┘
YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ
Telegram: @NowNameBo
▄▀█ █▀▄▀█ █ █▄░█ █▀█ ▄▀█ █░█ ▀█▀ █▀█ █▀█ █▀▀ █▀▀ █▄▄ █▀█
█▀█ █░▀░█ █ █░▀█ █▄█ █▀█ █▄█ ░█░ █▄█ █▀▄ ██▄ █▄█ █▄█ █▄█
Version = 4.2
1.Autoreg with your mail server|If u have one|/Авторег для вашего почтового сервера
2.AutoReg for Amino/Авторег для амино
3.Generate emails/Сгенерировать почты""")
emailselect = input("Type Number/Введите Цифру: ")

		#email generator def
def emailgenerator():
		try:
			mail = secmail.SecMail()
			email = mail.generate_email()
			print(f"Generated {email}")
			for i in range(emailnumber):
				emailsgenerating = email
				emails = open(GeneratedMail, 'a+')
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

		#autoregdef
def autoregforamino():
	try:
		thedeviceId = deviceIdgenerator()
		password = input("Password for All Accounts: ")
	except:
		return  
	while True:
		thedeviceId = deviceIdgenerator()	
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
			write_mail = open(RegisteredMail, 'a+')
			write_mail.write(email + '\n')
			write_mail.close()
		except amino.lib.util.exceptions.IncorrectVerificationCode:
			print("IncorrectVerificationCode")
			print("Неверный код верификаций")
			return  
		except amino.lib.util.exceptions.AccountLimitReached:
			print("Account Limit Reached")
			print("Превышен лимит аккаунтов")
			return  
		except amino.lib.util.exceptions.InvalidEmail:
			print("Invalid Email")
			print("Неверная почта")
			return  
		except amino.lib.util.exceptions.EmailAlreadyTaken:
			print(f"Email Already Taken {email}")
			print(f"Эту почту уже использовали {email}")
			return  
		except amino.lib.util.exceptions.UnsupportedEmail:
			print(f"UnsupportedEmail {email}")
			print(f"Неподдерживаемая почта {email}")
			return  
		except amino.lib.util.exceptions.CommandCooldown:
			print("CommandCooldown")
			print("Кулдаун команды,можно обойти сменив ip")
			return  
		except amino.lib.util.exceptions.VerificationRequired as e:    #здесь запрашивается ручная верефикация
			print(f"Verification required for {email}")
			print(f"Запрашивается верификация для почты {email}")
			url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")
			webbrowser.open_new(str(url))
			input("Press Enter: ")	
		except Exception as e:
			print(str(e))
			return  
		#autoregdef

	#randomly generate mails name for emailserver
def creatingemailname():
	letters_and_digits = string.ascii_letters + string.digits
	mailName =''.join(secrets.choice(letters_and_digits) for i in range(25))
	return mailName
	#randomly generate mails name for emailserver


	#def for getting link	
def gettingthelink(maildomain, CentralMailPass, CentralMail):
	mail = imaplib.IMAP4(maildomain)
	mail.login(CentralMail,CentralMailPass)
	mail.list()
	mail.select("inbox")
	readStatus, messages = mail.search(None,'UnSeen')
	if readStatus == "OK" and messages[0] != b"":
		readStatus, data = mail.store(messages[0].replace(b' ',b','),'+FLAGS','\\SEEN')
		for i in messages[0].split(b" "):
			readStatus, msg = mail.fetch(i, "(RFC822)")
			RawLink = re.search("<a href=\".*?(?=\")",str (msg))
			ClearedLink = RawLink.group()[9:]
	return ClearedLink
	#def for getting link


	#def autoregwithserv
def autoregwithserv():
	try:
		password = input("Password for All Accounts: ")
		maildomain = input("domain(for example: mail.mails.da):  ") 
		CentralMail = input("Email to which all letters are forwarded:  ")
		CentralMailPass = input("Password: ")
	except:
		return  None
	while True:
		thedeviceId = deviceIdgenerator()	
		client = amino.Client()
		email=creatingemailname()+"@"+maildomain   
		client.request_verify_code(email=email)
		time.sleep(4)
		nick = generate('en')
		print(f'Email/Почта: {email}')
		print(f'Password/Пароль: {password}')
		print(f'DeviceId/Девайсайди: {thedeviceId}')
		link = gettingthelink(maildomain, CentralMailPass, CentralMail)
		print(f"Verification Link/Ссылка на верификацию: {link}")
		webbrowser.open_new_tab(link)
		try:
			theverificationcode = input("Verification code/Код верификаций: ")
			client.register(nickname=nick, email=email, password=password, verificationCode=theverificationcode, deviceId=thedeviceId)
			print(f"{email} Registered/Зарегистрировали")
			client.login(email=email, password=password)
			client.request_verify_code(email=email)
			time.sleep(4)
			link = gettingthelink(maildomain,CentralMailPass,CentralMail)
			print(f"Verification Link/Ссылка на верификацию: {link}")
			webbrowser.open_new_tab(link)
			accountactivatingcode = input("Verification code/Код верификаций: ")
			client.activate_account(email=email, code=accountactivatingcode)
			print(F"{email} Activated Account/Активировали аккаунт")
			write_mail = open(RegisteredMailServ, 'a+')
			write_mail.write(email+'\n')
			write_mail.close()
		except amino.lib.util.exceptions.IncorrectVerificationCode:
			print("IncorrectVerificationCode")
			print("Неверный код верификаций")
			return  
		except amino.lib.util.exceptions.AccountLimitReached:
			print("Account Limit Reached")
			print("Превышен лимит аккаунтов")
			return  
		except amino.lib.util.exceptions.InvalidEmail:
			print("Invalid Email")
			print("Неверная почта")
			return  
		except amino.lib.util.exceptions.EmailAlreadyTaken:
			print(f"Email Already Taken {email}")
			print(f"Эту почту уже использовали {email}")
			return  
		except amino.lib.util.exceptions.UnsupportedEmail:
			print(f"UnsupportedEmail {email}")
			print(f"Неподдерживаемая почта {email}")
			return  
		except amino.lib.util.exceptions.CommandCooldown:
			print("CommandCooldown")
			print("Кулдаун команды,можно обойти сменив ip")
			return  
		except amino.lib.util.exceptions.VerificationRequired as e:        #здесь запрашивается ручная верефикация по идее
			print(f"Verification required for {email}")
			print(f"Запрашивается верификация для почты {email}")
			url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")
			webbrowser.open_new(str(url))
			input("Press Enter: ")		
		except Exception as e:
			print(str(e))
			return  
	#def autoregwithserv


#choices
if emailselect == "1":
	autoregwithserv()

elif emailselect == "2":
	autoregforamino()

elif emailselect == "3":
	emailnumber = int(input("How Much Email Generate?: "))
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		_ = [executor.submit(emailgenerator) for _ in range(emailnumber)]
	print(f"Created => {emailnumber} emails in file generatedmails.txt")
	print(f"Создано => {emailnumber} почт в файле generatedmails.txt")
