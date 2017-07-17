import codecs
import hacker_news_crawler

"""Test definition.
Filter 1: Filter all previous entries with more than five words in the title ordered by amount of comments first.
Filter 2: Filter all previous entries with less than or equal to five words in the title ordered by points.

The scenes were obtained by directly coping the html code of ¨https://news.ycombinator.com/¨.

There to different type of tests:

number_entries: compare that the number the remained entries after the filter is the same.
order_entries: compare that the order of the entries are correct.
"""
page = codecs.open("html_scene_1.html", 'r')
allData = hacker_news_crawler.scrapWeb(page)


def test_scene1_filter1_number_entries():
    numberEntries = len(allData.filterNameOrderComments())
    assert numberEntries == 9


def test_scene1_filter1_order_entries():
    order = ['26', '22', '16', '20', '14', '12', '21', '11', '6']
    entriesOrder = [index[0] for index in allData.filterNameOrderComments()]
    assert entriesOrder == order


def test_scene1_filter2_number_entries():
    numberEntries = len(allData.filterNameOrderPoints())
    assert numberEntries == 21


def test_scene1_filter2_order_entries():
    order = ['10', '29', '17', '24', '3', '5', '25', '13', '1', '27',
             '7', '2', '4', '23', '30', '18', '9', '19', '28', '15', '8']
    entriesOrder = [index[0] for index in allData.filterNameOrderPoints()]
    assert entriesOrder == order


page = codecs.open("html_scene_2.html", 'r')
allData2 = hacker_news_crawler.scrapWeb(page)


def test_scene2_filter1_number_entries():
    numberEntries = len(allData2.filterNameOrderComments())
    assert numberEntries == 9


def test_scene2_filter1_order_entries():
    order = ['5', '8', '18', '20', '3', '16', '23', '21', '13']
    entriesOrder = [index[0] for index in allData2.filterNameOrderComments()]
    assert entriesOrder == order


def test_scene2_filter2_number_entries():
    numberEntries = len(allData2.filterNameOrderPoints())
    assert numberEntries == 21


def test_scene2_filter2_order_entries():
    order = ['26', '24', '15', '11', '2', '29', '9', '1', '10', '6',
             '28', '27', '19', '7', '22', '12', '14', '25', '30', '4', '17']
    entriesOrder = [index[0] for index in allData2.filterNameOrderPoints()]
    assert entriesOrder == order
