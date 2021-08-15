import pyfiglet
from autoregconfigs import autoregfunctions
from colored import fore, back, style, attr
attr(0)
print(fore.MEDIUM_PURPLE + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminoautoreg", font="chunky"))
autoregfunctions.main_menu()
emailselect = input("Type Number >> ")

if emailselect == "1":
	password = input("Password for All Accounts >> ")
	autoregfunctions.auto_register(password=password)
	
elif emailselect == "2":
	print("Nope Learn Python")
	print("Тебя заскамили мамонт")
