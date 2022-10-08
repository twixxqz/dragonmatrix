import os
from time import sleep

os.system('clear')
os.system('sudo dnf install cowsay')
sleep(4)
os.system('clear')
os.system('cowsay -f dragon "Hello!"')
sleep(5)
os.system('sudo dnf install cmatrix')
os.system('cmatrix')