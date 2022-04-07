from components import vars
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import emoji



def total(value):
  character = ""
	
  if value == 0:
      character = vars.character = vars.characters[0]

  elif value > 0 and value < 200:
      character = vars.character = vars.characters[1]       

  elif value >= 200:
      character = vars.character = vars.characters[2]
            
  print(Back.MAGENTA + "It's " + character)
  print(emoji.emojize('Python is :thumbs_up:'))