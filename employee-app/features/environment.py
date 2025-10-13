from selenium import webdriver

def before_all(context):
    # Initialize the WebDriver here before all tests
    context.driver = webdriver.Chrome()  # You can change this to the appropriate WebDriver (e.g., Firefox)

def after_all(context):
    # Quit the WebDriver when all tests are done
    context.driver.quit()
