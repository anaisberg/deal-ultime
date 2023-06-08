from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ledealultime.fr/"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

with webdriver.Chrome(options=options) as driver:
    driver.get(url)

    print(driver.current_url) # https://www.zenrows.com/
    print(driver.title) #

    # find element by id
    # driver.find_element(By.ID, "twotabsearchtextbox")

    # find element by CSS selector
    # driver.find_element(By.CSS_SELECTOR, "form[role='search'] input[type='text']")

    # find elements by class name
    # items = driver.find_elements(By.CLASS_NAME, "a-list-item")

    items = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')
    for item in items:
        names = item.find_elements(By.TAG_NAME, "span")
        print(names[3].text)
        promo = names[8].text
        print(promo)
        address = item.find_element(By.TAG_NAME, "p")
        print(address.text)
    
