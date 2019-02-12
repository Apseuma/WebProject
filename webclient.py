
 # downLoad a web page
 # search activities in web page
 # print the activities

import urllib

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()


    def download_page(arg):
        # connect to the web site
        f = urllib.urlopen("http://www.eps.udl.cat/ca/")
        # get the download page
        page = f.read()
        # close the connection
        f.close
        return page


    def run(self):
        page = self.download_page()
        print(page)

if __name__ == "__main__":
     c = WebClient()
     c.run()
