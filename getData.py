from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ledealultime.fr/"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

def get_data():
    allDeals = []
    with webdriver.Chrome(options=options) as driver:
        driver.get(url)

        print(driver.current_url) 
        print(driver.title) 

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
            for name in names:
                print(name.text) 
            address = item.find_element(By.TAG_NAME, "p").text
            
            dealDetails = {
                "deal": deal,
                "restaurant": restaurant,
                "address":address,
                "latitude": 0,
                "longitude": 0,
            }
            allDeals.append(dealDetails)
            
    return allDeals


if __name__ == '__main__':
    get_data()