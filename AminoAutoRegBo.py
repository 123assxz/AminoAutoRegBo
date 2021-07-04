import amino
import secmail
import concurrent.futures
import webbrowser
import time
import base64
import pyfiglet
import string 
import random
import json
from nickname_generator import generate
from hashlib import sha1
from bs4 import BeautifulSoup
from os import path
from colorama import init, Fore, Back, Style
init()
THIS_FOLDER = path.dirname(path.abspath(__file__))
RegisteredMail = path.join(THIS_FOLDER, "registeredmails.txt")
GeneratedMail = path.join(THIS_FOLDER, "generatedmails.txt")
print(Fore.BLACK + Style.BRIGHT)
print("""Script by Lil Zevi & Gefest
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoauto", font="speed"))
print(pyfiglet.figlet_format("regbo", font="speed"))
print("""Version = 5.7
[1] AutoReg for Amino
[2] Generate emails
[3] AccountGenerator for Amino""")
emailselect = input("Type Number >> ")

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
			return
		#email generator def

		#email generating process
def emailgeneratingprocess():
	emailnumber = int(input("How Much Email Generate?: "))
	with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
		_ = [executor.submit(emailgenerator) for _ in range(emailnumber)]
	print(f"Created => {emailnumber} emails in file generatedmails.txt")
		#email generating process
	
		#deviceidgenerator def thanks to gefest
def deviceIdgenerator(st : int = 69):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
    thedevice = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
    return thedevice

		#autoregdef
def autoreg():
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
		print(f'Email: {email}')
		print(f'Password: {password}')
		print(f'DeviceId: {thedeviceId}')
		client.request_verify_code(email=email)
		time.sleep(7)
		verifymsgid = mail.get_messages(email=email).id
		verifymsgid = verifymsgid[0]
		themail = mail.read_message(email, verifymsgid).htmlBody
		soup = BeautifulSoup(themail, 'lxml')
		quotes = soup.find_all('a')
		quotes = quotes[0].get('href')
		print(f"Verification Link: {quotes}")
		webbrowser.open_new_tab(quotes)
		nick = generate('en')
		try:
			theverificationcode = input("Verification code for register: ")
			client.register(nickname=nick, email=email, password=password, verificationCode=theverificationcode, deviceId=thedeviceId)
			print(f"{email} Registered")
			client.login(email=email, password=password)
			client.request_verify_code(email=email)
			time.sleep(7)
			verifymsgid = mail.get_messages(email=email).id
			verifymsgid = verifymsgid[0]
			themail = mail.read_message(email, verifymsgid).htmlBody
			soup = BeautifulSoup(themail, 'lxml')
			quotes = soup.find_all('a')
			quotes = quotes[0].get('href')
			print(f"Verification Link: {quotes}")
			webbrowser.open_new_tab(quotes)
			accountactivatingcode = input("Verification code for activating: ")
			client.activate_account(email=email, code=accountactivatingcode)
			print(F"{email} Activated Account")
			write_mail = open(RegisteredMail, 'a+')
			write_mail.write(email + '\n')
			write_mail.close()
		except amino.lib.util.exceptions.IncorrectVerificationCode:
			print("IncorrectVerificationCode")
			return  
		except amino.lib.util.exceptions.AccountLimitReached:
			print("Account Limit Reached")
			return  
		except amino.lib.util.exceptions.InvalidEmail:
			print("Invalid Email")
			return  
		except amino.lib.util.exceptions.EmailAlreadyTaken:
			print(f"Email Already Taken {email}")
			return  
		except amino.lib.util.exceptions.UnsupportedEmail:
			print(f"UnsupportedEmail {email}")
			return  
		except amino.lib.util.exceptions.CommandCooldown:
			print("CommandCooldown")
			return  
		except amino.exceptions.VerificationRequired as e:
			print("VerificationRequired for {email}")
			url = print(f"Verification Link: {e}")
			webbrowser.open_new(str(e))
			TheEnter = input("Press Enter: ")
		except Exception as e:
			print(str(e))
			return  
		#autoregdef


#choices
if emailselect == "1":
	autoreg()
	
elif emailselect == "2":
	emailgeneratingprocess()
	
elif emailselect == "3":
	print("Nope Learn Python")
	print("Тебя заскамили мамонт")
