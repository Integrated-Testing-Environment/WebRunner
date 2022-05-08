import sys

from je_web_runner import get_webdriver_manager

try:
    if __name__ == "__main__":
        driver_wrapper = get_webdriver_manager("firefox")
        driver = driver_wrapper.webdriver
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        driver_wrapper.set_driver("firefox")
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        driver_wrapper.set_driver("firefox")
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        driver_wrapper.set_driver("firefox")
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        driver_wrapper.set_driver("firefox")
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        driver_wrapper.set_driver("firefox")
        driver_wrapper.open_browser("http://www.python.org")
        print(driver.title)
        print(driver_wrapper.current_webdriver_list)
        driver_wrapper.quit()
except Exception as error:
    print(repr(error), file=sys.stderr)
    sys.exit(1)
