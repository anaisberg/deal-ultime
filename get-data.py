from selenium import webdriver

url = "https://www.ledealultime.fr/"
with webdriver.Chrome() as driver:
    driver.get(url)

    print(driver.current_url) # https://www.zenrows.com/
    print(driver.title) #