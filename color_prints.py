#import os
#os.system("") #enables ANSI escape characters in terminal

import colorama
colorama.init() #enables ANSI escape characters in terminal


# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text:str, effect:str=WHITE) -> None:
	output = f'{effect}{text}{RESET}'
	print(output)




#print(RED, 'Hi. i am in red color.',RESET)
color_print('Hi i am from function. and i am colored')


