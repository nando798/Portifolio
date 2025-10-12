# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / "drivers" / "chromedriver.exe"


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )

    # chrome_options.add_argument'--headless'
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


if __name__ == "__main__":
    TIME_TO_SLEEP = 100  # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get("https://google.com/")
    # Espere para encontrar o input de pesquisa

    #

    try:
        search_imput = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_imput.send_keys("Selenium Python")
        search_imput.send_keys(Keys.ENTER)

        result = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        result = browser.find_element(By.ID, "search")
        links = result.find_elements(By.TAG_NAME, "a")
        links[0].click()

    except TimeoutException:
        print("Elemento de pesquisa não encontrado.")
    except NoSuchElementException:
        print("Elemento de pesquisa não encontrado.")

    # Dorme por 10 segundos
    sleep(TIME_TO_SLEEP)
