from colorama import Fore, Back, Style

"""Output text for the webcrawler program.
This module helps to maintain order of the main script and make easy its maintenance.
"""


def title():
    print(' ')
    print('WELCOME TO THE MINIMALIST HACKER NEWS CRAWLER')


def menu():
    print(' ')
    print(' ')
    print(Back.GREEN + 'MENU' + Back.RESET)
    print('1: Reload the page.')
    print('2: Show the 30 first entries.')
    print('3: Filter entries with more than five words in the title ordered by amount of comments.')
    print('4: Filter entries with less than or equal to five words in the title ordered by points.')
    print('5: Filter entries with more than a given number of words in the title ordered by amount of comments.')
    print('6: Filter entries with less than or equal to a given number of words in the title ordered by points.')
    print('7: Help.')
    print('8: Exit.')


def errorOption():
    print(' ')
    print(Fore.RED + 'Not a Valid Choice. ' + Fore.RESET + 'Please choose again.')


def help():
    print(' ')
    print(Back.YELLOW + 'HELP' + Back.RESET)
    print('-Load the page to refresh the search by selecting option ' +
          Fore.BLUE + Style.BRIGHT + '1' + Fore.RESET + Style.NORMAL + '.')


def filter():
    print(' ')
    print(Back.YELLOW + 'FILTER RESULT:' + Back.RESET)


def allEntries():
    print(' ')
    print(Back.YELLOW + 'ALL ENTRIES:' + Back.RESET)


def reload():
    print(' ')
    print(Back.YELLOW + 'RELOADING THE PAGE:' + Back.RESET)


def done():
    print(' ')
    print('Done!!')
