from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep
import time

class BarScraper():
    def __init__(self, barName, city):
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

    def getPopTimes(self):
        '''
        Query the page to populate dict of times and busyness level
        '''

        # Sleep to give page time to load
        sleep(1)

        # Get all containers containing busyness data
        numOfItems = self.browser.find_elements_by_class_name('iWYMkd')
        hoursData = self.browser.find_elements_by_class_name('D6mXgd')
        busyData = self.browser.find_elements_by_class_name('cwiwob')

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
        while i < len(numOfItems):
            self.busyness[self.times[i]] = self.pixels[i]
            i += 1

        self.browser.close()
        return self.busyness