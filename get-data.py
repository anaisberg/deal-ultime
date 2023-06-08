from selenium import webdriver

url = "https://www.ledealultime.fr/"

options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome(options=options) as driver:
    driver.get(url)

    print(driver.current_url) # https://www.zenrows.com/
    print(driver.title) #