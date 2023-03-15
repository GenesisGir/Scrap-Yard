"""
                                ██████╗░██╗██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗
                                ██╔══██╗██║██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║
                                ██████╔╝██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝
                                ██╔═══╝░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░
                                ██║░░░░░██║███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░
                                ╚═╝░░░░░╚═╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░

                                ⣿⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
                                ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿
                                ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀
                                ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀
                                ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀
                                ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀
                                ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀
                                ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀
                                ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀
                                ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀
                                ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀
                                ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀
                                        source code by genesisgir
                                    
                            manipulate images and get color RGBA values and more!
"""

# import modules
import os, random, sys
import pyinputplus as pyip
from PIL import ImageColor
from PIL import *
import logging, logging.handlers

def logger(): # GenesisGir's typical logger preset! 🪵
    
    # importing modules
    import logging, logging.handlers
    from logging.handlers import SMTPHandler
    
    # create the logger and set severity
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # set logger level

    # create handles and set their severity
    
    # File Handlers
    file_handler = logging.FileHandler( 
    filename = r"Scrap-Yard\Labs-March-2023\pillowXKO01\pillowlogger.log",
    mode = 'w', # filemode 
    encoding = 'utf-8', # set encoding format
    delay = False, 
    errors = None)
    file_handler.setLevel(logging.DEBUG) # severity level


    
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] [Lvl:%(levelno)s] [%(funcName)s] [%(lineno)d] %(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p')

    # add formatter to handles
    file_handler.setFormatter(formatter)

    # adding the handler
    logger.addHandler(file_handler)
    
    return logger
    
# logger variable
logger = logger()

# method
def colour():
    """ # color()
    Returns the RBGA values of a color user has set or a random one from a list data type.
    """
    
    # colors list
    colors = ['RED', 'GREEN', 'BLUE', 'PINK', 'YELLOW', 'ORANGE', 'WHITE', 'BLACK']
    
    # color sunshine machine option stirs
    option = ['Choose your own colour', 'Generate a random colour', 'Exit Color Sunshine Machine v1.0.0']
    
    # colour  prompt
    while True:
        
        # user input
        resp = pyip.inputMenu(
            prompt='Colour Sunshine machine v1.0.0 \n', 
            choices=[option[0], option[1], option[2]],
            numbered=True)
        print()
        
        # conditionals
        if resp == option[0]: # user color
            
            while True:
                # exception handling
                try:
                    
                    # user input
                    resp = input('What colour would you like to get RGBA values from? \n')
                    print()

                    # user color value
                    user_colour = resp

                    # return user RGBA color values 
                    rgba_values = ImageColor.getcolor(color=user_colour, mode='RGBA')

                    # color output
                    message = print("The RGBA values of the colour %s are %s! \n" %(resp, rgba_values))
                    
                    # [INFO] [20]
                    logger.info("User generated a colour: %s and the RGBA values were %s" %(user_colour, rgba_values))
                    
                    break
                
                except: # invalid
                    # display to user they have entered invalid chars
                    print('Invalid characters, try again! \n')
                    continue
            continue
            
        elif resp == option[1]: # generate random color
            
            # exception handling
            try:
                # random colour
                rand_color = random.choice(seq=colors)

                # return arbitrary RGBA colour values
                rgba_values = ImageColor.getcolor(color=rand_color, mode='RGBA')

                # color output
                message = print("The RGBA values of the color %s are %s! \n" %(rand_color, rgba_values))
                
                # [INFO] [20]
                logger.info("A random colour was generated: %s and the RGBA values were %s" %(rand_color, rgba_values))
                continue
            
            except:
                pass
        
        elif resp == option[2]: # exit program
            print('Thank you for using Colour Sunshine Machine!')
            sys.exit()

        else:
            # [ERROR] [40]
            logger.error("An error has occured and a random colour could not be generated, check the list or code!")
            pass
    
# init
colour()