import sys

from je_web_runner import get_webdriver_manager

try:
    if __name__ == "__main__":
        webdriver_manager = get_webdriver_manager("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        webdriver_manager.new_driver("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        webdriver_manager.new_driver("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        webdriver_manager.new_driver("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        webdriver_manager.new_driver("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        webdriver_manager.new_driver("firefox")
        webdriver_manager.webdriver_wrapper.to_url("http://www.python.org")
        print(webdriver_manager.current_webdriver_list)
        webdriver_manager.quit()
except Exception as error:
    print(repr(error), file=sys.stderr)
    sys.exit(1)
