# start the coding automate git cycle 
# import library's
import os
from colorama import Fore,init
import subprocess

c = input(Fore.GREEN+' [ + ] '+Fore.WHITE+'Please Enter your comment for commit : ')

add = os.system('git add -A')
comment = os.system(f'git commit -m "{ c }"')
print("\n")
print(Fore.GREEN+f" Commited by this commit ==> {comment.__str__} ")