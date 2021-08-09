from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep
import time

class BarScraper():
    def __init__(self, barName, city):
        self.bar = barName
        self.city = city

        page = 'https://www.google.com/search?q=' + barName + '+' + city

        # Create a headless browser
        opts = Options()
        opts.headless = True
        self.browser = Firefox(options=opts)
        self.browser.get(page)

        # Get and track popular times for today
        self.busyness = {}
        self.times = []
        self.pixels = []

        # Get and track other items
        self.rating = ''
        self.website = ''

    def getPopTimes(self):
        '''
        Query the page to populate dict of times and busyness level
        '''

        # Sleep to give page time to load
        sleep(1)

        # Get all containers containing busyness data
        hoursData = self.browser.find_elements_by_css_selector('div.wYzX9b')
        busyData = self.browser.find_elements_by_css_selector('div.cwiwob')

        # Filter the items into a time:pixel dict
        for hour in hoursData:
            self.times.append(hour.get_attribute('data-hour'))
        for busy in busyData:
            # Busyness is displayed as pixel height between 0 and 75 pixels inclusive
            px = float(busy.get_attribute('style').split(' ')[-1].split(';')[0].split('p')[0])
            # Convert pixel height to a percentage
            pctBusy = int((px/75)*100)
            self.pixels.append(pctBusy)
        i = 0
        while i < len(hoursData):
            self.busyness[self.times[i]] = self.pixels[i]
            i += 1

        return self.busyness

    def getRatings(self):
        '''
        Query the page to get the rating
        '''

        # Sleep to give page time to load
        sleep(1)

        # Get the ratings using XPath
        rating = self.browser.find_elements_by_css_selector("span.Fam1ne.EBe2gf")
        stars = rating[0].get_attribute('aria-label')
        # Process response to get just the number of stars
        stars = stars.split(" ")
        stars = stars[1]
        self.rating = stars

        return self.rating

    def getWebsite(self):
        '''
        Query the page to get the website URL
        '''

        # Sleep to give page time to load
        sleep(1)

        # Get URL using XPath
        pages = self.browser.find_elements_by_css_selector("a.ab_button")
        page = pages[0]
        url = page.get_attribute('href')
        self.website = url

        return self.website

    def closeBrowser(self):
        self.browser.close()

