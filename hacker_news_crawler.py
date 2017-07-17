from bs4 import BeautifulSoup
import unidecode


class scrapWeb:
    """Class to scraping the page  'https://news.ycombinator.com/'.
    This class only can be used with the Hacker news page.

    filterNameOrderComments(number)
        This method filters all entries with more than a given 'number' of words.
        The input variable 'number' is the threshold. By default 'number' is set to 5.
        Return the filtered list ordered by amount of comments first.

    filterNameOrderPoints(number)
        This method filters all entries with less than or equal than a given 'number' of words.
        The input variable 'number' is the threshold.  By default 'number' is set to 5.
        Return the filtered list ordered by amount of points first.

    """

    def __init__(self, page):
        self.scrapedData = []
        soup = BeautifulSoup(page, 'html.parser')
        entry_subtexts = soup.find_all("td", {"class": "subtext"})
        entry_mains = soup.find_all("tr", {"class": "athing"})

        for entry_main in entry_mains:
            entry_id = entry_main["id"]
            rank = entry_main.find("span", {"class": "rank"}).string
            rank = rank.replace('.', '')
            name = entry_main.find("a", {"class": "storylink"}).string
            score = "0"
            for subtext in entry_subtexts:
                if subtext.find("span", {"id": "score_" + entry_id}):
                    score = subtext.find("span", {"id": "score_" + entry_id}).string
                    score = score.split(" ")[0]

                    comments = subtext.find_all(
                        "a", {"href": "item?id=" + entry_id})[1].string
                    comments = unidecode.unidecode(comments)
                    comments = comments.split(" ")
                    if len(comments) == 1:
                        comments = "0"
                    else:
                        comments = comments[0]

            self.scrapedData.append((rank, name, int(score), int(comments)))

    def filterNameOrderComments(self, number=5):
        filterData = [entry for entry in self.scrapedData if len(entry[1].split(" ")) <= number]
        filterData.sort(key=lambda x: x[3])
        return filterData

    def filterNameOrderPoints(self, number=5):
        filterData = [entry for entry in self.scrapedData if len(entry[1].split(" ")) > number]
        filterData.sort(key=lambda x: x[2])
        return filterData
