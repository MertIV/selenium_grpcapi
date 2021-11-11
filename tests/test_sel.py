from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver import DesiredCapabilities
from time import sleep
from qrcode import make
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

grid_url = "http://localhost:4444/wd/hub"

options = ChromeOptions()
# options.add_argument('--user-data-dir=/sel_sessions')
capabilities = options.to_capabilities()
driver = webdriver.Remote(command_executor=grid_url,desired_capabilities=capabilities, options=options)
print(driver.session_id)

driver.get("https://web.whatsapp.com/")
sleep(3)
qr = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-ref]")))

value = qr.get_attribute("data-ref")


print(value)

make(value).save("qr.png") #make my qr using the previous value

input()

driver.quit()