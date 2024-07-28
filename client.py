from socket import *
from colorama import Fore , init ; init()
import sys
import os
import platform
import time
#=====================================================================

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
#=====================================================================

print(Fore.GREEN + """
███████╗███████╗ ██████╗██████╗ ███████╗████████╗     ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
███████╗█████╗  ██║     ██████╔╝█████╗     ██║       ██║     ███████║███████║   ██║   
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║       ██║     ██╔══██║██╔══██║   ██║   
███████║███████╗╚██████╗██║  ██║███████╗   ██║       ╚██████╗██║  ██║██║  ██║   ██║   
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                   
""" + Fore.RESET)
#=====================================================================
connection = socket(AF_INET , SOCK_STREAM)
#==========================Connect to server==========================
try:
    Name = input(Fore.MAGENTA + "Enter your Name : " + Fore.RESET)
    Ip = input(Fore.MAGENTA + "\nEnter the server Ip : " + Fore.RESET)
    print(Fore.MAGENTA + "")
    Port =  int(input("Enter the port : " + Fore.RESET))

    connection.connect((Ip , Port))
except KeyboardInterrupt:
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")
except ConnectionRefusedError:
    exit(Fore.BLUE + "\nWrong IP or Port !" + Fore.RESET)

#=====================================================================
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
#=====================================================================
print(Fore.MAGENTA + """
 ██████╗██╗  ██╗ █████╗ ████████╗██████╗  ██████╗  ██████╗ ███╗   ███╗
██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
██║     ███████║███████║   ██║   ██████╔╝██║   ██║██║   ██║██╔████╔██║
██║     ██╔══██║██╔══██║   ██║   ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
╚██████╗██║  ██║██║  ██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝                                                                                                                                
""" + Fore.RESET)
#=====================================================================
connection.send(f"Say Hello to {Fore.YELLOW}{Name}{Fore.RESET} !".encode())
time.sleep(0.5)
connection.send(f"\n{Fore.YELLOW}{Name}{Fore.RESET} System is {Fore.BLUE}:{Fore.RESET} {platform.uname()[0]}".encode())
time.sleep(0.5)
connection.send(f"\nAnd Node is {Fore.BLUE}:{Fore.RESET} {platform.uname()[1]}".encode())


print(Fore.RED + "\n!end for end the chat \n".title() + Fore.RESET)

print(Fore.LIGHTWHITE_EX + "Wait for server Answer...\n".title())
#=====================================================================
try:
    while True:
        data = connection.recv(11111111).decode()
        print(f"\n{Fore.YELLOW}Server{Fore.RESET}{Fore.LIGHTWHITE_EX} Sended {Fore.BLUE}:{Fore.RESET} {data}")

        message = input(Fore.GREEN + "\n> > > " + Fore.RESET)

        connection.send(f"\n{Fore.YELLOW}{Name}{Fore.RESET}{Fore.LIGHTWHITE_EX} Sended {Fore.BLUE}:{Fore.RESET} {message}".encode())

        if message == "!end" or message == "!End":
            sys.exit()
        elif message == "\n":
            pass

except Exception:
    exit(Fore.RED + "server left the chat !".title() + Fore.RESET)
except KeyboardInterrupt:
    connection.close()
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")
#=====================================================================