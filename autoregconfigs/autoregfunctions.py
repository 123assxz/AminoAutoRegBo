import amino
import secmail
import time
import terminal_banner

from nickname_generator import generate
from bs4 import BeautifulSoup

def main_menu():
	print("""Version = 1.1.4
[1] AutoReg for Amino
[2] AccountGenerator for Amino""")

def auto_register(password):
	deviceIds = open("deviceids.txt")
	deviceId = str(deviceIds.readline()).strip()
	while True:
		mail = secmail.SecMail()
		client = amino.Client()
		email = mail.generate_email()
		nick = generate('en')
		print(terminal_banner.Banner(f"\nEmail >> {email}, \nPassword >> {password}, \ndeviceID >> {deviceId}\n"))
		try:
			client.register(nickname=nick, email=email, password=password, deviceId=deviceId)
			print(f"{email} Registered")
			client.login(email=email, password=password)
			client.request_verify_code(email=email)
			time.sleep(3)
			verifymsgid = mail.get_messages(email=email).id
			verifymsgid = verifymsgid[0]
			themail = mail.read_message(email, verifymsgid).htmlBody
			soup = BeautifulSoup(themail, 'lxml')
			quotes = soup.find_all('a')
			quotes = quotes[0].get('href')
			print(f"Verification Link >> {quotes}")
			accountactivatingcode = input("Verification code >> ")
			client.activate_account(email=email, code=accountactivatingcode)
			print(F"{email} Activated Account")
			write_mail = open("registeredmails.txt", 'a+')
			write_mail.write(f"{email}\n")
			write_mail.close()
		except amino.lib.util.exceptions.IncorrectVerificationCode:
			print("IncorrectVerificationCode")
			auto_register()
		except amino.lib.util.exceptions.AccountLimitReached:
			print("Account Limit Reached")
			deviceId = str(deviceIds.readline()).strip()
			print(f"New deviceID >> {deviceId}")
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
		except amino.lib.util.exceptions.VerificationRequired as e:
			print(f"VerificationRequired")
			link = e.args[0]['url']
			print(link)
			verify = input("Waiting for verification >> ")
			client.register(nickname=nick, email=email, password=password, deviceId=deviceId)
		except Exception as e:
			print(e)
			return
			
