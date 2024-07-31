from socket import *
from colorama import Fore , init ; init()
import sys
import os
#=====================================================================
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
#=====================================================================

print(Fore.RED + """
███████╗███████╗ ██████╗██████╗ ███████╗████████╗     ██████╗██╗  ██╗ █████╗ ████████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
███████╗█████╗  ██║     ██████╔╝█████╗     ██║       ██║     ███████║███████║   ██║   
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║       ██║     ██╔══██║██╔══██║   ██║   
███████║███████╗╚██████╗██║  ██║███████╗   ██║       ╚██████╗██║  ██║██║  ██║   ██║   
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                      
""" + Fore.RESET)
#=====================================================================

Server = socket(AF_INET , SOCK_STREAM)

try:
    ip = input(Fore.MAGENTA + "Which ip you want open : ".title() + Fore.RESET)
    print(Fore.MAGENTA + "")
    port = int(input("Which port you want to open : ".title() + Fore.RESET))

    Server.bind((ip , port))

except KeyboardInterrupt:
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)" + Fore.RESET)
except OSError:
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} Wrong IP or Connection Error !" + Fore.RESET)
except ValueError:
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} Enter Some Value !" + Fore.RESET)

#=====================================================================

try:
    Server.listen(1)

except Exception:
    print(Fore.RED + "Write number by int !" + Fore.RESET)
    sys.exit()


print(f"\n{Fore.YELLOW}[+]{Fore.LIGHTWHITE_EX} Wating For Client ..." + Fore.RESET)

#=====================================================================
try:
    client , addr = Server.accept()
except KeyboardInterrupt:
                exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")

#=====================================================================
clear()
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

print(f"\nConnected to : {Fore.GREEN}{addr}\n" + Fore.RESET)

name = client.recv(1024).decode()
print(name)

system = client.recv(1024).decode()
node = client.recv(1024).decode()
print(system)
print(node)

print(Fore.RED + "\n!end for end the chat\n".title() + Fore.RESET)

print(Fore.GREEN + "=================================" + Fore.RESET)

#=====================================================================
try :
    while True:
        Message = input(Fore.GREEN + "\n> > > " + Fore.RESET)
        client.send(f"{Message}".encode())

        if Message == "!end" or Message == "!End":
            Server.close()
            sys.exit()
        elif Message == "\n":
            pass

        data = client.recv(11111111).decode()
        print(data)

except Exception:
    exit(Fore.RED + "client left the chat !".title() + Fore.RESET)
except KeyboardInterrupt:
    Server.close()
    exit(f"\n{Fore.RED}[-]{Fore.BLUE} User Exited :)")
#=====================================================================