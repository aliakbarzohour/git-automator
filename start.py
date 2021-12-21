# start the coding automate git cycle 
# import library's
import os
from colorama import Fore,init
import subprocess

c = input(Fore.GREEN+' [ + ] '+Fore.WHITE+'Please Enter your comment : ')

add = os.system('git add -A')
comment = os.system(f'git commit -m "{ c }"')
status = os.system('git status')

print(Fore.GREEN+"Commited by this commit ==> "+Fore.WHITE+comment)