from colored import fg, attr
import os
import requests
import json
import re
import string

def clean():
    os.system('cls')
print('\t%s' % (fg(251)))
print('\t%s██╗     ██╗███╗   ██╗██╗  ██╗██╗   ██╗███████╗██████╗ ████████╗██╗███████╗███████╗    ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗' % (fg(117)))
print('\t%s██║     ██║████╗  ██║██║ ██╔╝██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝' % (fg(117)))
print('\t%s██║     ██║██╔██╗ ██║█████╔╝ ██║   ██║█████╗  ██████╔╝   ██║   ██║███████╗█████╗      ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗' % (fg(117)))
print('\t%s██║     ██║██║╚██╗██║██╔═██╗ ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║╚════██║██╔══╝      ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║' % (fg(117)))
print('\t%s███████╗██║██║ ╚████║██║  ██╗ ╚████╔╝ ███████╗██║  ██║   ██║   ██║███████║███████╗    ██████╔╝   ██║   ██║     ██║  ██║███████║███████║' % (fg(117)))
print('\t%s╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝    ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝' % (fg(117)))
print('\t%sCrée par GalackQSM                                                                                                 Github.com/GalackQSM' %(fg(130)))
print('')
print('')

url = "https://bypass.bot.nu/bypass2?url="
old_link = input('[%s+%s] %sEntrer le lien Linkvertise : %s' % (fg(196), attr('reset'), fg(196), attr('reset')))
re = url + old_link
os.system("cls")
r = requests.get(re)
link = r.json()['destination']

print('\t%s' % (fg(251)))
print('\t%s██╗     ██╗███╗   ██╗██╗  ██╗██╗   ██╗███████╗██████╗ ████████╗██╗███████╗███████╗    ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗' % (fg(117)))
print('\t%s██║     ██║████╗  ██║██║ ██╔╝██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝' % (fg(117)))
print('\t%s██║     ██║██╔██╗ ██║█████╔╝ ██║   ██║█████╗  ██████╔╝   ██║   ██║███████╗█████╗      ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗' % (fg(117)))
print('\t%s██║     ██║██║╚██╗██║██╔═██╗ ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║╚════██║██╔══╝      ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║' % (fg(117)))
print('\t%s███████╗██║██║ ╚████║██║  ██╗ ╚████╔╝ ███████╗██║  ██║   ██║   ██║███████║███████╗    ██████╔╝   ██║   ██║     ██║  ██║███████║███████║' % (fg(117)))
print('\t%s╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝    ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝' % (fg(117)))
print('\t%sCrée par GalackQSM                                                                                                 Github.com/GalackQSM' %(fg(130)))
print('')
print('')

print('%s [+] Lien bypass :' % (fg(196)), fg(196) + link)


def main():
    os.system('title Linkvertise bypass by GalackQSM')



main()