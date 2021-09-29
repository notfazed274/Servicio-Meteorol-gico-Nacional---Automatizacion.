from selenium import webdriver
import pytest
import time
from SMN.Pages.smnHomePage import smnHomePage

class Testsmn():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=r'C:/Users/Federico/AppData/Local/Programs/Python/Python39/Scripts/chromedriver.exe')
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('https://www.smn.gob.ar/')
        yield
        time.sleep(7)
        driver.close()
        driver.quit()
        print("Test completed")

    #Buscar pronóstico de una ciudad.
    def test_smn(self, test_setup):
        t = smnHomePage(driver)
        t.abrir_nav_opciones('1')
        t.abrir_opciones_li('pronostico')
        t.buscar_ciudad('Rosario', '1')


    #Probar botones de redes sociales
    def test_verify_social_media_(self, test_setup):
        t = smnHomePage(driver)
        media = ["facebook", "twitter", "youtube", "instagram"]
        t.social_media(media[1])







