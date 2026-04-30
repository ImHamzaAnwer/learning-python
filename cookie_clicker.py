import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")


time.sleep(3)

try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    time.sleep(3)
except NoSuchElementException:
    print("Language selection not found")


time.sleep(2)
cookie_btn = driver.find_element(By.ID, value="bigCookie")


def buy_products():
    try:
        products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
        best_item = None
        for product in reversed(products):
            if "enabled" in product.get_attribute("class"):
                best_item = product
                break

        if best_item:
            best_item.click()
    except (NoSuchElementException, ValueError):
        print("Couldn't find cookie count or items")


last_buy_time = 0
while True:
    cookie_btn.click()
    current_time = time.time()
    if current_time - last_buy_time >= 5:
        buy_products()  # Call your function
        last_buy_time = current_time

# driver.quit()
