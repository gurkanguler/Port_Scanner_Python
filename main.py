import os
import sys
import time
import platform
import socket
import argparse


# Error Message
def ErrorMessage(msg):
    print("\n\033[1;31m[-] %s \033[0m\n" % msg)

# Success Message
def successMessage(msg):
    print("\033[1;32m[+] %s \033[0m\n" % msg) 


# resetColor
def resetColor():
    print("\033[0m")

# checkOs
def checkOs():
    return platform.system()


# clearScreen
def clearScreen():
    if checkOs() == "Windows":
        ErrorMessage("It's not for windows")
    else:
        os.system("clear")

# PortScanner
class PortScanner:
    # main function
    def __init__(self, target_addr):
        # call to clearScreen Function
        clearScreen()
        # call to banner function in this class
        self.banner()
        self.target_addr = target_addr
        self.target = "www" in self.target_addr
        if self.target == True:
            successMessage("Target Website => %s " % self.target_addr)
            successMessage("Target IP Address => %s " % self.convert_to_ip())
            successMessage("Port Scanner Started...\n")
            self.portScanner()
        elif self.target == False:
            successMessage("Target IP Address => %s " % self.target_addr)
            self.portScannerIp()

    
    def convert_to_ip(self):
        self.ip_addr_split = self.target_addr.split("https://")[1]
        self.ip_addr = socket.gethostbyname(self.ip_addr_split)
        return self.ip_addr

    def banner(self):
        try:
            import pyfiglet
        except ImportError as err:
            ErrorMessage(err)
            os.system("sudo pip3 install pyfiglet")
        finally:
            self.f = pyfiglet.figlet_format("Port\nScanner", font="small")
            print("\033[1;32m")
            print(self.f)
            print(">>> Coded by gurkan <<<")
            resetColor()
    def portScanner(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for self.port in range(0,6666):
                self.result = self.sock.connect_ex((self.convert_to_ip(), self.port))
                if self.result == 0:
                    successMessage("Port Number -> %s -> %s" % (self.port, self.getPortName()))
        except socket.error as err:
            ErrorMessage(err)

    def portScannerIp(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for self.port in range(0,6666):
                self.result = self.sock.connect_ex((self.target_addr, self.port))
                if self.result == 0:
                    successMessage("Port Number -> %s -> %s" % (self.port, self.getPortName()))
        except socket.error as err:
            ErrorMessage(err)

    def getPortName(self):
        try:
            self.portName = socket.getservbyport(self.port)
            return self.portName
        except socket.error as err:
            ErrorMessage(err)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("-t", "--target", help="Enter to target address")
    user_args = vars(args.parse_args())
    target_addr = user_args["target"]
    port_scanner = PortScanner(str(target_addr))