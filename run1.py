##
## This challenge is to grab the HTML document contained inside a HTML tag 
##

# 3rd-Party
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nerodia.browser import Browser

# https://stackoverflow.com/questions/56347625/how-to-get-the-html-document-contained-inside-an-html-tag-using-selenium-in-pyth



def setup_getDriver():
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
    #options.binary_location = "/Applications/Firefox-Dev.app/Contents/MacOS/firefox"  # MAC
    #options.binary_location = "C:\Program Files\Mozilla Firefox\firefox" # WIN

    # Run headless / no interface
    #options.add_argument('--headless')

    # Ignore HTTPs certificate errors 
    options.add_argument('--ignore-certificate-errors')

    # https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/
    driver = webdriver.Firefox(firefox_profile=ffprofile, options=options)
    driver.implicitly_wait(30)
    
    return driver


##### MAIN #####

TARGET_ENDPOINT = "file:///C:/red/nerodia/sample1/msweet.html"


try:
    d = setup_getDriver()

    # These steps are Selenium stuff 
    d.get( TARGET_ENDPOINT )
    d.switch_to.default_content()
    frame = d.find_element_by_xpath('/html/body/iframe[4]')
    d.switch_to.frame(frame)

    print( d.page_source )

except:
    logging.exception("!!! Fail at Selenium section !!!")
    logging.exception(sys.exec_info())


