from colors import *
import util
from classy import*
import sys
import main


def menu_structure():
    menu = [the_sqirrel, the_knight, the_wizzard]
    instruction = print('{:^52}'.format("Press <--A or D--> to choose\n"),'{:^21}'.format("Confirm by S"))
    choose = print('{:^48}'.format("Choose character.\n"))
    return [choose, menu, instruction]

def menu_print(structure, num):
    CHOOSE = 0
    MENU = 1
    INSTRUCTION = 2

    print()
    print(f'{structure[CHOOSE]}', COLOR.BLUE)
    # print()
    print(f'{structure[MENU][num]}', COLOR.LIGHTGREEN)
    print()
    print(f'{structure[INSTRUCTION]}', COLOR.RED)
    # print(num)  ###############

def start_menu_handler(key, option):
    # print(key)
    output = True
    if key == 'a':
        option -= 1
    if key == 'd':
        option += 1
    if key == '0':
        output = False
    if key == 's':
        output = change_char(option)
    num = handle_menu_option(option)
    return [output, num]

def change_char(character):
    output = True
    if character == 0:
        util.clear_screen()
        print(the_sqirrel)
        return the_sqirrel
    elif character == 1:
        util.clear_screen()
        print(the_knight)
        return the_knight
    elif character == 2:
        util.clear_screen()
        print(the_wizzard)
        return the_wizzard
    else:
        key = util.key_pressed()
        if key == 'q':
            sys.exit()
            
    return output


def handle_menu_option(number_to_check):
    menu_option = 1
    if number_to_check < 0:
        number_to_check = len(menu_structure()[menu_option])-1
    elif number_to_check == len(menu_structure()[menu_option]):
        number_to_check = 0
    return number_to_check


def start_menu():
    FIRST_ELEMENT = 0
    SECOND_ELEMENT = 1
    num = 0
    
    is_running = True
    while is_running:
        print("             WELCOME IN RUN FOREST!\n")
        util.clear_screen()
        menu_print(menu_structure(), num)
        key = util.key_pressed()
        menu_handler_options = start_menu_handler(key, num)
        is_running = menu_handler_options[FIRST_ELEMENT]
        num = menu_handler_options[SECOND_ELEMENT]
    main.main()
        

start_menu()