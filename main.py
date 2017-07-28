import random
from datetime import datetime
from line_art import *
import saved_items
import sys
import time

if __name__ == "__main__":
    # Clear screen
    print("\033[1;1H\033[J")
    print_pokemon()
    time.sleep(3)

    # Clear screen
    print("\033[1;1H\033[J")
    # Change colors
    print("\033[33m")
    print_pikachu()
    time.sleep(3)

    #print("")
    #print("Welcome!")
    #random.seed(datetime.now())
    #print(random.randint(0, 9))
    #saved_items.initialize()
    #saved_items.close()

    # http://www.termsys.demon.co.uk/vtansi.htm

    # Change colors
    print("\033[43;34;5m")
    # Clear screen
    print("\033[1;1H\033[J")
    # Show welcome
    print("\033[1;1HWelcome!")
    # Prompt input
    if sys.version_info[0] == 2:
        name = raw_input("Your name? > ")
    else:
        name = input("your name? > ")
    # Clear line
    print("\033[1A\033[2K\033[1A")
    delay = 0.15
    time.sleep(delay)
    print("\033[1;1H elcome!")
    time.sleep(delay)
    print("\033[1;1H  lcome!")
    time.sleep(delay)
    print("\033[1;1H   come!")
    time.sleep(delay)
    print("\033[1;1H    ome!")
    time.sleep(delay)
    print("\033[1;1H     me!")
    time.sleep(delay)
    print("\033[1;1H      e!")
    time.sleep(delay)
    print("\033[1;1H       !")
    time.sleep(delay)
    print("\033[1;1H        ")


    print("Bye bye " + name)
    time.sleep(3)

    # Reset console
    print("\033c")
