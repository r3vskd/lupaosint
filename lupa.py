from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from argparse import ArgumentParser
from requests.exceptions import MissingSchema
import subprocess
import requests
import socket
import time
import json
import sys
import re
#######################################################################################
print('\x1b[33;92m'" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██╗░░░░░██╗░░░██╗██████╗░░█████╗░░█████╗░░██████╗██╗███╗░░██╗████████╗ "'\x1b[0m')
print('\x1b[33;92m'" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⣠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀██║░░░░░██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝ "'\x1b[0m')
print('\x1b[33;92m'" ⠀⠀⠀⠀⠀⠀⠀⡀⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀██║░░░░░██║░░░██║██╔═══╝░██╔══██║██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░ "'\x1b[0m')
print('\x1b[33;92m'" ⠀⠀⠀⠀⠀⠐⢿⣷⡄⠙⠋⠉⠀⠀⠀⠀⠉⠙⠻⢿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀███████╗╚██████╔╝██║░░░░░██║░░██║╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░ "'\x1b[0m')
print('\x1b[33;92m'" ⠀⠀⠀⠠⣿⣦⡀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⡄⠀⠀⠀⠀⠀╚══════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░ "'\x1b[0m')
print('\x1b[33;92m'" ⠀⠀⢰⣦⣄⠉⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡆⠀⢀⠀⠀█▀▀▄ █──█ 　 █▀▀█ █▀▀█ ▀█─█▀ █▀▀ █─█ █▀▀▄ |https://github.com/r3vskd"'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⣿⣿⠇⠀⠀⠀⣼⠟⠀⢀⣤⡶⢶⣦⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⠟⠛⠃⠀ █▀▀▄ █▄▄█ 　 █▄▄▀ ──▀▄ ─█▄█─ ▀▀█ █▀▄ █──█ |https://twitter.com/r3vskd"'\x1b[0m')
print('\x1b[33;92m'"⠀⢸⣿⣿⠀⠀⠀⢰⡿⠀⢠⡟⠁⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀ ▀▀▀─ ▄▄▄█ 　 ▀─▀▀ █▄▄█ ──▀── ▀▀▀ ▀─▀ ▀▀▀─  "'\x1b[0m')
print('\x1b[33;92m'"⠀⢸⣿⣿⠀⠀⠀⠸⣷⠀⠸⣧⠀⣴⣿⣷⣼⠇⠀⣿⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀ v1.0 "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⣿⣿⡆⠀⠀⠀⠻⣆⠀⠙⠳⠾⠿⠟⠋⢀⣼⠏⠀⡀⠀⣸⠇⠀⠀⠀⠀⠀  "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⠘⣿⣿⣄⠀⠀⠀⠈⠳⣦⣤⣤⣤⣤⡶⠟⠁⣠⣾⣿⣿⣿⣤⣀⠀⠀⠀⠀  "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⠀⠘⢿⣿⣦⡀⠀⠀⠀⠀⠈⠉⠉⠀⣀⣤⣶⣿⣿⣿⣿⣿⡟⠙⠻⠂⠀⠀  "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⠀⢀⣼⡿⠋⠙⠷⣤⣀⡀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀  "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀  "'\x1b[0m')
print('\x1b[33;92m'"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  "'\x1b[0m')

options={
        1:'Retrieve the IP address from any website',
        2:'Retrieve the country/city/province from the IP address',
        3:'Check if the IP address is alive',
        4:'Retrieve web servers that uses the host IP address',
        5:'Get email addresses from website',
        6:'Get phone numbers from wbsite',
        7:'HTTP/HTTPS headers check',
        8:'Exit\n \n',
        }

def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "⣿"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

def selection():
    for key in options.keys():
        print([key],'\x1b[33;92m' '' '\x1b0===>',options[key])
       ################## get IP from website url ########################
def option1():
    hostname=input("Enter website domain: ")
    print(f'The IP Address retrieved from-> [{hostname}] is-> [{socket.gethostbyname(hostname)}]')

       ###################### geolocation ########################
def option2():
    print('Enter IP: ') 
    bash= "read text && echo $text | whois $text | grep 'City\|StateProv\|Country'"
    open=subprocess.Popen(bash, shell=True)
    open.wait()

       ##################### alive or dead ############################
def option3():
    print('Enter IP & press CTRL+Z to finish: ')
    bash="read status && ping $status "
    open=subprocess.Popen(bash, shell=True)
    open.wait()

       ##################### web servers ############################     
def option4(): 
    print('Enter IP: ')
    bash= "read sv && echo $sv | whois $sv | grep 'NetName\|OrgName\|OrgNOCName'"
    open=subprocess.Popen(bash, shell=True)
    open.wait()

      ##################### email scrapper ###########################
def option5():
    print('Enter URL to retrieve all emails: ')
    bash="./scraper_emails.sh"
    open=subprocess.Popen(bash, shell=True)
    open.wait()
    #time.sleep(0.5)
    #bash="./scrapper_phone_numbers.sh"
    #open=subprocess.Popen(bash, shell=True)
    #open.wait()
    #time.sleep(0.5)

    ##################### phone number scraper ###########################
def option6():
    print('Enter URL to retrieve all emails: ')
    bash="./scraper_phone_numbers.sh"
    open=subprocess.Popen(bash, shell=True)
    open.wait()
    #time.sleep(0.5)
    #bash="./scrapper_phone_numbers.sh"
    #open=subprocess.Popen(bash, shell=True)
    #open.wait()
    #time.sleep(0.5)

    ##################### header ###############################
def option7():
    print('Enter URL to get the headers: ')
    bash= "read url && curl -I $url | head -n 13"
    open=subprocess.Popen(bash, shell=True)
    open.wait()

##################### inicio ###########################
if __name__=='__main__':
    while(True):
        print("\t")
        selection()
        option= '' 
        try:
            option= int(input('[''\x1b[33;92m''▬O''\x1b[0m'']' '>>> '))
        except:
            print('')
        if option==1:
          option1()
        elif option==2:
            option2() 
        elif option==3:
            option3()
        elif option==4:
            option4()
        elif option==5:
            option5()
        elif option==6:
            option6()
        elif option==7:
            option7()
        elif option==8:
           for i in progressbar(range(7), "Closing lupa0sint:", 20):
               time.sleep(0.1)
           exit()
        else:
            print('Try a valid option')

