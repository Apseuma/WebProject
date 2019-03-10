from urllib.request import urlopen
import bs4

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()


    def download_page(arg):
        # connect to the web site
        f = urlopen("https://www.banggood.com/Flashdeals.html")
        # get the download page
        page = f.read()
        # close the connection
        f.close
        return page

    def get_offers(self, page):

        tree = bs4.BeautifulSoup(page,"lxml")

        ul = tree.find("ul", "goodlist_1")
        li = ul.find_all("li")
        offers = []
        i = 1

        for item in li:
            offer = []
            offer.append(i)
            offer.append(item.find("span","title").text)
            offer.append(item.find("span","price").text)
            offer.append(item.find("span","price_old").text)
            i+=1

            offers.append(offer)

        return offers

    def print_offers (self, offers):
        for offer in offers:
            print("OFFER NUMBER " + str(offer[0]) + ":" +
                 "\nNOW YOU CAN BUY: " + offer[1] +
                 "\nTHE PRICE IS JUST: " + offer[2] +
                 "\nTHE PREVIOUS PRICE WAS: " + offer[3] + "\n")

    def run(self):
        page = self.download_page()
        offers = self.get_offers(page)
        print("\n") #just aestethic
        self.print_offers(offers)


if __name__ == "__main__":
     c = WebClient()
     c.run()
