import requests
from bs4 import BeautifulSoup
import time


class Sitemap:
    def __init__(self, SiteMapURL, uaName='OldTaoge-OpenSource'):
        self.SiteMapURL = SiteMapURL
        self.SiteURL = []
        self.ua = 'Mozilla/5.0 (compatible; ' + uaName + '-render/2.0; )'
        self.Mobileua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; ' + uaName + '-render/2.0;)'
        self.URLScan(SiteMapURL)


    def URLScan(self, url):
        res = requests.get(url, headers={'User-Agent': self.ua})
        requests.get(url, headers={'User-Agent': self.Mobileua})
        # print(res.text)
        soup = BeautifulSoup(res.text, "lxml")
        for i in range(2, 2147483647):
            newUrl = soup.select("body > div:nth-child(3) > table > tr:nth-child("+str(i)+") > td:nth-child(1) > a")
            try:
                newUrl[0]
            except IndexError:
                break
            else:
                if newUrl[0].attrs["href"] not in self.SiteURL:
                    time.sleep(1)
                    self.SiteURL.append(newUrl[0].attrs["href"])
                    print(newUrl[0].attrs["href"])
                    self.URLScan(newUrl[0].attrs["href"])




