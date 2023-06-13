from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ledealultime.fr/"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

def get_data():
    allDeals = []
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
            restaurant = names[3].text
            deal = names[8].text
            address = item.find_element(By.TAG_NAME, "p").text
            allDeals.append([restaurant, deal, address])
            
    return allDeals
