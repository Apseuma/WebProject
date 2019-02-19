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

    def search_activities(self, page):
        tree = bs4.BeautifulSoup(page,"lxml")

        #ul = tree.find("ul", "goodlist_1")
        #li = ul.find_all("li")
        #act_list = []
        #for item in li:
        #   price = item.find("span","price").text
        #   title = item.find("span","title").text
        #   act_list.append((title, price))
        #return act_list

        activities = tree.find_all("span", "title")
        act_list = []
        i = 0
        for activity in activities:
            link = activity.find("a")
            act_list.append((link["href"]))
            i+=1
            if i >= 5 :
                break
        return act_list


    def run(self):
        page = self.download_page()
        data = self.search_activities(page)
        print (data)

if __name__ == "__main__":
     c = WebClient()
     c.run()
