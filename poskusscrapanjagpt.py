from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pot do Chromedriverja (namestitev in nastavitev: https://sites.google.com/a/chromium.org/chromedriver/downloads)
chromedriver_path = './geckodriver.exe'

# Lokacija in časovni razpon
location = 'Europe'
start_date = '2023-01-01'
end_date = '2023-12-31'

# Mapa, kamor boste shranili CSV datoteko
download_folder = './data'

# Inicializacija brskalnika
options = webdriver.ChromeOptions()
options.add_argument('--download.default_directory=' + download_folder)
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Odpremo spletno stran
driver.get('https://worldfireatlas.copernicus.eu/en/webapp')

# Počakamo, da se naložijo vsi elementi strani
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'v-button-caption')))

# Nastavimo lokacijo in časovni razpon
location_input = driver.find_element(By.ID, 'gwt-uid-3')
location_input.clear()
location_input.send_keys(location)
location_input.send_keys(Keys.RETURN)

start_date_input = driver.find_element(By.ID, 'gwt-uid-5')
start_date_input.clear()
start_date_input.send_keys(start_date)
start_date_input.send_keys(Keys.RETURN)

end_date_input = driver.find_element(By.ID, 'gwt-uid-7')
end_date_input.clear()
end_date_input.send_keys(end_date)
end_date_input.send_keys(Keys.RETURN)

# Počakamo, da se naloži rezultat
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'download-button')))

# Poiščemo gumb za prenos CSV in ga kliknemo
download_button = driver.find_element(By.CLASS_NAME, 'download-button')
download_button.click()

# Počakamo nekaj sekund, da se datoteka prenese
import time
time.sleep(5)

# Zapremo brskalnik
driver.quit()
