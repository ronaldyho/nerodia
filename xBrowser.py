##
## This is where you will want to make granular changes to every browser session
## Here are some of the things that you can potentially tweak
## - Browser Profile
##   - i.e. Set values within the Profile (Accept Untrusted Cert)
## - Browser Options
##

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nerodia.browser import Browser
# Mine
from lib._config import *
from lib.tbsqa_logging import *

import sys


def launchSite():

# Example
# - https://www.programcreek.com/python/example/100026/selenium.webdriver.FirefoxProfile
# Firefox profiles
# - 
# Firefox options
# - https://www.selenium.dev/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html

    from inspect import getsourcefile
    from os.path import abspath

    pathToHere = abspath(getsourcefile(lambda:0))


    ### 1 Create Firefox Profile instance and Options instance 
    ffprofile = webdriver.FirefoxProfile()
    options = webdriver.firefox.options.Options()

    # Set the download location
    ffprofile.set_preference('browser.download.dir', pathToHere)

    # Disable native events ( vs synthesized events)
    # Always set as False to prevent certain problems 
    ffprofile.set_preference('webdriver_enable_native_events', False)

    # Location of Browser executable 
    options.binary_location = "/Applications/Firefox-Dev.app/Contents/MacOS/firefox"  # MAC

    # Run headless / no interface
    #options.add_argument('--headless')

    # Ignore HTTPs certificate errors 
    options.add_argument('--ignore-certificate-errors')

    # https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/
    driver = webdriver.Firefox(firefox_profile=ffprofile, options=options)
    driver.implicitly_wait(30)
    #driver.maximize_window()

    ### 2 Create Nerodia session
    browserSession = Browser(driver)

    try:
        # Launch the website 
        browserSession.goto( API_ENDPOINT )

        return browserSession

    except:
        logging.exception("!!! Unable to create Browser Session !!!")
        logging.exception(sys.exec_info())



def launchSite_simple():
# Returns a BROWSER SESSION

    targetBrowser = 'Firefox'

    try:
        browserSession = Browser(browser=targetBrowser)
        browserSession.goto( API_ENDPOINT )

        return browserSession

    except:
        logging.exception("!!! Unable to create Browser Session !!!")
        logging.exception(sys.exec_info())



#### WATIR CODE Example 
#		Selenium::WebDriver::Firefox.path = "/Applications/Firefox-Dev.app/Contents/MacOS/firefox" ## Mac 
#		profile = Selenium::WebDriver::Firefox::Profile.from_name "watir"
#		profile['setAcceptUntrustedCertificates'] = true
#		profile.native_events = false    #disabled to prevent certain problems 
#		options = Selenium::WebDriver::Firefox::Options.new
#		options.profile = profile
#		return Watir::Browser.new( :firefox, :options => options )
