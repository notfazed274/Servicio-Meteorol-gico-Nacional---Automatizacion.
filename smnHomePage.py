
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class smnHomePage():
    def __init__(self, driver):
        self.driver = driver
        self.input_search = (By.CLASS_NAME, 'js-typeahead')


    def buscar_ciudad(self, ciudad, index_resultado):
        #String de búsqueda
        input_buscador = self.driver.find_element(*self.input_search)
        input_buscador.send_keys(ciudad)
        #Posición index del resultado
        index_posicion_resultado = self.driver.find_element_by_css_selector(f'li[data-index="{index_resultado}"')
        index_posicion_resultado.click()

    def social_media(self, social):
        self.driver.find_element_by_css_selector(f'a[href*="{social}"]').click()

    def abrir_nav_opciones(self, index):
        self.driver.find_element_by_css_selector(f'.nav.navbar-nav.navbar-right > .dropdown:nth-child({index}) ').click()

    def abrir_opciones_li(self, navLi):
        self.driver.find_element_by_css_selector(f'a[href*="{navLi}"]').click()