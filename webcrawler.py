#!/usr/bin/env python3
from urllib.request import urlopen
from colorama import Fore
import hacker_news_crawler
import custom_text

"""Web crawler program for the page 'Hacker news'.
This program is a minimlist example of web crawling using scraping techniques.
This program only works for the page 'https://news.ycombinator.com/'.
"""

custom_text.title()

exit = 0
pageURL = 'https://news.ycombinator.com/'
page = urlopen(pageURL)
allData = hacker_news_crawler.scrapWeb(page)  # Initial reading of the page.

while exit == 0:

    custom_text.menu()
    option = input('Enter your choice and press return: ')

    if option == '1':
        custom_text.reload()
        page = urlopen(pageURL)
        allData = hacker_news_crawler.scrapWeb(page)
        custom_text.done()

    elif option == '2':
        custom_text.allEntries()
        for entry in allData.scrapedData:
            print(Fore.GREEN + entry[0] + Fore.RESET + '. ' + entry[1] + ', ' + str(entry[2]) +
                  ' points, ' + str(entry[3]) + ' comments.')

    elif option == '3':
        custom_text.filter()
        for entry in allData.filterNameOrderComments():
            print(entry[0] + '. ' + entry[1] + ', ' + str(entry[2]) +
                  ' points, ' + Fore.GREEN + str(entry[3]) + ' comments' + Fore.RESET + '.')

    elif option == '4':
        custom_text.filter()
        for entry in allData.filterNameOrderPoints():
            print(entry[0] + '. ' + entry[1] + ', ' + Fore.GREEN + str(entry[2]) +
                  ' points' + Fore.RESET + ', ' + str(entry[3]) + ' comments.')

    elif option == '5':
        userNumber = input('Custom number of entries: ')
        try:
            number = int(userNumber)
            custom_text.filter()
            for entry in allData.filterNameOrderComments(number):
                print(entry[0] + '. ' + entry[1] + ', ' + str(entry[2]) +
                      ' points, ' + Fore.GREEN + str(entry[3]) + ' comments' + Fore.RESET + '.')
        except ValueError:
            custom_text.errorOption()

    elif option == '6':
        userNumber = input('Custom number of entries: ')
        try:
            number = int(userNumber)
            custom_text.filter()
            for entry in allData.filterNameOrderPoints(number):
                print(entry[0] + '. ' + entry[1] + ', ' + Fore.GREEN + str(entry[2]) +
                      ' points' + Fore.RESET + ', ' + str(entry[3]) + ' comments.')
        except ValueError:
            custom_text.errorOption()

    elif option == '7':
        custom_text.help()

    elif option == '8':
        exit = 1

    else:
        custom_text.errorOption()
