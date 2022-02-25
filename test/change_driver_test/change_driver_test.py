from selenium_wrapper import get_webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

if __name__ == "__main__":
    driver_wrapper = get_webdriver("firefox")
    driver = driver_wrapper.webdriver
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.set_driver("chrome")
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.set_driver("firefox")
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.set_driver("chrome")
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.set_driver("firefox")
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.set_driver("chrome")
    driver_wrapper.open_browser("http://www.python.org")
    print(driver.title)
    driver_wrapper.quit()
